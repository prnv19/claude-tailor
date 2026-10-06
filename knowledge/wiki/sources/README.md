# Sources

One summary page per raw source in `../../raw/`. The agent owns these pages and regenerates them whenever the underlying source is re-ingested.

## Filename convention

A raw note and its summary page share one plain topic title: `knowledge/raw/<topic>.md` ↔ `knowledge/wiki/sources/<topic>.md` (e.g. `xyz-formula.md`). No author, publisher, or year in the name. Raw notes carry no attribution either. Provenance (URL, author, dates) is kept locally in `knowledge/raw/originals/PROVENANCE.md`. The catalog is in [`../index.md`](../index.md).

Every committed raw file is research notes: a topic title, the capture date, key claims, and short quotes, with section anchors matching the original. Full copies of third-party text, where kept, live in `knowledge/raw/originals/`, which is gitignored and never shipped.

Concept pages and the rulebook don't cite these pages in their text. A concept page's frontmatter `sources:` list is the only link, used by `lint` and `ingest` for tracing.

## Required structure of each source page

```markdown
---
type: source
sources: [<slug>.<ext>]          # the raw file in knowledge/raw/
last_updated: 2026-10-01
status: stable | draft | needs-review
---

# <Human title> — Source Summary

> **Raw source**: `../../raw/<slug>.<ext>`
> **Author / origin**: ...
> **Date published / accessed**: ...
> **URL**: ...

## Key highlights
1. The 5-10 most actionable takeaways, numbered, highest signal first.

## Unique contributions
What this source adds that others don't. If mostly redundant, say so and link the canonical concept page.

## Key claims (with section anchors)
- Claim (§<section in raw source>)

## Direct quotes worth reusing
Short verbatim quotes.

## Where it feeds the wiki
- Concept pages this source backs, with the rule numbers.

## Disagreements            (only if the source conflicts with others)

## Caveats & re-ingest notes
Vendor bias, sample size, age, what to re-check on re-ingest.
```

## What NOT to put in source pages

- Imperative rules. Those live in `concepts/` pages.
- Verbatim copies of the source. Summarize and cite.
- Cross-source synthesis. That's the job of concept pages.
- Ingest bookkeeping ("touched index.md"). That goes in `../log.md`.
