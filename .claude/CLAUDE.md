# Resume Tailorer: maintainer schema

> Claude Code auto-loads this file in sessions opened in this repo. It covers **developing** the plugin and maintaining the knowledge base. The tailoring workflow itself lives in the plugin's skills, which load only when invoked, so it costs nothing in sessions that don't tailor. This file lives in `.claude/` rather than the repo root because the repo root is the plugin root, where `claude plugin validate` flags a `CLAUDE.md` (plugins never load one).

This repo is a Claude Code plugin (`resume-tailorer`). Users install it and run three commands from their own folder:

| Command | Skill | What it does |
|---|---|---|
| `/setup` | `skills/setup/SKILL.md` | Toolchain check, creates `workspace/`, imports the user's existing resume into `workspace/master-resume.tex` |
| `/tailor <JD>` | `skills/tailor/SKILL.md` | JD → Company/Role slugs → diff → choice gates → tailored `resume.pdf` |
| `/cover` | `skills/cover/SKILL.md` | Cover letter for an existing tailored application |

To tailor in this repo, use `/tailor` like any user (load the plugin with `claude --plugin-dir .`).

## Repository layout

The knowledge base follows Karpathy's LLM Wiki pattern (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): raw sources (layer 1) → compiled wiki (layer 2) → schema (layer 3: the Hard Constraints and the skills).

```
Resume-Tailorer/                  # = the plugin root (CLAUDE_PLUGIN_ROOT when installed)
  .claude-plugin/
    plugin.json                   # plugin manifest
    marketplace.json              # single-plugin marketplace, source "./"
  skills/
    setup/SKILL.md                # /setup
    tailor/SKILL.md               # /tailor: workflow, choice gates, heuristics
    tailor/references/            # sizing.md (content budget), diff-format.md (resume-diff.md layout)
    cover/SKILL.md                # /cover
  hooks/
    hooks.json                    # plugin hook registration (PreToolUse guard)
    guard_workspace.py            # blocks browsing workspace/tailored/ (Hard Constraint 9)
  engine/
    rules/hard-constraints.md     # SCHEMA: the 12 Hard Constraints (overrides the wiki)
    scripts/
      workspace.sh                # status | init | backup | compile-master (/setup and every preflight)
      scaffold.sh                 # scaffold tailored/<Company>/<Role>/resume.tex from master
      compile.sh                  # canonical compile + runs check_resume.py
      check_resume.py             # mechanical Hard Constraint checker
    templates/master-resume.tex   # the LaTeX template with fictional placeholder content
  knowledge/
    raw/                          # RAW SOURCES (layer 1): research notes per source, immutable (raw/originals/ = local full copies, gitignored)
    wiki/                         # COMPILED WIKI (layer 2), agent-maintained
      index.md, log.md, rulebook.md, sources/, concepts/
  docs/guide.md                   # full usage guide
  README.md
  .claude/                        # maintainer config, inert in an installed plugin
    CLAUDE.md                     # this file
    settings.json                 # runs the guard hook for sessions without the plugin loaded
  workspace/                      # the developer's own data when tailoring here (gitignored, created by /setup)
```

**Naming**: docs, wiki pages, and shell scripts are kebab-case. Python is snake_case. Names tools look for keep their names (`README.md`, `CLAUDE.md`, `SKILL.md`, `plugin.json`). Sources are plain topic titles (`<topic>.md`, no author, publisher, or year), identical in `knowledge/raw/` and `knowledge/wiki/sources/`. Engine scripts are named for what they do (`scaffold.sh`, `compile.sh`). See `knowledge/README.md` for the knowledge layout.

## Plugin development rules

1. **One home per rule.** Hard Constraints live only in `engine/rules/hard-constraints.md`. Workflow, gates, and heuristics live only in `skills/tailor/`. Cover-letter procedure only in `skills/cover/SKILL.md`, its rules in `knowledge/wiki/concepts/cover-letters.md`. Never copy a rule into a second file: point to it.
2. **Workspace location.** At runtime the plugin is a read-only copy in the plugin cache. User data is always `<project dir>/workspace/`. Every engine script takes the project dir from `-C <dir>` (the skills pass `${CLAUDE_PROJECT_DIR}`, because Claude's shell may have `cd`'d elsewhere), else `$CLAUDE_PROJECT_DIR`, else the current directory. Scripts must never derive the workspace from their own location, and nothing may write inside `${CLAUDE_PLUGIN_ROOT}`.
3. **Skill paths.** Skills reference bundled files as `${CLAUDE_PLUGIN_ROOT}/...` (repo-wide) or `${CLAUDE_SKILL_DIR}/...` (own folder), and call scripts as `bash "${CLAUDE_PLUGIN_ROOT}/engine/scripts/<name>.sh" -C "${CLAUDE_PROJECT_DIR}" ...` so the `allowed-tools` patterns match. Claude Code substitutes all three variables in both the skill body and `allowed-tools`. Keep each skill's `allowed-tools` in sync with the commands its body tells the agent to run. A `!` preflight command that isn't pre-approved aborts the whole skill outside auto mode. The plugin lives outside the user's folder, where the Read tool asks permission, so a skill that reads bundled files lists `Read(/${CLAUDE_PLUGIN_ROOT}/**)` (the extra `/` makes the substituted path absolute). A `*` inside a quoted path, as in `Bash(cat "${CLAUDE_PLUGIN_ROOT}/*)`, doesn't match (a trailing ` *` after the full script path does), so read bundled files with Read, not `cat`.
4. **Guard hook trap.** `hooks/hooks.json` and `.claude/settings.json` both run `hooks/guard_workspace.py` by path before every Bash/Read/Write/Edit/Glob/Grep call. If that file is missing, Python exits 2, Claude Code treats that as a block, and every tool call (even `!` shell commands) fails until it is fixed from a terminal outside Claude Code. To move or rename it: copy to the new path, update both registrations, then delete the old file.
5. **Test before committing.** `claude plugin validate --strict .`, then exercise changed skills with `claude --plugin-dir .` from a scratch folder (not this repo) so the workspace logic is tested the way users hit it. Bump `version` in `plugin.json` for any user-visible change.
6. **The template preamble is a contract.** `check_resume.py` compares every tailored preamble against the user's master. Changing `templates/master-resume.tex`'s preamble only affects new masters, and invalidates the measured page capacity in `skills/tailor/references/sizing.md` (re-measure it). `LATEX_NEEDS` in `workspace.sh` lists the files the preamble loads, so update it with any package change.
7. **No app code here.** A future web app would call `engine/` with `-C` pointing at each user's folder and read `knowledge/` and `engine/rules/`. It never duplicates their rules.
8. **Privacy.** `workspace/` is gitignored. Never commit resumes, JDs, or PDFs, and never write a candidate's facts into `knowledge/` or a skill.

## Wiki architecture and operations

- `knowledge/raw/` is **immutable** once captured: read from it, never edit its notes. `knowledge/raw/originals/` holds optional full copies, local only.
- `knowledge/wiki/` is **agent-owned**: create, update, and lint pages here.
- **The wiki is candidate-agnostic and field-agnostic.** Never write a candidate's facts (employers, projects, metrics, gap lists) into it, and never add role or field playbooks, job-title keyword lists, or rules that only apply to one field. Tailoring is selecting the most relevant master content for the JD (`concepts/content-selection.md`), which works for any field.

### Page conventions

Every wiki page except `index.md`, `log.md`, and folder `README.md` files starts with YAML frontmatter:

```yaml
---
type: source | concept | compiled-rulebook
sources: [ml-engineer-resume-guide.md, resume-as-a-product.md]   # filenames in knowledge/raw/
last_updated: YYYY-MM-DD
status: stable | draft | needs-review
---
```

- Concept pages MUST contain a `## Rules for the tailoring agent` section with imperative, numbered rules.
- Concept pages and the rulebook do **not** cite sources in their text. The frontmatter `sources:` list is the only link from a page back to `knowledge/raw/`. Schema rules are referenced as Hard Constraint N or the `/tailor` skill.
- Source disagreements go in an explicit `## Disagreements` section, never hidden, describing each position ("one guide says...") without naming the source.
- Filenames are short, human-readable slugs (`bullets.md`, not `concept_001.md`).

### `ingest <source-filename>`

1. Read the source end-to-end, then capture it into `knowledge/raw/<topic>.md` as research notes: a topic title, the capture date, key claims, and short quotes with the original's section anchors. No author, publisher, URL, or names in the note. Record where it came from in `knowledge/raw/originals/PROVENANCE.md`, and keep any full copy in `knowledge/raw/originals/` (both gitignored, never committed or shipped).
2. Propose a diff: the new `sources/<slug>.md` summary page, which `concepts/` pages change, and any new pages.
3. **Wait for user approval** before writing.
4. Apply: write/update pages, update `index.md`, append `## [YYYY-MM-DD] ingest | <filename>` to `log.md` with 1-2 sentences.
5. Recompile `rulebook.md` if any rule-bearing claim changed.

### `lint`

User-triggered health check: contradictions between concept pages, stale claims superseded by newer sources, orphan pages, concepts mentioned across sources without their own page, rulebook rules no longer traceable to a wiki page, and skills or `hard-constraints.md` disagreeing with the wiki. Append `## [YYYY-MM-DD] lint | <summary>` to `log.md`.
