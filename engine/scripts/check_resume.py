#!/usr/bin/env python3
"""Mechanical Hard Constraint checker for tailored resumes and cover letters.

Usage:
    engine/scripts/check_resume.py [-C PROJECT_DIR] <Company> <Role> [--build-dir DIR]

Checks every grep-able Hard Constraint (engine/rules/hard-constraints.md) against
workspace/tailored/<Company>/<Role>/resume.tex (and cover-letter.tex
if present), using workspace/master-resume.tex as the source of truth:

  resume.tex
    1. No em dash characters anywhere (Hard Constraint 5)
    2. No semicolons or colons (outside template syntax, ratios, and
       times) in the document body (Hard Constraint 6). For 1-2, a line
       copied unchanged from master only warns, since a tailor can't edit
       master
    3. Unique bullet openers across Experience/Projects/Awards (Hard Constraint 4)
    4. No weak openers ("Responsible for", "Worked on", "Helped") or
       first-person pronouns (Hard Constraint 4)
    5. Every master Experience entry present with identical company,
       dates, title, location (Hard Constraint 7)
    6. Compiled PDF is exactly one page (Hard Constraint 1), reporting how
       many text lines spilled past page 1 when pdftotext is installed
    7. Template spacing fidelity (Hard Constraint 8): preamble matches
       master-resume.tex verbatim (comments/whitespace ignored), body
       \vspace values limited to those master uses, and no \itemsep /
       \parsep / \topsep / \addtolength / \setlength in the body
    8. Numeric fidelity (Hard Constraint 3): every number in a tailored
       bullet traces back to master, scoped per employer in Experience
    9. Bullet count caps (Hard Constraint 11): <=3 bullets per Experience
       role, exactly 1 for an internship-titled role, <=2 per project,
       and never 0
   10. Fresh drafting (Hard Constraint 12): no Experience/Projects bullet may
       be a light rewording of a master bullet. Fails when a bullet shares
       a long verbatim word run with, or is too similar overall to, any
       master bullet in the same employer/Projects scope
   11. Reverse-chronological order: Experience and Education entries sorted
       by end date, newest first (ties broken by start date, newest first)
   12. Every entry heading (employer, school, role, project) comes from
       master unchanged, so none is invented or edited (Hard Constraint 3)

  Sections are found by kind: a heading named "Experience" or containing
  it ("Professional Experience"), and likewise for Education, Projects,
  and Awards/Honors, so other titles are checked rather than skipped.

  cover-letter.tex
    - No em dashes / semicolons / colons in body, one page
    - No fluff words (passionate, hardworking, determined, motivated)
      or banned cliches (wiki cover-letters.md Rule 10)
    - Education tense: no "pursuing" / "expected to graduate" once the
      latest Education end date in master has passed

Errors exit 1. Warnings exit 0 and are informational.
"""

import argparse
import calendar
import datetime
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# The workspace is <project dir>/workspace, never the plugin install dir (this
# script may run from the plugin cache). main() resolves the project dir from
# -C, else $CLAUDE_PROJECT_DIR, else the current directory.
WORKSPACE = Path(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()) / "workspace"
MASTER = WORKSPACE / "master-resume.tex"

FLUFF_COVER = re.compile(r"\b(passionate(ly)?|hard-?working|determined|motivated)\b", re.I)
CLICHES = [
    "excited to apply",
    "proven track record",
    "leader in the industry",
    "team player",
    "think outside the box",
]
WEAK_OPENERS = re.compile(r"^\s*(?:was\s+)?(responsible for|worked on|helped)\b", re.I)
FILLER_WARN = re.compile(r"\b(successfully|various|multiple)\b", re.I)

# Hard Constraint 11 caps
INTERN_TITLE = re.compile(r"\b(interns?|internships?|externs?|externships?|co-?op|trainee)\b", re.I)
EXPERIENCE_MAX = 3
INTERN_MAX = 1
PROJECT_MAX = 2

# Fresh-drafting check (Workflow step 3). Calibrated on real tailors: shared
# facts (tool lists, before/after figures, product names) run up to 8
# words, while copied master clauses ran 9-19 words. Overall
# similarity of genuinely rewritten bullets sat at 0.29-0.55, lightly
# reworded ones at 0.61-0.89.
MAX_SHARED_RUN = 9      # words, error at or above
MAX_SIMILARITY = 0.60   # difflib ratio over word lists, error at or above


def strip_comments(text: str) -> str:
    """Remove LaTeX comments (%. .. EOL) but keep escaped \\%."""
    return re.sub(r"(?<!\\)%.*", "", text)


def body_of(text: str) -> tuple[str, int]:
    """Return (body, line offset of \\begin{document})."""
    m = re.search(r"\\begin\{document\}", text)
    if not m:
        return text, 0
    return text[m.end():], text[: m.end()].count("\n")


def read_group(s: str, i: int) -> tuple[str, int]:
    """Read one balanced {...} group starting at s[i] == '{'."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "{" and (j == 0 or s[j - 1] != "\\"):
            depth += 1
        elif c == "}" and s[j - 1] != "\\":
            depth -= 1
            if depth == 0:
                return s[i + 1: j], j + 1
        j += 1
    raise ValueError("unbalanced braces")


def sections(text: str) -> dict:
    """Split document body into {section name (lowercase): content}."""
    out = {}
    parts = re.split(r"\\section\{([^}]*)\}", text)
    for k in range(1, len(parts) - 1, 2):
        name = re.sub(r"\\[a-zA-Z]+\*?", "", parts[k])
        out[norm(name).lower()] = parts[k + 1]
    return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# Which heading holds each kind of content. A heading named exactly after the
# kind wins, else the first heading (in document order) matching the pattern,
# so masters titled "Professional Experience" or "Honors & Awards" are still
# checked instead of silently skipped.
SECTION_KINDS = {
    "experience": re.compile(r"\b(experience|employment|work history|career history)\b"),
    "education": re.compile(r"\beducation\b"),
    "projects": re.compile(r"\bprojects?\b"),
    "awards": re.compile(r"\b(awards?|honou?rs)\b"),
}


def kind_key(secs: dict, kind: str):
    """Name of the section holding `kind` content (names are lowercase), or None."""
    if kind in secs:
        return kind
    return next((name for name in secs if SECTION_KINDS[kind].search(name)), None)


def by_kind(secs: dict) -> dict:
    """{kind: that section's text}, '' where the document has none."""
    return {kind: secs.get(kind_key(secs, kind), "") for kind in SECTION_KINDS}


def macro_calls(text: str, macro: str, nargs: int) -> list:
    """Normalized argument tuples of every \\<macro>{...}...{...} call in text."""
    out = []
    pattern = re.compile(r"\\" + macro + r"\b")
    idx = 0
    while True:
        m = pattern.search(text, idx)
        if not m:
            return out
        pos = m.end()
        args = []
        try:
            for _ in range(nargs):
                while pos < len(text) and text[pos] in " \t\n\r":
                    pos += 1
                if pos >= len(text) or text[pos] != "{":
                    raise ValueError
                arg, pos = read_group(text, pos)
                args.append(norm(arg))
            out.append(tuple(args))
        except ValueError:
            pass
        idx = pos


def subheadings(section_text: str) -> list:
    """(org, dates, title, location) for each \\resumeSubheading call."""
    return macro_calls(section_text, "resumeSubheading", 4)


def subsubheadings(section_text: str) -> list:
    """(title, dates) for each \\resumeSubSubheading call: another role at the
    employer of the \\resumeSubheading above it, such as a promotion."""
    return macro_calls(section_text, "resumeSubSubheading", 2)


def resume_items(section_text: str) -> list:
    """Extract (content, char offset) for each \\resumeItem in a section."""
    out = []
    for m in re.finditer(r"\\resumeItem\s*", section_text):
        pos = m.end()
        if pos < len(section_text) and section_text[pos] == "{":
            try:
                content, _ = read_group(section_text, pos)
                out.append((content, m.start()))
            except ValueError:
                pass
    return out


def opener_of(item: str) -> str:
    """First real word of a bullet, ignoring LaTeX control sequences."""
    cleaned = re.sub(r"\\[a-zA-Z]+\*?", " ", item)
    cleaned = cleaned.replace("{", " ").replace("}", " ")
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", cleaned)
    return words[0] if words else ""


NUM_TOKEN = re.compile(r"[A-Za-z0-9,.]*\d[A-Za-z0-9,.]*")


def num_tokens(text: str) -> set:
    """Numeric tokens in LaTeX text, normalized for comparison against master.

    A token is any run of alphanumerics/commas/dots holding at least one
    digit, so plain metrics ("94", "97.3", "1,200") and versioned
    identifiers ("TD3", "ROS2", "7B", "v2") both round-trip. Commas and
    edge dots are dropped and the token is lowercased, so "1,200" matches
    "1200". Backslashes and "$" break runs, so "\\%" and "$\\sim$500"
    yield "500" rather than dragging markup into the token.
    """
    out = set()
    for tok in NUM_TOKEN.findall(text):
        t = tok.replace(",", "").strip(".").lower()
        if t:
            out.add(t)
    return out


def entries(section_text: str) -> list:
    """[(first \\resumeSubheading arg, chunk text)], one per subheading.

    Each chunk runs from its \\resumeSubheading to the next one, so bullets
    stay attached to the employer/school they belong to.
    """
    marks = [m.start() for m in re.finditer(r"\\resumeSubheading\b", section_text)]
    out = []
    for i, start in enumerate(marks):
        end = marks[i + 1] if i + 1 < len(marks) else len(section_text)
        chunk = section_text[start:end]
        subs = subheadings(chunk)
        out.append((subs[0][0] if subs else "", chunk))
    return out


def employer_text(section_text: str) -> dict:
    """{employer: all of that employer's entry chunks, joined}, so a promotion
    listed as two \\resumeSubheading entries shares one employer scope."""
    out = {}
    for company, chunk in entries(section_text):
        out[company] = out.get(company, "") + chunk
    return out


def roles(chunk: str) -> list:
    """[(title, text)] for each role in one \\resumeSubheading entry chunk: the
    entry's own title, then one per \\resumeSubSubheading under it."""
    subs = subheadings(chunk)
    title = subs[0][2] if subs and len(subs[0]) > 2 else ""
    marks = [m.start() for m in re.finditer(r"\\resumeSubSubheading\b", chunk)]
    if not marks:
        return [(title, chunk)]
    out = [(title, chunk[:marks[0]])]
    for i, start in enumerate(marks):
        part = chunk[start:marks[i + 1] if i + 1 < len(marks) else len(chunk)]
        sub = subsubheadings(part)
        out.append((sub[0][0] if sub else title, part))
    return out


def project_entries(section_text: str) -> list:
    """[(display name, chunk text)], one per \\resumeProjectHeading."""
    marks = [m.start() for m in re.finditer(r"\\resumeProjectHeading\b", section_text)]
    out = []
    for i, start in enumerate(marks):
        end = marks[i + 1] if i + 1 < len(marks) else len(section_text)
        chunk = section_text[start:end]
        flat = norm(re.sub(r"\\[a-zA-Z]+\*?", " ", chunk[:300])).split("$|$")[0]
        name = re.sub(r"[{}]", " ", flat).strip()[:40]
        out.append((name or f"project {i + 1}", chunk))
    return out


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, fname, msg):
        self.errors.append(f"  ERROR [{fname}] {msg}")

    def warn(self, fname, msg):
        self.warnings.append(f"  warn  [{fname}] {msg}")


STRUCTURAL_COLON = re.compile(
    r"\\href\{[a-zA-Z][a-zA-Z0-9+.\-]*:[^}]*\}"  # \href{tel:...}, \href{mailto:...}, \href{https://...}
    r"|\\url\{[^}]*\}"                            # \url{https://...}
    r"|\\textbf\{[^}]*:\}"                        # \textbf{Relevant Coursework:}
    r"|\}\s*\{\s*:"                               # Skills line: \textbf{Category} {: ...}
    r"|(?<=\d):(?=\d)"                            # ratios and times: 1:2, 9:30
)


def check_chars(rep: Report, fname: str, text: str, master_text: str = ""):
    """Em dash anywhere (outside comments), semicolons/colons in body.

    Colons required by template syntax (tel:/mailto:/https: link schemes,
    \\url, the Skills block's \\textbf{Category}{: ...} format, and the
    "Relevant Coursework:" label) and colons between digits (ratios, times)
    are not flagged; only prose colons are. A line copied unchanged from
    master is the master's own text, which a tailor may not edit, so it gets
    a warning pointing at master instead of an error that can't be fixed.
    """
    master_lines = set(normalized_lines(master_text))

    def flag(n: int, line: str, what: str):
        if norm(line) in master_lines:
            rep.warn(fname, f"line {n}: {what} copied unchanged from master-resume.tex, "
                            f"fix it there: {norm(line)[:70]}")
        else:
            rep.error(fname, f"line {n}: {what} found: {norm(line)[:80]}")

    clean = strip_comments(text)
    for n, line in enumerate(clean.splitlines(), 1):
        if "—" in line:
            flag(n, line, "em dash")
    body, offset = body_of(clean)
    for n, line in enumerate(body.splitlines(), offset + 1):
        if ";" in line:
            flag(n, line, "semicolon")
        if ":" in STRUCTURAL_COLON.sub("", line):
            flag(n, line, "colon")


def preamble_of(text: str) -> str:
    return text.split("\\begin{document}")[0]


def normalized_lines(text: str) -> list:
    """Comment-stripped, whitespace-normalized, non-empty lines."""
    return [norm(l) for l in strip_comments(text).splitlines() if norm(l)]


BODY_SPACING_BAN = re.compile(r"\\(itemsep|parsep|topsep|addtolength|setlength)\b")


def check_template_spacing(rep: Report, fname: str, text: str, master_text: str,
                           preamble_must_match: bool):
    """Hard Constraint 8: template spacing is never altered.

    Resumes only. Cover letters are exempt from margin/vspace fidelity
    (see knowledge/wiki/concepts/cover-letters.md Rule 12) since a one-page letter
    doesn't need the resume's space-saving squeeze; they still copy the
    header block (name/contact/colors/icons) and every non-spacing
    preamble line, and still forbid spacing hacks inside the body.
    """
    if preamble_must_match:
        m_lines = normalized_lines(preamble_of(master_text))
        t_lines = normalized_lines(preamble_of(text))
        if m_lines != t_lines:
            import difflib
            changes = [d for d in difflib.unified_diff(m_lines, t_lines, lineterm="", n=0)
                       if d[:1] in "+-" and d[:3] not in ("+++", "---")][:6]
            rep.error(fname, "preamble differs from master-resume.tex (Hard Constraint 8): "
                             + " | ".join(changes)[:300])

    master_body, _ = body_of(strip_comments(master_text))
    body, offset = body_of(strip_comments(text))
    allowed = set(re.findall(r"\\vspace\*?\{([^}]*)\}", master_body))
    for n, line in enumerate(body.splitlines(), offset + 1):
        if preamble_must_match:  # resumes only: letters use their own positive spacing
            for v in re.findall(r"\\vspace\*?\{([^}]*)\}", line):
                if v not in allowed:
                    rep.error(fname, f"line {n}: \\vspace{{{v}}} not used anywhere in master "
                                     f"body, looks like a spacing hack (Hard Constraint 8)")
        if BODY_SPACING_BAN.search(line):
            rep.error(fname, f"line {n}: spacing command in body "
                             f"(Hard Constraint 8): {norm(line)[:80]}")


def check_numeric_fidelity(rep: Report, fname: str, secs: dict, master_secs: dict):
    """Hard Constraint 3: every number in a tailored bullet comes from master.

    Tailoring rewrites bullet prose freely, but a figure may never be
    invented, drifted ("97.3%" -> "97%"), or moved between roles. Experience
    is scoped per employer so a metric cannot migrate from one job to
    another; other sections are scoped to the same section in master, whose
    headings supply tech-stack tokens like "ROS2" and "S3".

    Employers missing from master are skipped here, since the heading check
    already reports them. A section master doesn't have
    (an approved Summary, say) may use any number found anywhere in master.
    """
    master_anywhere = set()
    for text in master_secs.values():
        master_anywhere |= num_tokens(text)

    def flag(label: str, scope: str, content: str, unknown: set):
        for tok in sorted(unknown):
            seen = ("appears elsewhere in master" if tok in master_anywhere
                    else "appears nowhere in master")
            rep.error(fname, f"{label} bullet uses '{tok}', absent from master's "
                             f"{scope} ({seen}), numbers may not be invented or "
                             f"moved (Hard Constraint 3): \"{norm(content)[:60]}...\"")

    exp_key = kind_key(secs, "experience")
    master_exp = employer_text(master_secs.get(kind_key(master_secs, "experience"), ""))
    for company, chunk in entries(secs.get(exp_key, "")):
        if company not in master_exp:
            continue
        allowed = num_tokens(master_exp[company])
        for content, _pos in resume_items(chunk):
            unknown = num_tokens(content) - allowed
            if unknown:
                flag("Experience", f"'{company}' entries", content, unknown)

    for sec_name, sec_text in secs.items():
        if sec_name == exp_key:
            continue
        if sec_name in master_secs:
            allowed, scope = num_tokens(master_secs[sec_name]), f"{sec_name.title()} section"
        else:
            allowed, scope = master_anywhere, "file"
        for content, _pos in resume_items(sec_text):
            unknown = num_tokens(content) - allowed
            if unknown:
                flag(sec_name.title(), scope, content, unknown)


def bullet_words(text: str) -> list:
    """Lowercased word list of a bullet, LaTeX commands and braces removed."""
    t = re.sub(r"\\[a-zA-Z]+\*?", " ", text).replace("{", " ").replace("}", " ")
    return re.findall(r"[a-z0-9][a-z0-9'+.-]*", t.lower())


def check_fresh_drafting(rep: Report, fname: str, secs: dict, master_secs: dict):
    """Workflow step 3: compose each bullet fresh, never string-edit master's.

    Every Experience bullet is compared with master's bullets for the same
    employer, every Projects bullet with all of master's project bullets.
    A bullet fails when it shares a verbatim run of MAX_SHARED_RUN+ words
    with a master bullet, or when its overall word-sequence similarity to
    one reaches MAX_SIMILARITY. Numbers and tool names may repeat (they are
    facts), but master's sentence structure may not. Reusing the closest
    master bullet's opening verb is a warning, not an error.
    """
    import difflib

    def compare(label: str, content: str, pool: list):
        w = bullet_words(content)
        if not w or not pool:
            return
        best_ratio, best_src, best_run, run_text = 0.0, "", 0, ""
        for src in pool:
            mw = bullet_words(src)
            sm = difflib.SequenceMatcher(None, w, mw, autojunk=False)
            ratio = sm.ratio()
            m = sm.find_longest_match(0, len(w), 0, len(mw))
            if ratio > best_ratio:
                best_ratio, best_src = ratio, src
            if m.size > best_run:
                best_run, run_text = m.size, " ".join(w[m.a:m.a + m.size])
        flat = norm(" ".join(w))[:60]
        if best_run >= MAX_SHARED_RUN:
            rep.error(fname, f"{label} bullet copies {best_run} consecutive words from master "
                             f"(\"{run_text[:70]}\"), recompose it from the fact inventory "
                             f"(Hard Constraint 12): \"{flat}...\"")
        elif best_ratio >= MAX_SIMILARITY:
            rep.error(fname, f"{label} bullet is {best_ratio:.0%} similar to master's "
                             f"\"{norm(' '.join(bullet_words(best_src)))[:50]}...\", a light "
                             f"rewording, recompose it from the fact inventory "
                             f"(Hard Constraint 12): \"{flat}...\"")
        if best_src and opener_of(content).lower() == opener_of(best_src).lower():
            rep.warn(fname, f"{label} bullet reuses master's opening verb "
                            f"'{opener_of(content)}' for the same fact, check the JD "
                            f"justifies it: \"{flat[:50]}...\"")

    exp_key = kind_key(secs, "experience")
    master_exp = employer_text(master_secs.get(kind_key(master_secs, "experience"), ""))
    for company, chunk in entries(secs.get(exp_key, "")):
        pool = [c for c, _ in resume_items(master_exp.get(company, ""))]
        for content, _pos in resume_items(chunk):
            compare(f"Experience '{company}'", content, pool)
    proj_key = kind_key(secs, "projects")
    if proj_key and proj_key != exp_key:
        master_proj = [c for c, _ in resume_items(by_kind(master_secs)["projects"])]
        for content, _pos in resume_items(secs[proj_key]):
            compare("Projects", content, master_proj)


HEADING_MACROS = (("resumeSubheading", 4), ("resumeSubSubheading", 2), ("resumeProjectHeading", 2))


def check_headings(rep: Report, fname: str, secs: dict, master_body: str, master_secs: dict):
    """Hard Constraint 3: every entry heading comes from master unchanged.

    Tailoring rewrites bullets, never the employer, school, role, or project
    headings, so a heading master doesn't have was invented or edited. An
    edited heading of a master employer is left to the Hard Constraint 7
    check, which names both versions.
    """
    known = {macro: set(macro_calls(master_body, macro, n)) for macro, n in HEADING_MACROS}
    by_first = {(macro, call[0]): call for macro in known for call in known[macro]}
    master_orgs = {s[0] for s in subheadings(by_kind(master_secs)["experience"])}
    exp_key = kind_key(secs, "experience")
    for sec_name, sec_text in secs.items():
        for macro, nargs in HEADING_MACROS:
            for call in macro_calls(sec_text, macro, nargs):
                if call in known[macro]:
                    continue
                if sec_name == exp_key and macro == "resumeSubheading" and call[0] in master_orgs:
                    continue
                label = norm(re.sub(r"\\[a-zA-Z]+\*?|[{}$|]", " ", call[0]))[:60]
                original = by_first.get((macro, call[0]))
                what = (f"heading for '{label}' was edited (master has {original}, tailored "
                        f"has {call})" if original else f"heading '{label}' is not in master")
                rep.error(fname, f"{sec_name.title()} {what}. Headings are copied from "
                                 f"master-resume.tex, never written or edited (Hard Constraint 3)")


def check_bullet_counts(rep: Report, fname: str, secs: dict):
    """Hard Constraint 11: per-entry bullet caps.

    Internships get exactly 1 bullet, other roles at most 3, projects at
    most 2, and no entry may end up with none. The soft defaults (1 project
    bullet by default, the 2-vs-3 experience ladder) stay judgment calls.
    Caps apply per role, so each \\resumeSubSubheading role under one
    employer is counted on its own.
    """
    sections_by_kind = by_kind(secs)
    for company, chunk in entries(sections_by_kind["experience"]):
        parts = roles(chunk)
        for i, (role, part) in enumerate(parts):
            n = len(resume_items(part))
            if n == 0 and i == 0 and len(parts) > 1:
                continue  # the roles listed under this employer carry the bullets
            intern = bool(INTERN_TITLE.search(role))
            cap = INTERN_MAX if intern else EXPERIENCE_MAX
            if n > cap:
                kind = "internship" if intern else "experience"
                rep.error(fname, f"'{company}' ({role}) has {n} bullets, {kind} cap is "
                                 f"{cap} (Hard Constraint 11)")
            elif n == 0:
                rep.error(fname, f"'{company}' ({role}) has no bullets, every entry keeps "
                                 f"at least 1 (Hard Constraint 11)")
    for name, chunk in project_entries(sections_by_kind["projects"]):
        n = len(resume_items(chunk))
        if n > PROJECT_MAX:
            rep.error(fname, f"project '{name}' has {n} bullets, cap is "
                             f"{PROJECT_MAX} (Hard Constraint 11)")
        elif n == 0:
            rep.error(fname, f"project '{name}' has no bullets (Hard Constraint 11)")


MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
SEASONS = {"winter": 1, "spring": 4, "summer": 7, "fall": 10, "autumn": 10}
# Range separators: LaTeX "--", a hyphen, an en or em dash, or the word "to"
# (as a word only, since "October" contains "to").
DATE_SPLIT = re.compile(r"\s*(?:--|[-–—])\s*|\s+to\s+", re.I)


def parse_month(s: str):
    """'Mar. 2024' -> (2024, 3), 'Present' -> far future, else None.

    Also reads full month names, seasons ('Summer 2024'), MM/YYYY, a bare
    year, and an 'Expected' prefix ('Expected May 2027').
    """
    s = re.sub(r"(?i)^(expected|anticipated|exp\.)\s*", "", s.strip())
    if re.match(r"(?i)(present|current|now|ongoing)\b", s):
        return (9999, 12)
    m = re.match(r"([A-Za-z]+)\.?\s+(\d{4})\b", s)
    if m:
        word = m.group(1).lower()
        if word in SEASONS:
            return (int(m.group(2)), SEASONS[word])
        return (int(m.group(2)), MONTHS[word[:3]]) if word[:3] in MONTHS else None
    m = re.match(r"(\d{1,2})/(\d{4})\b", s)
    if m and 1 <= int(m.group(1)) <= 12:
        return (int(m.group(2)), int(m.group(1)))
    m = re.match(r"(\d{4})$", s)
    return (int(m.group(1)), 12) if m else None


def date_key(date_field: str):
    """Sort key (end, start) for a subheading date like 'Jan. 2026 -- May 2026'."""
    parts = [parse_month(x) for x in DATE_SPLIT.split(date_field) if x.strip()]
    if not parts or None in parts:
        return None
    return (parts[-1], parts[0])


def check_chronology(rep: Report, fname: str, secs: dict):
    """Experience and Education entries must be reverse-chronological.

    Ordered by end date, newest first, with ties broken by start date,
    newest first (so a Jan. 2025 -- Jun. 2025 role precedes a
    Sep. 2023 -- Jun. 2025 one). Reordering entries is never a tailoring
    lever, only bullets within an entry are.
    """
    sections_by_kind = by_kind(secs)
    for sec_name in ("experience", "education"):
        subs = subheadings(sections_by_kind[sec_name])
        keyed = []
        for s in subs:
            k = date_key(s[1])
            if k is None:
                rep.warn(fname, f"{sec_name.title()} '{s[0]}': could not parse dates "
                                f"'{s[1]}', skipped chronology check for it")
                continue
            keyed.append((s[0], s[1], k))
        for (a, ad, ak), (b, bd, bk) in zip(keyed, keyed[1:]):
            if bk > ak:
                want = [n for n, _, _ in sorted(keyed, key=lambda e: e[2], reverse=True)]
                rep.error(fname, f"{sec_name.title()} not reverse-chronological: '{a}' "
                                 f"({ad}) is above '{b}' ({bd}). Expected order: "
                                 f"{' > '.join(want)}")
                break


def latest_education_end(master_text: str):
    """Last day of the newest Education end date in master, or None.

    'Present'/'Current' (still studying) and any unparseable Education date
    return None, which skips the tense check rather than guessing.
    """
    body, _ = body_of(strip_comments(master_text))
    keys = [date_key(s[1]) for s in subheadings(by_kind(sections(body))["education"])]
    if not keys or None in keys:
        return None
    year, month = max(k[0] for k in keys)
    if year == 9999:
        return None
    return datetime.date(year, month, calendar.monthrange(year, month)[1])


def spilled_lines(pdf: Path):
    """Non-empty text lines after page 1 of a PDF, or None without pdftotext."""
    exe = shutil.which("pdftotext")
    if not exe or not pdf.exists():
        return None
    try:
        out = subprocess.run([exe, "-f", "2", str(pdf), "-"], capture_output=True,
                             text=True, timeout=30).stdout
    except (OSError, subprocess.SubprocessError):
        return None
    return sum(1 for line in out.splitlines() if line.strip())


def check_pages(rep: Report, fname: str, build_dir: Path, stem: str):
    log = build_dir / f"{stem}.log"
    if not log.exists():
        rep.warn(fname, f"no build log at {log}, skipped page-count check")
        return
    # pdflatex hard-wraps log lines at ~79 chars, so unwrap before matching
    unwrapped = log.read_text(errors="replace").replace("\n", "")
    m = re.search(r"Output written on .*?\((\d+) pages?", unwrapped)
    if not m:
        rep.warn(fname, "could not parse page count from build log")
    elif int(m.group(1)) != 1:
        spill = spilled_lines(build_dir / f"{stem}.pdf")
        how = (f"{spill} text lines spilled past page 1, cut at least that much in one batch"
               if spill is not None else
               "read page 2 of the PDF to count the spilled lines (pdftotext not installed)")
        rep.error(fname, f"PDF is {m.group(1)} pages, must be exactly 1 (Hard Constraint 1), {how}")


def check_resume(rep: Report, tex_path: Path, build_dir: Path):
    fname = tex_path.name
    text = tex_path.read_text()
    master_text = MASTER.read_text()
    check_chars(rep, fname, text, master_text)
    check_pages(rep, fname, build_dir, tex_path.stem)
    check_template_spacing(rep, fname, text, master_text, preamble_must_match=True)

    body, _ = body_of(strip_comments(text))
    secs = sections(body)

    # Hard Constraint 7: every master Experience entry, verbatim fields
    master_body, _ = body_of(strip_comments(master_text))
    master_secs = sections(master_body)
    master_exp_text = by_kind(master_secs)["experience"]
    tailored_exp_text = by_kind(secs)["experience"]
    master_exp = subheadings(master_exp_text)
    tailored_exp = subheadings(tailored_exp_text)
    for entry in master_exp:
        if entry not in tailored_exp:
            company = entry[0]
            near = [t for t in tailored_exp if t[0] == company]
            if near:
                rep.error(fname, f"Experience entry altered for '{company}': master has "
                                 f"{entry}, tailored has {near[0]} (Hard Constraint 7)")
            else:
                rep.error(fname, f"Experience entry missing: '{company}' "
                                 f"({entry[2]}, {entry[1]}) (Hard Constraint 7)")
    # ...including each role listed under an employer with \resumeSubSubheading
    tailored_by_employer = employer_text(tailored_exp_text)
    for company, chunk in employer_text(master_exp_text).items():
        kept = set(subsubheadings(tailored_by_employer.get(company, "")))
        for role in subsubheadings(chunk):
            if role not in kept:
                rep.error(fname, f"Experience role missing or altered under '{company}': "
                                 f"master has {role} (Hard Constraint 7)")

    # Hard Constraint 3: no invented or edited employer, school, role, or project
    check_headings(rep, fname, secs, master_body, master_secs)

    # Experience/Education entries newest first
    check_chronology(rep, fname, secs)

    # Hard Constraint 3: no invented or drifted numbers
    check_numeric_fidelity(rep, fname, secs, master_secs)

    # Hard Constraint 11: per-entry bullet caps
    check_bullet_counts(rep, fname, secs)

    # Hard Constraint 12: bullets composed fresh, not string-edited from master
    check_fresh_drafting(rep, fname, secs, master_secs)

    # Hard Constraint 4: unique openers + no weak openers, Experience/Projects/Awards
    seen = {}
    dupes = {}
    opener_sections = []
    for kind in ("experience", "projects", "awards"):
        key = kind_key(secs, kind)
        if key and key not in opener_sections:
            opener_sections.append(key)
    for sec_name in opener_sections:
        for content, _pos in resume_items(secs[sec_name]):
            flat = norm(re.sub(r"\\[a-zA-Z]+\*?", " ", content).replace("{", " ").replace("}", " "))
            if flat.lower().startswith("relevant coursework"):
                continue
            if WEAK_OPENERS.search(flat):
                rep.error(fname, f"weak opener in {sec_name}: \"{flat[:70]}...\"")
            if re.match(r"^\s*(I|My|We)\b", flat):
                rep.error(fname, f"first-person pronoun opens a {sec_name} bullet: \"{flat[:70]}...\"")
            opener = opener_of(content)
            if not opener:
                continue
            key = opener.lower()
            if key in seen:
                d = dupes.setdefault(key, {"verb": opener, "count": 1, "secs": {seen[key]}})
                d["count"] += 1
                d["secs"].add(sec_name)
            else:
                seen[key] = sec_name
            if FILLER_WARN.search(flat):
                rep.warn(fname, f"filler word in {sec_name} bullet: \"{flat[:70]}...\"")
    if dupes:
        # One aggregated error per verb, not one per occurrence
        parts = [f"'{d['verb']}' x{d['count']} ({'/'.join(sorted(d['secs']))})"
                 for d in sorted(dupes.values(), key=lambda d: -d["count"])]
        rep.error(fname, f"duplicate openers, each verb may open only one bullet "
                         f"(unique-openers rule): {', '.join(parts)}")


def check_cover_letter(rep: Report, tex_path: Path, build_dir: Path):
    fname = tex_path.name
    text = tex_path.read_text()
    master_text = MASTER.read_text()
    check_chars(rep, fname, text, master_text)
    check_pages(rep, fname, build_dir, tex_path.stem)
    check_template_spacing(rep, fname, text, master_text, preamble_must_match=False)

    body, offset = body_of(strip_comments(text))
    for n, line in enumerate(body.splitlines(), offset + 1):
        if FLUFF_COVER.search(line):
            rep.error(fname, f"line {n}: fluff word ({FLUFF_COVER.search(line).group(0)}): "
                             f"{norm(line)[:80]}")
        for cliche in CLICHES:
            if cliche in line.lower():
                rep.error(fname, f"line {n}: cliche '{cliche}': {norm(line)[:80]}")
    grad = latest_education_end(master_text)
    if grad and datetime.date.today() > grad:
        if re.search(r"\b(pursuing|expected to graduate|expected graduation)\b", body, re.I):
            rep.error(fname, f"degree described as in-progress, but master's latest Education "
                             f"entry ended {grad:%b %Y} (wiki cover-letters.md Rule 13)")


def main():
    global WORKSPACE, MASTER
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-C", dest="project", default=None,
                    help="project dir holding workspace/ (default: $CLAUDE_PROJECT_DIR, "
                         "else the current directory)")
    ap.add_argument("company")
    ap.add_argument("role")
    ap.add_argument("--build-dir", type=Path, default=None,
                    help="dir holding pdflatex .log files (default: workspace/build/<Company>/<Role>)")
    args = ap.parse_args()
    if args.project:
        WORKSPACE = Path(args.project) / "workspace"
        MASTER = WORKSPACE / "master-resume.tex"

    tailored = WORKSPACE / "tailored" / args.company / args.role
    build_dir = args.build_dir or WORKSPACE / "build" / args.company / args.role
    if not tailored.is_dir():
        sys.exit(f"No such tailored dir: {tailored}")
    if not MASTER.exists():
        sys.exit(f"Master not found: {MASTER}")

    rep = Report()
    checked = []
    resume = tailored / "resume.tex"
    if resume.exists():
        check_resume(rep, resume, build_dir)
        checked.append("resume.tex")
    letter = tailored / "cover-letter.tex"
    if letter.exists():
        check_cover_letter(rep, letter, build_dir)
        checked.append("cover-letter.tex")
    if not checked:
        sys.exit(f"Nothing to check in {tailored} (no resume.tex or cover-letter.tex)")

    if not (tailored / "jd.md").exists():
        rep.warn("jd.md", "missing: save the job description as jd.md in this folder")

    print(f"check_resume: {args.company}/{args.role} ({', '.join(checked)})")
    for w in rep.warnings:
        print(w)
    for e in rep.errors:
        print(e)
    if rep.errors:
        print(f"FAIL: {len(rep.errors)} constraint violation(s)")
        sys.exit(1)
    print(f"PASS{' (' + str(len(rep.warnings)) + ' warning(s))' if rep.warnings else ''}")


if __name__ == "__main__":
    main()
