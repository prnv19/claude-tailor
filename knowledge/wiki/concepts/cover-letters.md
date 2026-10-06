---
type: concept
sources: [cover-letter-guide.md, ats-friendly-resume-guide.md, describing-ai-work.md]
last_updated: 2026-10-01
status: draft
---

# Cover Letters

How to write a tailored cover letter for a specific `tailored/<Company>/<Role>/` application. Invoked by the `/cover` skill (`skills/cover/SKILL.md`). This page is the authoritative rulebook for cover letter generation.

## Rules for the tailoring agent

1. **On-request only.** Generate a cover letter only when the candidate invokes `/cover` or explicitly asks. Never bundle one into a `tailor` pass uninvited.
2. **Read order before drafting**: this page, then [[voice]], then the role's `resume.tex` + `resume-diff.md` (facts and approved phrasing), then the JD (`jd.md` if saved, otherwise ask the user to paste it). `master-resume.tex` is the fact fallback.
3. **Pain-point extraction**: pull the top 3 tasks from the JD's "What you'll do" / responsibilities section. The letter must address at least 2 of them with concrete evidence. Requirements lists are secondary.
4. **Complement, never repeat the resume**: pick 2-3 of the strongest JD-relevant achievements and give them context and narrative ("why should they care"). Do not enumerate jobs or restate bullets.
5. **Speak their dialect**: mirror JD vocabulary exactly in prose, same casing discipline as [[keywords-and-skills]].
6. **Company hook required, generic praise forbidden**: paragraph 3 needs something real (mission, product, recent project, personal connection). "Your company is a leader in the industry" and equivalents are banned. If no hook is available, ask the user for one, or fall back to the role-focused framing: drawn to the role because the team's focus on X matches experience in Y.
7. **Structure**: greeting to named hiring manager if known, else "Dear Hiring Team" → P1: who + role + the one-line reason the background solves their stated problem → P2: 2-3 achievements with real numbers → P3: why this company + what the candidate brings → P4: thanks + sign-off. Body 200-300 words, always one page.
8. **Truthful**: facts and numbers only from `master-resume.tex` or the approved tailored resume. Same fabrication ban as resumes (Hard Constraint 3). If underqualified for a stated must-have, use honest growth framing with a concrete recent example, never inflation.
9. **60-70% rule**: missing 2-3 requirements is not a blocker. Do not apologize for gaps in the letter, demonstrate understanding of the job instead.
10. **Human voice, mechanically enforced**: no em dashes, no semicolons (Hard Constraints 5-6), no forbidden fluff words (passionate, hardworking, determined, motivated as filler, per [[structure]] Rule 17), no cliches ("I am excited to apply", "proven track record"). Apply the read-aloud test: if a sentence sounds stiff or robotic, rewrite it in the candidate's natural voice.
11. **Draft-first, approved by selection**: show the letter body as plain text before writing any `.tex` (mirrors `diff_first`), and take every question through the choice gates in `skills/cover/SKILL.md` Steps 3, 3.5, and 4 — clarifiers, then gap handling, then a single proceed question. Each question is a multiple-choice selection with a one-line note per option, never an open prose question the candidate has to type an answer to. Only a proceed selection authorizes writing the `.tex`, and a Gate 1/2 answer that materially changes the letter forces a re-draft and a fresh proceed question.
12. **Template and deliverables**: copy the document-class, packages, colors, custom commands, and header block (name/contact/icons) verbatim from `workspace/master-resume.tex` (the source of truth), not from a past tailored cover letter. **Margins and body vspace are the exception** (schema directive 2026-09-10): do not copy the master's space-saving margin block. Use instead:
    ```latex
    \addtolength{\oddsidemargin}{-0.25in}
    \addtolength{\evensidemargin}{-0.25in}
    \addtolength{\textwidth}{0.5in}
    \addtolength{\topmargin}{-0.25in}
    \addtolength{\textheight}{0.5in}
    ```
    (~0.75in margins, header contact line still fits one line) and drop `\raggedright` (keep `\raggedbottom`) so body paragraphs justify like a normal letter. **Dropping `\raggedright` re-enables `article`'s default first-line paragraph indent** (invisible in the resume, which keeps `\raggedright`) — immediately add `\setlength{\parindent}{0pt}` after the margin block so paragraphs stay flush-left, not indented. (A real letter once shipped indented because this line was missing, so it is mandatory.) Separate date/greeting/paragraphs/signature with `\vspace{16pt}`, and use `\vspace{20pt}` before "Sincerely,". Outputs are `cover-letter.tex` + `cover-letter.pdf` in `tailored/<Company>/<Role>/`, compile scratch in `build/<Company>/<Role>/`, same hygiene as resumes.
13. **Education tense**: if the newest Education end date in master is in the past, describe that degree as completed (past tense), never "pursuing" or "expected to graduate". If it reads "Present" or a future month, "pursuing" is correct. (see Synthesis; mechanically checked by `check_resume.py`)
14. **Never reference tailored resumes (or old cover letters) as a template source.** Any file under `tailored/<Company>/<Role>/` (a tailored `resume.tex`, its `resume-diff.md`, or a previous `cover-letter.tex`) may only supply approved facts/phrasing (Rule 2), never the LaTeX preamble, header block, or layout. `master-resume.tex` is the sole template source, always.
15. **Hard Constraint 8 does not apply to cover letters.** The template-spacing lock exists to protect the resume's one-page fit against a career's worth of content, and a short letter has no such pressure. `engine/scripts/check_resume.py` enforces HC8 (preamble-verbatim, vspace-allowlist) on `resume.tex` only. Cover letters use the standard-letter margins/spacing in Rule 12 instead, and deviating from the master's *resume* spacing there is expected, not a violation. Hard Constraints 1 (one page), 3 (truthful), 5 (no em dashes), and 6 (no semicolons/colons) still apply to letters in full.

## Synthesis

Most recruiters do not read cover letters, so they are an **on-request deliverable**, never an automatic part of `tailor`. When they do matter, the winning letter is a clear, honest conversation that connects the candidate's evidence to the JD's top pain points. It must **complement the resume, not replicate it** and read like a human wrote it, since AI-detection tools like GPTZero are run on cover letters even more often than on resumes.

The letter also has a second job the resume cannot do: it is the home for motivation and personal connection. Curiosity/interest content that is banned from resume bullets ("belongs in a cover letter at best") lives here.

Established repo format: centered contact header matching the resume, date, addressee block, 3-4 body paragraphs, "Sincerely". **Canonical source: `workspace/master-resume.tex`** — copy its document-class, packages, colors, custom commands, and header block (name, contact line with FontAwesome icons) verbatim rather than a past tailored artifact, since the master is the only file guaranteed not to drift or get deleted.

**Margins and spacing are the one deliberate divergence from "verbatim"** (schema directive 2026-09-10): the master's margin block (`\addtolength{\oddsidemargin}{-0.6in}` etc.) exists solely to squeeze a multi-role career onto one resume page. A 200-300 word cover letter has no such pressure, so copying that squeeze produces a letter with unnaturally cramped whitespace. Cover letters use their own standard-letter margins (~0.75in) and a roomier vspace rhythm (16pt between blocks, 20pt before the signature) instead — see Rule 12 for the exact values. This is scoped to cover letters only; the resume's margins stay locked under Hard Constraint 8.

Degree tense follows the calendar, not the master's wording. Read the end date of the newest Education entry in `master-resume.tex` and compare it with today's date. Once that date has passed, the degree is **completed** and the letter uses past tense ("I recently completed my Master of Science...", "I earned..."). Never write "pursuing", "expected graduation", or present-tense enrollment language for a degree whose end date is behind us. An end date of "Present" or a future month means the candidate is still enrolled, and "pursuing" is correct. `check_resume.py` derives the same date from master and fails a letter that gets this wrong.

## Disagreements

- **Length and shape of the narrative**: one guide's worked example is a 4-paragraph life-story arc (childhood hook → career journey → achievements → mission alignment), another prescribes a short, problem-focused letter with no biography. **Resolution**: default to the short, pain-point-first shape. A personal-story opening is allowed only when the user supplies a genuine specific connection and approves it in the draft step.
- **Tone latitude**: one guide invites "unique, creative expression of your personal brand", another says no gimmicks, clarity beats cleverness. **Resolution**: clarity wins as the default, consistent with the wiki-wide anti-AI-tone and no-fluff rules.

## Adjacent concepts

- [[voice]] — voice rules apply verbatim to letters, and detection risk is higher for prose than bullets.
- [[keywords-and-skills]] — dialect rule is the prose version of keyword mirroring.
- [[structure]] — forbidden fluff words list is shared.
- [[ats-and-readers]] — the letter targets the recruiter/HM gates, not ATS.
