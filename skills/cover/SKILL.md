---
name: cover
description: Generate a tailored cover letter (cover-letter.tex + cover-letter.pdf) for a specific Company/Role application. Use when the user types /cover or asks for a cover letter for a job, JD, or existing tailored resume.
argument-hint: "[Company] [role-slug]"
allowed-tools:
  - Read(/${CLAUDE_PLUGIN_ROOT}/**)
  - Bash(bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/workspace.sh" *)
  - Bash(bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/compile.sh" *)
  - Bash(test -f *)
  - Bash(test -d *)
---

# /cover: tailored cover letter

Produce a one-page LaTeX cover letter for `workspace/tailored/<Company>/<Role>/`, following the wiki cover letter rulebook. Cover letters are on-request deliverables, never generated automatically during `/tailor`.

Arguments: $ARGUMENTS

Workspace preflight (already run for you):

!`bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/workspace.sh" -C "${CLAUDE_PROJECT_DIR}" status`

- `master=MISSING` or `master=placeholder`: stop and tell the user to run `/setup` first.
- `pdflatex=MISSING` or `latex-packages=MISSING`: say so up front. You can still draft the letter, but nothing compiles until `/setup` sorts the toolchain.
- `today=` is the date for the letter and for the education tense check.

**Paths.** `workspace=` is the absolute path of the user's `workspace/` folder, and every `workspace/...` path below means a path inside it. Call engine scripts as `bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/<name>.sh" -C "${CLAUDE_PROJECT_DIR}" ...`, so they find the workspace from any working directory.

## Step 1: Resolve the target

- If arguments name a company/role (e.g. `/cover NVIDIA ml-engineer`), check that `workspace/tailored/<Company>/<Role>/` exists with `test -d` on that one path, nothing more.
- If no arguments, use the Company/Role most recently discussed in this conversation (e.g. a resume just tailored).
- If neither resolves unambiguously, **ask the user as a choice question** (`AskUserQuestion`): options are the Company/Role targets named in this conversation, and "Other" lets them type one. Do not `ls`, `find`, or glob `tailored/` to build that option list. Browsing past applications is banned (Hard Constraint 9), so the options come only from conversation context.
- A tailored `resume.tex` must exist for the target (`test -f`). If it does not, say so and offer to run `/tailor` first.

## Step 2: Load rules and facts

Read, in order:

0. `${CLAUDE_PLUGIN_ROOT}/engine/rules/hard-constraints.md`: the Hard Constraints referenced by number below.
1. `${CLAUDE_PLUGIN_ROOT}/knowledge/wiki/concepts/cover-letters.md`: the authoritative rulebook. Follow its "Rules for the tailoring agent" exactly.
2. `${CLAUDE_PLUGIN_ROOT}/knowledge/wiki/concepts/voice.md`: voice and drafting rules.
3. The target's `resume.tex` and `resume-diff.md`: approved facts, numbers, and phrasing.
4. The JD: use `jd.md` in the target directory if present. Otherwise ask the user to paste the JD (and save it as `jd.md` in the target directory for future reference).
5. `workspace/master-resume.tex`: fallback for facts not in the tailored resume.

## Step 3: Gate 1, clarifiers (choice-style, batched)

Every question in a `/cover` pass is a **selection**, never a typed answer. Anything the rulebook requires that you don't have becomes a choice question, batched 1-4 at a time into a single `AskUserQuestion` call, each option carrying a one-line note on what picking it does to the letter. Never end a message with an open prose ask like "do you have a hook for this company?".

Typical clarifiers and their option sets:

- **Company hook** (Rule 6): mission angle / specific product or recent news / the user's personal connection / role-focused fallback.
- **Greeting**: "Dear Hiring Team," / a named hiring manager (Other lets the user type the name).
- **Which achievements to feature** (multi-select, 2-3 of them): list each by its resume evidence so the pick is informed.
- **A metric that exists in neither master nor the tailored resume**: never invent one. Options are drop the claim, cite the nearest number that does exist, or the user supplies the real figure via Other.

An affirmative option is phrased as a claim the user is confirming, never as the agent asserting a fact, and a Yes authorizes only what the option text literally says (Hard Constraint 3). Skip Gate 1 entirely if nothing is missing, and say so in one line.

## Step 3.5: Gate 2, gap handling (only if gaps exist)

If the JD names must-haves with no evidence in `master-resume.tex` or the tailored `resume.tex`, ask one choice question per gap, max 4 per call, highest-impact first. Standard option set:

1. **Honest growth framing**: one sentence pairing the gap with a concrete adjacent example (Rule 8).
2. **Cover indirectly**: lean on the nearest real evidence without naming the gap.
3. **Say nothing**: the 60-70% rule (Rule 9). Missing 2-3 requirements is not a blocker, and apologizing for gaps in the letter is banned.

Never auto-select, and never fabricate to close a gap. If there are no material gaps, state "No gaps to address" and move to Step 4.

## Step 4: Draft, then Gate 3, proceed

Write the letter body as **plain text in chat** (not a file). The draft must follow the wiki rulebook, in particular:

- Address at least 2 of the JD's top 3 pain points with concrete evidence.
- 200-300 word body, 3-4 paragraphs, in the rulebook's shape (P1 who + why fit, P2 achievements with real numbers, P3 company hook + what the candidate brings, P4 thanks).
- Complement the resume, never restate its bullets.
- No em dashes, no semicolons, no fluff words (passionate, hardworking, determined, motivated), no cliches, no fabricated facts or numbers.
- Read-aloud test: natural human voice throughout.

Then ask **one** proceed question (`AskUserQuestion`), always last, with the letter's shape recapped in the question (hook used, achievements featured, gaps handled):

1. **Approve and compile**: move to Step 5 and write the `.tex`.
2. **Approve with the tweaks I picked**: apply the selections, then write.
3. **Revise the draft first**: re-draft, no files written.

Only a proceed selection authorizes Step 5. If a Gate 1 or Gate 2 answer, or an approved tweak, materially changes the letter, re-post the revised body and **re-run Gate 3**. Never act on a stale approval.

## Step 5: Write the .tex

- Copy the **document-class, packages, colors, custom commands, and the centered header block** (name + `\faPhone`/`\faEnvelope`/`\faLinkedin`/`\faGithub`/`\faGlobe` contact line) **verbatim** from `workspace/master-resume.tex`, never from a past tailored cover letter, which can drift or be deleted.
- **Margins are the one deliberate exception**: do NOT copy the master's space-saving margin block (`\addtolength{\oddsidemargin}{-0.6in}` etc.). That squeeze exists only because the resume must cram a career onto one page, and a 200-300 word letter doesn't need it. Use this standard-letter margin block instead (the schema default since 2026-09-10, cover letters only, never the resume):
  ```latex
  \addtolength{\oddsidemargin}{-0.25in}
  \addtolength{\evensidemargin}{-0.25in}
  \addtolength{\textwidth}{0.5in}
  \addtolength{\topmargin}{-0.25in}
  \addtolength{\textheight}{0.5in}
  ```
  This gives ~0.75in margins (roomier than the resume, still comfortably one page) while keeping the header's contact line on one line. Also drop `\raggedright` from the body (keep `\raggedbottom`) so the letter's prose paragraphs are justified like a normal letter, not ragged like resume bullets. **Dropping `\raggedright` re-enables `article`'s default first-line paragraph indent** (the master never shows it because `\raggedright` suppresses it). Add `\setlength{\parindent}{0pt}` right after the margin block so letter paragraphs stay flush-left block style instead of indenting. A real letter once shipped indented because this line was missing, so never drop it.
- **Body spacing**: separate the date, greeting, each paragraph, and the signature with `\vspace{16pt}` (use `\vspace{20pt}` right before "Sincerely,"). This is roomier than the resume's tight rhythm on purpose, for the same reason as the margins.
- **Never reference any tailored `resume.tex`, `cover-letter.tex`, or other `tailored/<Company>/<Role>/` artifact as a template source**, not even a recent or well-formatted one. `master-resume.tex` is the only permitted source for the document-class, packages, colors, custom commands, and header. (Tailored `resume.tex` and `resume-diff.md` are still read for facts per Step 2. This rule is about the LaTeX template only.)
- Update only the date (today's), the addressee block (hiring team + company), and the body paragraphs.
- **Education tense**: read the end date of the newest Education entry in `workspace/master-resume.tex` and compare it with today's date. If that date has passed, describe the degree as completed, in the past tense ("I recently completed my Master of Science..."), never "pursuing" or "expected to graduate". If it reads "Present" or a future month, "pursuing" is correct. `check_resume.py` derives the same date and fails a letter that gets it wrong.
- Escape LaTeX special characters in the body (%, &, $, #, _).
- Save as `workspace/tailored/<Company>/<Role>/cover-letter.tex`.

**Hard Constraint 8 (template spacing lock) does not apply to cover letters.** It exists to protect the resume's one-page fit and is enforced only on `resume.tex`. Cover letters use the standard-letter margins and spacing above instead, and `check_resume.py` does not flag them for it. Hard Constraints 1 (one page), 3 (truthful), 5 (no em dashes), and 6 (no semicolons or colons) still apply in full to cover letters.

## Step 6: Compile and deliver

```bash
bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/compile.sh" -C "${CLAUDE_PROJECT_DIR}" "<Company>" "<Role>" cover-letter.tex
```

The script compiles into `workspace/build/<Company>/<Role>/`, copies `cover-letter.pdf` into the tailored folder, removes stray scratch files, and runs `check_resume.py`, which mechanically verifies the letter is one page with no em dashes, no semicolons, no fluff words, no cliches, and no in-progress degree language. A non-zero exit means a violation. Fix the `.tex` and re-run until it passes.

Then verify manually (the checker cannot do this): every number cited appears in `master-resume.tex` or the tailored `resume.tex`.

If the letter overflows one page, cut body content (weakest achievement first). Never shrink fonts or margins.

## Step 7: Report

Tell the user the deliverable paths, which JD pain points the letter addresses, and any gaps deliberately not claimed.
