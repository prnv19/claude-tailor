# engine

The resume engine: the Hard Constraints, the LaTeX template, and the scripts that scaffold, compile, and mechanically check every tailored resume and cover letter. The plugin's skills (`/setup`, `/tailor`, `/cover`) call it. Python is standard library only. The shell scripts need `pdflatex`.

## Scripts

Every script takes an optional `-C <project-dir>` first, like `git -C`: the folder that holds `workspace/`. Without it, the project dir is `$CLAUDE_PROJECT_DIR`, else the current directory. The skills always pass `-C`, because Claude's shell may have `cd`'d elsewhere. Scripts never locate the workspace relative to themselves, because in an installed plugin they run from the read-only plugin cache. A future web app would call the same scripts with `-C` pointing at each user's folder.

| Script | What it does |
|--------|--------------|
| `scripts/workspace.sh status` | Prints toolchain and workspace state as `key=value` lines, injected into each skill's preflight: `workspace`, `python3`, `pdflatex`, `latex-packages` (the TeX Live names of any missing packages), `pdftotext`, `master` (`ok`, `placeholder`, or `MISSING`), `gitignore`, `today`. Always exits 0 |
| `scripts/workspace.sh init` | Creates `workspace/tailored/` and `workspace/build/` and copies the template in as the master. Never overwrites a master |
| `scripts/workspace.sh backup` | Copies the master to `workspace/master-resume.backup-<date>.tex`, never overwriting an earlier backup |
| `scripts/workspace.sh compile-master` | Compiles the master into `workspace/build/_master/` and reports its page count. Only a LaTeX error fails it |
| `scripts/scaffold.sh <Company> <Role>` | Copies `workspace/master-resume.tex` to `workspace/tailored/<Company>/<Role>/resume.tex`. Refuses to overwrite |
| `scripts/compile.sh <Company> <Role> [tex ...]` | Compiles `resume.tex` (and `cover-letter.tex` if present) into `workspace/build/<Company>/<Role>/`, copies the PDFs next to their sources, then runs the checker. Non-zero exit on any failure |
| `scripts/check_resume.py <Company> <Role> [--build-dir DIR]` | Mechanical Hard Constraint checks against the master: one page (counting the lines that spilled past it when `pdftotext` is installed), preamble and spacing fidelity, Experience entries unchanged and reverse-chronological, every entry heading copied from master, numeric fidelity, bullet caps, fresh drafting, unique and strong openers, punctuation bans. For cover letters: fluff words, cliches, and degree tense (derived from master's Education dates) |

## Rules

`rules/hard-constraints.md` is the single home of the 12 Hard Constraints. `check_resume.py` enforces the mechanical ones, and the skills load the file.

## Template

`templates/master-resume.tex` is the LaTeX template: the custom preamble and macros, filled with fictional placeholder content. `/setup` copies it to `workspace/master-resume.tex` and replaces the content. The preamble must stay byte-compatible, because the checker compares every tailored preamble against the master's. Contact icons use Font Awesome 7 where it's installed and fall back to Font Awesome 5.

The checker's thresholds (bullet caps, the fresh-drafting similarity limits) are constants at the top of `check_resume.py`, mirroring Hard Constraints 11-12.
