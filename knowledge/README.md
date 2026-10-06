# knowledge/

What the tailoring agent knows about writing resumes. It's built in three layers, after Karpathy's LLM Wiki pattern, and holds no candidate data.

```
raw/                  1. Sources: research notes on each guide or study (immutable)
  originals/             full copies and PROVENANCE.md (where each source came from), local only (gitignored)
wiki/                 2. Compiled knowledge (agent-maintained)
  sources/               one summary page per raw source, same filename
  concepts/              one page of numbered rules per job (bullets, keywords, structure, ...)
  rulebook.md            all concept rules compiled into one page, in workflow order
  index.md               catalog of every page
  log.md                 append-only history of ingests, lints, and schema changes
```

Layer 3, the schema, lives outside this folder: `engine/rules/hard-constraints.md` and the skills in `skills/`.

## How it's read

- `/tailor` reads `wiki/rulebook.md` and `wiki/concepts/content-selection.md` every time, and a single concept rule on demand via the rulebook's `[page n]` citations.
- `/cover` reads `wiki/concepts/cover-letters.md` and `wiki/concepts/voice.md`.
- `raw/` is read only when a wiki page has a gap, and by `ingest` and `lint`.

## Naming

- Sources: a plain topic title, `<topic>.md` (e.g. `xyz-formula.md`, `recruiter-eye-tracking.md`), identical in `raw/` and `wiki/sources/`. No author, publisher, or year in the name, and none inside the raw notes either. Provenance (URLs, authors, dates) is kept locally in `raw/originals/PROVENANCE.md`.
- Concept pages and the rulebook don't cite sources in their text. Each page's frontmatter `sources:` list is the only link back.
- Concepts: a short slug for the job the page covers (e.g. `bullets.md`, `keywords-and-skills.md`).

## Changing it

Add sources with `ingest`, health-check with `lint`. Both are defined in the repo's maintainer schema (`.claude/CLAUDE.md`) and run in a session opened in this repo. Edit a concept page, never the rulebook alone, then recompile the rulebook.
