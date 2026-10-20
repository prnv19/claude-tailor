---
name: setup
description: First-time setup for resume tailoring. Checks the LaTeX/Python toolchain, creates workspace/ in the current folder, and builds workspace/master-resume.tex by importing the user's existing resume (PDF, DOCX, .tex, .md, or .txt dropped into workspace/inbox/) into the template. Use when the user types /setup, is starting out, wants to load or re-import their resume, or when /tailor or /cover reports a missing or placeholder master.
argument-hint: "[optional: path to your current resume]"
allowed-tools:
  - Bash(bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/workspace.sh" *)
  - Bash(textutil -convert txt -stdout *)
  - Bash(pdftotext *)
  - Bash(test -f *)
---

# /setup: build the master resume

Get the user from nothing to a compiled `workspace/master-resume.tex` that holds everything true about their career. Every later `/tailor` and `/cover` picks from this file, so its accuracy and completeness cap the quality of every application.

Source given with the command (a file path, or empty):

$ARGUMENTS

Preflight (already run for you):

!`bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/workspace.sh" -C "${CLAUDE_PROJECT_DIR}" status`

`workspace=` is the absolute path where everything lands: `workspace/` inside the folder Claude Code was started from. Use that absolute path for every workspace file below. Call the engine as `bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/workspace.sh" -C "${CLAUDE_PROJECT_DIR}" <command>`. Run each one as its own command, exactly in that form: never chain `;`, `&&`, `|`, or extras like `echo $?` or `pdfinfo` onto it. The pre-approved patterns match only the bare command, so anything added stops the user with a permission prompt, and the exit status reaches you anyway.

All questions go through `AskUserQuestion` as choices with a one-line consequence note per option, never open prose.

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
2. Run `workspace.sh init`. It creates `workspace/inbox/`, `workspace/applications/`, and `workspace/build/`, and copies the template in only when no master exists.
3. If `gitignore=MISSING` (the folder is a git repo and `workspace/` is not ignored), ask: **Add workspace/ to .gitignore** (recommended, keeps resumes and PII out of commits) / **Leave it**. On yes, append a `workspace/` line to the project's `.gitignore`.

## Step 3: Get the source resume

The resume comes from a file, never pasted text (pasting long documents into a terminal is error-prone).

The user only ever saves files in their project folder (`${CLAUDE_PROJECT_DIR}`, the folder they ran Claude Code from). Moving them into `workspace/inbox/` is your job.

1. If `$ARGUMENTS` is a path, confirm it with `test -f <path>` and use it.
2. Otherwise look at the preflight's `inbox-file=` lines (files already in the inbox) and `project-file=` lines (files in the project folder). Judge which ones are resumes from their names, and open a file to check if the name doesn't tell you. One resume: name it in one line. Several: ask which to import (multi-select, since several sources such as an old resume and a LinkedIn export are welcome).
3. Move each chosen `project-file` into the inbox with `workspace.sh intake "<file name>"`, and read it from its new inbox path.
4. **Nothing detected:** tell the user to save their resume (PDF, DOCX, .tex, .md, or .txt) in `${CLAUDE_PROJECT_DIR}` (print the absolute path). Then ask: **I've added it, check again** (re-run `workspace.sh status` and go back to 2) / **Fill it in myself later** (stop after Step 2, the master stays placeholder and `/tailor` will refuse it). Repeat until a file is found or the user stops.

After the master is written (Step 4), run `workspace.sh done "<file name>"` for each inbox file used, so it moves to `inbox/processed/` and isn't picked up again.

Read the source:

- `.pdf`: Read it directly. If the text comes out garbled, try `pdftotext -layout`.
- `.docx`: `textutil -convert txt -stdout <file>` on macOS. Elsewhere, ask the user to export it to PDF and save that in the project folder.
- `.tex`: read it. If its preamble is already this template's (it came from this plugin), keep its content as is. Otherwise it is the user's own layout, so ask **one** question: **Convert to the bundled template** (Jake's Resume layout. The content moves over, the original look is not kept) / **Keep my own layout** (the agent adapts the file so the tailoring engine can work with it, Step 4b). Never convert a custom layout without asking.
- `.md`/`.txt`: use as is.

Multiple sources (an old resume plus a LinkedIn export) are welcome: the master should hold the union.

## Step 3.5: Confirm what you know (before writing anything)

**Show the profile.** Post everything you extracted, as a readable summary, not LaTeX:
- Contact: name, phone, email, location, links.
- Education: each degree with school, dates, GPA, coursework.
- Experience: each role with employer, title, dates, location, and its bullets in short form.
- Projects: name, stack, dates, the gist.
- Skills, and any other sections (certifications, publications, awards).

**Check the resume.** List concrete issues under the profile:
- Missing or inconsistent dates, locations, or titles.
- Overlapping or unexplained date gaps.
- Abbreviations or acronyms that need expanding.
- Text you couldn't place in a section.
- Contact links that look broken.
- Bullets with no number in them, grouped by role. `/tailor` can only use figures that are in the master, so every real metric added here (team size, users, latency, %, $, time saved) strengthens every future application.

**Ask, in one `AskUserQuestion` call:**
1. **Is this profile correct and complete?** Options: **All correct** / **Something is wrong** (they say what via Other or a follow-up) / **There's more to add** (roles, projects, skills, certifications, or links the resume left out, which the master should hold even if no single resume ever showed them).
2. **Clarifiers, 1-3 more questions** (the 4-question limit includes question 1), one per issue that matters most. Options come from what the file shows. Example: "End date for Acme?" with **Still there (Present)** / **Ended** (Other: type the month). A metric question offers **No number for this** alongside letting the user type the figure via Other.

If more issues remain after the answers, ask another batch the same way. Then post the corrected profile once more if anything changed, and continue only after an **All correct**. Everything the user adds goes through the truthfulness rule: only what they state, exactly as they state it.

## Step 4: Write the master

For **Keep my own layout**, skip to Step 4b. Otherwise edit `workspace/master-resume.tex` (the template copy):

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

## Step 4b: Adapt the user's own layout

The engine scripts are shared, read-only plugin code and are never edited. They don't depend on Jake's look, only on a fixed set of commands in the body and on every tailored preamble matching the master's. So the user's file is restructured to speak that interface, while its preamble and look stay theirs.

1. Run `workspace.sh backup` (if a master exists), then replace `workspace/master-resume.tex` with the user's `.tex`.
2. **Preamble: keep everything** (packages, fonts, colors, margins, `\titleformat`, their own macros). Add one clearly commented block at the end of it, `% --- resume-tailorer interface ---`, that defines (with `\newcommand`, or `\renewcommand` if the user already has one of these names) every command the engine reads, **rendered with the user's own styling** (copy the spacing, fonts, and alignment from how their file currently formats an entry):
   - `\resumeSubheading{Org}{Dates}{Title}{Location}`, `\resumeSubSubheading{Title}{Dates}`
   - `\resumeProjectHeading{Heading}{Dates}`
   - `\resumeItem{text}`, `\resumeItemListStart`/`\resumeItemListEnd`, `\resumeSubHeadingListStart`/`\resumeSubHeadingListEnd`
   If the file's text doesn't map to Unicode cleanly for ATS parsers, add `\input{glyphtounicode}` and `\pdfgentounicode=1` there too.
3. **Body:** rewrite every entry to use those commands, with the content rules of Step 4 (standard section titles, date format, punctuation, include everything, transcribe facts exactly). All vertical spacing must live inside the macro definitions, never as `\vspace` in the body (Hard Constraint 8). Keep the user's header markup as is.
4. Compile (Step 5), then compare the result with their original (compile or read their original PDF if they have one). Fix any visible drift in the macro definitions, not in the body.
5. **Measure the page capacity.** The `/tailor` content budget is measured for the bundled template, so a custom layout needs its own. If `compile-master` printed `page1-lines=<n>`, that's the capacity estimate. If the master fits on one page, there's nothing to measure yet: write `unmeasured`. Write `workspace/layout.md`:
   ```
   # Layout
   template: custom (adapted from <source file name>, <today>)
   page-capacity: <n> lines | unmeasured
   budget: <n - 2> lines | unmeasured
   ```
6. In Step 6, also tell the user what was added (the interface block) and that editing those definitions changes how every future tailored resume looks.

## Step 5: Compile

Run `workspace.sh compile-master`. On a LaTeX error, fix the offending line (usually an unescaped special character) and re-run until it compiles. A custom preamble may load packages the toolchain check doesn't cover. Name a missing `.sty` from the log, with the install command, the same way as Step 1. The page count is informational only. It also puts a review copy at `${CLAUDE_PROJECT_DIR}/master-resume.pdf`, next to the user's own files.

## Step 6: Review gate

The facts were confirmed in Step 3.5, so this gate is about the compiled file. Post a short summary: entries per section, bullets per role, page count, and anything that changed while writing it (a section renamed, an entry split for a promotion).

Point the user to the review copy by its absolute path, `${CLAUDE_PROJECT_DIR}/master-resume.pdf`, never the build folder. Ask one question: **Looks right, done** / **Fix something** (the user supplies corrections, you apply them and recompile, which refreshes the review copy) / **I'll edit the file myself** (edit `workspace/master-resume.tex`, then run `/setup` and pick **Just recompile it**).

On **Looks right, done**, run `workspace.sh approve-master`. It moves the review copy to `workspace/master-resume.pdf`, so the project folder is left clean.

Corrections go through the same truthfulness rule: only what the user states.

## Step 7: Report

Tell the user:

- The master path, and that `workspace/` is gitignored (or isn't), so they should **keep their own backup** of the master outside this folder.
- Next step: run `/tailor` and paste the job description, or `/tailor file: <path>` if it's saved in a file.
