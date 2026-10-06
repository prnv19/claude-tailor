---
name: setup
description: First-time setup for resume tailoring. Checks the LaTeX/Python toolchain, creates workspace/ in the current folder, and builds workspace/master-resume.tex by importing the user's existing resume (PDF, DOCX, .tex, or pasted text) into the template. Use when the user types /setup, is starting out, wants to load or re-import their resume, or when /tailor or /cover reports a missing or placeholder master.
argument-hint: "[path to your current resume (PDF, DOCX, .tex, .md), or paste it]"
allowed-tools:
  - Bash(bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/workspace.sh" *)
  - Bash(textutil -convert txt -stdout *)
  - Bash(pdftotext *)
  - Bash(test -f *)
---

# /setup: build the master resume

Get the user from nothing to a compiled `workspace/master-resume.tex` that holds everything true about their career. Every later `/tailor` and `/cover` picks from this file, so its accuracy and completeness cap the quality of every application.

Source given with the command (a path, pasted resume text, or empty):

$ARGUMENTS

Preflight (already run for you):

!`bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/workspace.sh" -C "${CLAUDE_PROJECT_DIR}" status`

`workspace=` is the absolute path where everything lands: `workspace/` inside the folder Claude Code was started from. Use that absolute path for every workspace file below. Call the engine as `bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/workspace.sh" -C "${CLAUDE_PROJECT_DIR}" <command>`.

All questions go through `AskUserQuestion` as choices with a one-line consequence note per option, never open prose (except asking the user to paste text, where there is nothing to choose).

## Step 1: Toolchain

From the preflight:

- `python3=MISSING`: required for the constraint checker. Point to python.org or `brew install python`.
- `pdflatex=MISSING`: required to produce PDFs. macOS: MacTeX (`brew install --cask mactex-no-gui`). Debian/Ubuntu: `sudo apt-get install texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-lang-english`. Windows: MiKTeX or TeX Live.
- `latex-packages=MISSING <names>`: the template's preamble needs these, and the names are TeX Live package names. TeX Live, MacTeX, or BasicTeX: `sudo tlmgr install <names>`. Debian/Ubuntu (where `tlmgr` is disabled): the `apt-get` line above. MiKTeX: its console, or let it install on first compile.
- `pdftotext=MISSING`: optional. It gives the overflow line count and the plain-text ATS check. macOS: `brew install poppler`. Debian/Ubuntu: `sudo apt-get install poppler-utils`. Mention it once, never ask about it: without it, PDFs are read directly.

If `python3`, `pdflatex`, or `latex-packages` is missing, give the exact install command and ask: **Continue setup anyway** (import the master now, compile later) / **Stop, I'll install first**. Never install software yourself.

## Step 2: Workspace and git safety

1. If `master=ok` already exists, ask before touching it: **Keep my master** (stop here, report it is ready) / **Re-import from a new resume** (the current master is backed up first) / **Just recompile it** (jump to Step 5).
   - Re-import: first run `workspace.sh backup`, which copies it to `workspace/master-resume.backup-<date>.tex`. Never overwrite a master without that backup.
2. Run `workspace.sh init`. It creates `workspace/tailored/` and `workspace/build/`, and copies the template in only when no master exists.
3. If `gitignore=MISSING` (the folder is a git repo and `workspace/` is not ignored), ask: **Add workspace/ to .gitignore** (recommended, keeps resumes and PII out of commits) / **Leave it**. On yes, append a `workspace/` line to the project's `.gitignore`.

## Step 3: Get the source resume

Use `$ARGUMENTS` if it is a path (confirm it with `test -f <path>`) or resume text. Otherwise ask: **I'll give a file path** (Other: type it) / **I'll paste it** / **Fill it in myself later** (stop after Step 2, the master stays placeholder and `/tailor` will refuse it).

Read the source:

- `.pdf`: Read it directly. If the text comes out garbled, try `pdftotext -layout`.
- `.docx`: `textutil -convert txt -stdout <file>` on macOS. Elsewhere, ask the user to export to PDF or paste the text.
- `.tex`: read it. If it already uses this template's macros, keep its content as is.
- `.md`/`.txt`/pasted: use as is.

Multiple sources (an old resume plus a LinkedIn export) are welcome: the master should hold the union.

## Step 4: Write the master

Edit `workspace/master-resume.tex` (the template copy):

- **Preamble untouched.** Everything above `\begin{document}` stays byte-for-byte. The checker compares every tailored resume's preamble against it. Delete the `PLACEHOLDER CONTENT` comment block.
- **Header:** name, phone, email, LinkedIn, GitHub in the template's `\href` + `\fa...` pattern. Drop an icon's `\href` if the user has no such link. Never invent one.
- **Section titles:** the standard ones that ATS parsers and the checker look for: `Education`, `Experience`, `Projects`, and plain names for the rest (`Certifications`, `Licenses`, `Publications`, `Awards`). A source's "Professional Experience" or "Work History" becomes `Experience`. Title the skills section for the field (`Skills`, `Technical Skills`, `Clinical Skills`).
- **Education, Experience:** one `\resumeSubheading{Org}{Dates}{Title or degree}{Location}` per role, reverse-chronological (newest end date first). A promotion at the same employer is a second entry with the same organization name. Dates as `Mon. YYYY -- Mon. YYYY` or `-- Present` (e.g. `Jun. 2024 -- Present`), the format the checker parses.
- **Punctuation that can't ship:** every tailored resume copies master's headings and entry lines, and Hard Constraints 5 and 6 ban em dashes, semicolons, and prose colons. Write date ranges with `--`, turn em dashes and semicolons into commas or periods, and put a label's colon inside `\textbf{...:}` like the template's `Relevant Coursework:` label (`\textbf{GPA:} 3.8`, never `GPA: 3.8`).
- **Projects:** `\resumeProjectHeading{\textbf{Name} $|$ \emph{Stack}}{}`.
- **Skills:** the `\textbf{Category}{: ...}` rows.
- **Other sections** (Publications, Awards, Certifications): keep them if the source has them, in the same itemize style as the template's Publications. Delete template sections the user has no content for.
- **Include everything.** The master may run past one page. More real bullets per role (4-6 is fine) give `/tailor` more to choose from. The one-page limit applies only to tailored resumes.
- **Transcribe, never improve facts.** Numbers, tools, titles, dates, and employer names exactly as the source states them. No rounding, no added metrics, no inferred tools. Rewording for clarity is fine. Escape LaTeX specials (`%` → `\%`, `&` → `\&`, `$`, `#`, `_`).
- Don't polish bullets into XYZ form here. `/tailor` rewrites bullets per JD from the facts. The master's job is to hold the facts completely and precisely.

## Step 5: Compile

Run `workspace.sh compile-master`. On a LaTeX error, fix the offending line (usually an unescaped special character) and re-run until it compiles. The page count is informational only.

## Step 6: Review gate

Post a short import summary: entries per section, bullets per role, and anything uncertain (a missing date or location, a title you had to infer, text that didn't map to any section). Then list **bullets with no number in them**, grouped by role. `/tailor` can only use figures that are in the master, so every real metric added here (team size, users, latency, %, $, time saved) strengthens every future application.

Ask one question: **Looks right, done** / **Fix the flagged items** (the user supplies corrections, you apply them and recompile) / **I'll edit the file myself**.

Corrections go through the same truthfulness rule: only what the user states.

## Step 7: Report

Tell the user:

- The master path, and that `workspace/` is gitignored (or isn't), so they should **keep their own backup** of the master outside this folder.
- Next step: `/tailor` followed by a pasted job description.
