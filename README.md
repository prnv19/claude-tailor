# Resume Tailorer

A **Claude Code plugin** that tailors a one-page, ATS-friendly LaTeX resume (and, on request, a cover letter) to any job description: three commands (`/setup`, `/tailor`, `/cover`), a compiled **knowledge base** of resume-writing rules, and an **engine** that scaffolds, compiles, and mechanically checks every tailored resume. Run `/tailor` with a job description (JD). The agent works out the company and role, proposes a diff against your master resume, asks its questions as multiple-choice gates, and only after you approve writes a tailored `.tex`, a changelog, and a compiled PDF.

It works for any field. Tailoring selects the most relevant content from your own master resume for each JD, so there are no role playbooks to match.

**Full walkthrough:** [docs/guide.md](./docs/guide.md).

---

## Quick start

1. **Install** [Claude Code](https://claude.com/claude-code), Python 3, and a LaTeX distribution: [MacTeX](https://www.tug.org/mactex/) on macOS (`brew install --cask mactex-no-gui`), [TeX Live](https://www.tug.org/texlive/) on Linux, MiKTeX on Windows. `/setup` checks every package the template needs and gives the exact install command for anything missing.
2. **Install the plugin** from inside Claude Code:

   ```
   /plugin marketplace add prnv19/claude-tailor
   /plugin install resume-tailorer@resume-tailorer
   ```

   (From a local clone: `claude --plugin-dir /path/to/claude-tailor`.)
3. **Start Claude Code in a folder for your job search** and build your master from your current resume (pass its path, or save it in that folder and run `/setup` on its own):

   ```bash
   mkdir ~/job-search && cd ~/job-search && claude
   ```

   ```
   /setup ~/Documents/my-resume.pdf
   ```

4. **Tailor:** run `/tailor` and paste the job description, or `/tailor file: <path>` if you saved it in a file. It asks for anything missing (the JD, the company, or the role). Review the diff and answer the three choice gates (clarifiers, gaps, proceed). Nothing is written until you pick **Proceed to tailor**.
5. **Get the PDF** at `workspace/applications/<Company>/<Role>/resume.pdf`. Optionally run `/cover` for a matching letter.

Your data never lives in the plugin. It goes in a `workspace/` folder inside whatever directory you run Claude Code from:

```
~/job-search/workspace/
├── master-resume.tex             ← your master (built by /setup)
├── applications/<Company>/<Role>/    ← resume.tex, resume-diff.md, jd.md, resume.pdf (+ cover-letter.tex/.pdf)
└── build/                        ← pdflatex scratch, safe to delete
```

> **Privacy:** keep `workspace/` out of git (`/setup` offers to add it to `.gitignore`). That also means git does **not** back up your master. Keep your own copy.

---

## Commands

| Command | What it does |
|---------|--------------|
| `/setup [resume file]` | Checks the toolchain, creates `workspace/`, imports your resume (PDF/DOCX/.tex/text) into the master, compiles it |
| `/tailor <JD>` or `/tailor file: <path>` | Takes the pasted JD (or the file you name), derives Company/Role from the JD (asks if missing) → selects from master → diff → choice gates → writes files → compile + check |
| `/cover [Company] [role-slug]` | Cover letter for an existing tailored application (on request only) |

If another plugin or command already uses one of these names, use the namespaced form, e.g. `/resume-tailorer:tailor`.

---

## Hard rules (full list in [`hard-constraints.md`](./engine/rules/hard-constraints.md))

- **One page.** Cut content, never fonts (≥10pt) or margins (≥0.4in) or spacing.
- **Truthful.** Rephrase and reorder only. No invented employers, schools, projects, tools, or metrics: every entry heading and every number must match master byte-for-byte (machine-checked).
- **Diff first, choices not typing.** You see BEFORE → AFTER and answer multiple-choice gates before any file is written.
- **Compose fresh.** Tailored bullets are rewritten from master's facts, not lightly reworded (machine-checked).
- **Layout-strict.** Single column, the master's preamble verbatim, template spacing untouched (machine-checked).
- **Bullet caps.** Internships 1 bullet, other roles 2-3, projects 1 (max 2) (machine-checked).
- **Every experience entry stays**, in reverse-chronological order (machine-checked).
- **No em dashes, semicolons, or colons** as connectors in bullets, diffs, or letters (machine-checked in the `.tex` files).
- **Past applications are write-once.** The agent never browses `workspace/applications/` (hook-enforced).

---

## Prerequisites

| Tool | Required? | Purpose |
|------|-----------|---------|
| [Claude Code](https://claude.com/claude-code) | Yes | Runs the plugin |
| `pdflatex` (MacTeX, TeX Live, or MiKTeX) | Yes, for PDFs | Compiles resumes and letters. The contact icons use `fontawesome7` when installed and fall back to `fontawesome5` |
| Python 3 (standard library only) | Yes | `check_resume.py` and the guard hook |
| `pdftotext` (poppler) | Optional | Overflow line counts and the plain-text ATS check. Without it, the agent reads PDFs directly |

Tested on macOS. The engine scripts are bash, so on Windows Claude Code needs Git Bash (untested).

---

## Repository layout

```
claude-tailor/                the plugin root
├── .claude-plugin/           plugin.json, marketplace.json
├── skills/
│   ├── setup/                /setup: toolchain check, import your resume into the master
│   ├── tailor/               /tailor: JD → diff → choice gates → one-page PDF
│   │   └── references/       sizing.md (content budget), diff-format.md
│   └── cover/                /cover: cover letter for a tailored application
├── hooks/                    guard that blocks browsing past applications
├── engine/
│   ├── rules/                hard-constraints.md: the 12 non-negotiable rules
│   ├── scripts/              workspace.sh, scaffold.sh, compile.sh, check_resume.py
│   └── templates/            master-resume.tex
├── knowledge/                what makes a good resume, no personal data (see knowledge/README.md)
│   ├── raw/                  research notes per source
│   └── wiki/                 rulebook.md, concepts/, sources/, index.md, log.md
├── docs/guide.md             full usage guide
└── .claude/                  maintainer schema (CLAUDE.md) and dev settings, unused by the installed plugin
```

---

## Knowledge base

`knowledge/wiki/rulebook.md` is the compiled rulebook: 10 highlights, then the rules in the order the tailoring workflow uses them, each cited to one of 10 concept pages that cite their sources. The rules are **field-agnostic**: there are no role playbooks. Tailoring scores your master's content against the JD and selects the most relevant (`concepts/content-selection.md`), so it works for any field. The wiki holds **no personal data**: your evidence comes only from your master at tailoring time.

See [`knowledge/wiki/index.md`](./knowledge/wiki/index.md) for the full catalog. `ingest <file>` and `lint` maintain the wiki, in a Claude Code session opened in this repo (see [`.claude/CLAUDE.md`](./.claude/CLAUDE.md)).

---

## Credits and sources

- The LaTeX template's macro layer descends from [Jake's Resume](https://github.com/jakegut/resume) (MIT). The styling and spacing are this project's own.
- `knowledge/raw/` holds research notes on each source (key claims and short quotes), not copies of the articles. Provenance and any full copies stay local in `knowledge/raw/originals/`, which is gitignored.

## License

[MIT](./LICENSE). The template's Jake's Resume notice is included in the same file.
