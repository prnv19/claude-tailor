# Resume Tailorer: Complete Usage Guide

This guide takes you from installing the plugin to a compiled, tailored PDF. The behavior it describes is defined by the plugin's skills (`skills/`) and the Hard Constraints (`engine/rules/hard-constraints.md`).

---

## Table of contents

1. [How the system works](#1-how-the-system-works)
2. [Prerequisites](#2-prerequisites)
3. [Install the plugin](#3-install-the-plugin)
4. [/setup: your master resume](#4-setup-your-master-resume)
5. [/tailor: tailoring for a job](#5-tailor-tailoring-for-a-job)
6. [Reviewing the diff and answering the gates](#6-reviewing-the-diff-and-answering-the-gates)
7. [/cover: cover letters](#7-cover-cover-letters)
8. [Compiling and checking](#8-compiling-and-checking)
9. [Updating your master](#9-updating-your-master)
10. [Maintaining the knowledge base](#10-maintaining-the-knowledge-base)
11. [Troubleshooting](#11-troubleshooting)

---

## 1. How the system works

```
┌─────────────────────────────────────────────────────────────┐
│  Layer 3: schema                                            │
│  skills/ (/setup, /tailor, /cover) + engine/rules/          │
│  hard-constraints.md → workflow, gates, Hard Constraints    │
└───────────────────────────┬─────────────────────────────────┘
                            │ reads
┌───────────────────────────▼─────────────────────────────────┐
│  Layer 2: knowledge/wiki/ (rulebook, concepts, sources)     │
│  → Compiled, candidate-agnostic resume rules                │
└───────────────────────────┬─────────────────────────────────┘
                            │ sourced from
┌───────────────────────────▼─────────────────────────────────┐
│  Layer 1: knowledge/raw/ (immutable research notes)         │
└─────────────────────────────────────────────────────────────┘

  Engine:     engine/scripts/ (workspace, scaffold, compile, check)
  Your data:  ./workspace/master-resume.tex   (in YOUR folder)
  Outputs:    ./workspace/applications/<Company>/<Role>/
              (resume.tex, resume-diff.md, jd.md, resume.pdf)
```

The plugin (rules, wiki, engine) is installed once. Your data lives in a `workspace/` folder inside whichever directory you run Claude Code from, for example `~/job-search/workspace/`. The skills load only when you invoke them, so they cost nothing in other sessions.

**A typical `/tailor`:**

1. You run `/tailor` and paste the JD (or point it at a file with `file: <path>`).
2. The agent reads the Hard Constraints and the rulebook, then works out the company and role from the JD.
3. It scores everything in your **master** against the JD's requirements, selects the most relevant experiences, projects, and bullets, and shows a **diff proposal**. No files are written yet. This works the same for any field.
4. It runs **three choice gates**, and you answer by picking options, never by typing.
5. It scaffolds `workspace/applications/<Company>/<Role>/resume.tex` (a byte-identical copy of your master's preamble), regenerates each entry's bullets from your master's facts, and saves the JD as `jd.md`.
6. It compiles the PDF and runs the mechanical Hard Constraint checks.
7. It writes `resume-diff.md` **last**, once the PDF is final.

The agent never invents experience or metrics. If the JD asks for something you don't have, it lists it under **Gaps to discuss**.

---

## 2. Prerequisites

| Requirement | Why |
|-------------|-----|
| **[Claude Code](https://claude.com/claude-code)** | Runs the plugin |
| **LaTeX (`pdflatex`)** with the template's packages | Builds every PDF. The contact icons use `fontawesome7` when installed, else `fontawesome5` |
| **Python 3** (standard library only) | Runs the mechanical checks and the workspace guard |
| **`pdftotext`** (poppler), optional | Counts overflow lines and runs the plain-text ATS check. Without it, the agent reads PDFs directly |

**Install LaTeX.** macOS: `brew install --cask mactex-no-gui` (BasicTeX works too, after `sudo tlmgr install` of the packages `/setup` names). Ubuntu/Debian: `sudo apt-get install texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-lang-english`. Windows: [MiKTeX](https://miktex.org/), with Claude Code running on Git Bash (the engine scripts are bash). `/setup` checks every file the template's preamble loads and gives the exact install command for anything missing.

**Install `pdftotext`** (optional): `brew install poppler` on macOS, `sudo apt-get install poppler-utils` on Ubuntu/Debian.

---

## 3. Install the plugin

**From GitHub:**

```
/plugin marketplace add prnv19/claude-tailor
/plugin install resume-tailorer@resume-tailorer
```

**From a local clone** (for development):

```bash
claude --plugin-dir /path/to/claude-tailor          # this session only
```

or, to install it persistently, `/plugin marketplace add /path/to/claude-tailor` followed by the same `/plugin install` line.

Then make a folder for your job search and start Claude Code there:

```bash
mkdir ~/job-search && cd ~/job-search && claude
```

Commands appear as `/setup`, `/tailor`, `/cover` (or `/resume-tailorer:tailor` if another plugin uses the same name).

---

## 4. /setup: your master resume

```
/setup ~/Documents/my-resume.pdf
```

Save your resume (PDF, DOCX, `.tex`, `.md`, or `.txt`) in the folder you run Claude Code from, or pass a path. `/setup` finds it and moves it into `workspace/inbox/`. If there's nothing to find, it asks you to save it there and checks again. Before writing anything, it shows everything it learned about you, flags anything unclear in the resume, and asks whether the profile is correct and complete. A Word, PDF, or text resume is rebuilt in the bundled template (Jake's Resume layout). A `.tex` resume in your own layout gets a choice: convert it to the bundled template, or keep your layout. If you keep it, `/setup` adds a small block to your preamble that defines the commands the tailoring engine reads, styled like the rest of your resume, and measures how many lines fit on one page so `/tailor` can plan the budget. Several sources (old resume plus a LinkedIn export) are welcome, and the master gets the union. `/setup`:

1. Checks `python3`, `pdflatex`, every LaTeX package the template needs, and the optional `pdftotext`, giving the exact install command for anything missing.
2. Creates `workspace/` (and offers to add it to `.gitignore` if your folder is a git repo).
3. Imports your resume into the template's LaTeX macros, transcribing every fact exactly.
4. Compiles the master and reports anything uncertain (missing dates, inferred titles).
5. Lists the bullets that have **no numbers**. `/tailor` can only use figures that are in your master, so adding real metrics here improves every future application.

**What "master" means:** one file with everything true about your career, every role, project, and skill you can defend in an interview, with exact numbers. It may run past one page. Tailoring copies from it and never changes it.

**Conventions** the checker relies on: dates as `Mon. YYYY -- Mon. YYYY` or `-- Present`, newest first. Numbers written exactly as you'd defend them (`97.3\%`, `$\sim$5000`, `1,200+`), because every tailored number must appear in master byte-for-byte. The preamble (above `\begin{document}`) stays untouched.

> **Back up your master.** `workspace/` is meant to stay out of git, so keep a copy somewhere safe (a private repo, a cloud drive, dated copies). Re-running `/setup` on an existing master makes a dated backup before re-importing.

---

## 5. /tailor: tailoring for a job

Paste the **full** posting (responsibilities, requirements, nice-to-haves) after the command, or run `/tailor` alone and paste it when asked. If it's saved in a file, use `/tailor file: <path>` instead (PDF, DOCX, `.md`, or `.txt`). A file in your folder is moved into `workspace/inbox/`, and a file elsewhere is read where it is, so approve the read if Claude Code asks. It only uses a file you name and never fetches URLs. The JD is saved as the application's `jd.md`. If the company or role isn't in the JD, it asks you. After the clarifiers and gap questions, it shows the company, role, output folder, and planned changes, and asks you to confirm before writing anything.

```
/tailor <paste the full job description>
/tailor file: ~/Downloads/acme-jd.pdf
```

You don't have to name the company or role. The agent takes them from the JD (or from `Company:` / `Role:` lines you add), derives the folder slugs (`workspace/applications/Procter-and-Gamble/brand-manager/`), and asks you before doing anything else when either is missing or ambiguous. If that Company/Role was already tailored, it asks whether to overwrite, use a new slug, or abort.

**Steering** goes after the JD in the same message:

```
/tailor <JD>

Steering: GenAI role, prioritize LLM and eval bullets. Keep the forecasting project. I have no Kubernetes in production.
```

---

## 6. Reviewing the diff and answering the gates

The proposal includes a **keyword map** (JD term → resume evidence), **section changes** (BEFORE → AFTER with a reason each), **dropped** content, **gaps to discuss**, and a **projected budget** ("~49/52 lines").

Then the gates:

- **Gate 1, clarifiers**: anything that would change the draft (an unstated tool you really used, which projects to feature), batched into one prompt. Skipped when nothing is unclear.
- **Gate 2, gap handling**: one question per JD requirement with no evidence in master: add a truthful bullet, cover indirectly, leave as a gap, or drop the keyword.
- **Gate 3, proceed**: always last, and the only thing that authorizes writing files. Pick **Revise the diff first** to iterate.

**Outputs** in `workspace/applications/<Company>/<Role>/`: `resume.tex`, `resume-diff.md` (changelog with keyword map), `jd.md` (the JD verbatim), `resume.pdf`.

**One-page overflow:** the checker reports how many lines spilled onto page 2, and the agent cuts at least that much in one pass, in this order: trim filler → demote projects from 2 bullets to 1 → drop coursework/awards/publications → drop the least relevant project → merge weak Experience bullets → drop the weakest Experience bullet (never below 1 per entry) → ask you. Fonts, margins, and spacing are never touched. Line-fill fixes (a bullet ending in a nearly empty last line) come last.

---

## 7. /cover: cover letters

On request only, after a tailor:

```
/cover                          # the application just tailored in this session
/cover Procter-and-Gamble brand-manager
```

The agent drafts the letter in plain text first, runs the same three choice gates, then writes `cover-letter.tex` and `cover-letter.pdf` into the same folder. Letters use roomier margins than the resume on purpose (the one exception to the spacing lock).

---

## 8. Compiling and checking

The skills compile for you. Every compile runs the checker, which fails the build on: more than one page, preamble or spacing drift, a missing or changed Experience entry, an employer, school, role, or project heading not copied from master, entries out of date order, a number not found in master, bullet caps exceeded, a bullet that is a light rewording of master, duplicate or weak openers, first person, em dashes, semicolons, or colons. For cover letters it also checks fluff words, cliches, and degree tense. **Line-fill is not checked.**

Before submitting, run an ATS plain-text check (needs `pdftotext`):

```bash
pdftotext workspace/applications/<Company>/<Role>/resume.pdf - | less
```

Sections and bullets should read in order, with titles, employers, and dates clean. See [`ats-and-readers.md`](../knowledge/wiki/concepts/ats-and-readers.md) Rule 14.

---

## 9. Updating your master

Edit `workspace/master-resume.tex` directly (new role, new metric, new tool) or re-run `/setup` with an updated resume. Then `/setup` → **Just recompile it** to check it builds. Never fix a fact only in a tailored file: put the truth in master.

**Promoting a tailored bullet back to master:**

```
Take the approved AFTER for Experience > Acme Analytics > bullet 2 from
workspace/applications/<Company>/<Role>/resume-diff.md and apply it to master. Show the diff first.
```

Naming the exact folder is fine. The agent just may not *browse* `applications/` (a hook blocks listing or globbing it).

---

## 10. Maintaining the knowledge base

These run in a Claude Code session opened **in the plugin repo** (they follow the repo's maintainer schema, `.claude/CLAUDE.md`):

- `ingest <source-filename>`: summarizes a new guide from `knowledge/raw/` into the wiki, proposes the changes, and applies them after approval.
- `lint`: checks the wiki for contradictions, stale claims, orphan pages, and untraceable rules.

---

## 11. Troubleshooting

| Problem | What to try |
|---------|-------------|
| `/tailor` says the master is missing or placeholder | Run `/setup` in the same folder |
| Outputs landed in the wrong place | `workspace/` is created in the folder Claude Code started in. Start it from your job-search folder |
| A file got written before you approved | Say: `Follow the rules: diff first, wait for my Gate 3 selection` |
| Agent invents skills or metrics | Say: `Only use evidence in my master, list gaps, don't invent` |
| COMPILE FAIL | Read the log tail it prints. Usually an unescaped `%`, `&`, `$`, `#`, or `_` |
| Constraint violation | The checker names the Hard Constraint and line. Fix the content, never the template |
| `pdflatex` not found, or `latex-packages=MISSING` | See §2. `/setup` names the exact packages to install. On macOS the scripts fall back to `/Library/TeX/texbin/pdflatex` |
| Agent is blocked accessing `applications/` | Working as intended. Name the exact `applications/<Company>/<Role>/` folder |
| **Every** tool call fails with a hook error (plugin development) | A registration points at a missing `hooks/guard_workspace.py`. Fix the path in `hooks/hooks.json` or `.claude/settings.json` from a terminal outside Claude Code, then restart |

---

## Related

- Hard Constraints: [`engine/rules/hard-constraints.md`](../engine/rules/hard-constraints.md)
- Rulebook: [`knowledge/wiki/rulebook.md`](../knowledge/wiki/rulebook.md)
- Wiki catalog: [`knowledge/wiki/index.md`](../knowledge/wiki/index.md)
- Maintainer schema: [`.claude/CLAUDE.md`](../.claude/CLAUDE.md)

*Last updated: 2026-10-04. Matches the plugin layout (`skills/`, `hooks/`, `engine/`, `knowledge/`).*
