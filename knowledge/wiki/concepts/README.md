# Concepts

One page per job the tailoring agent does, each synthesizing the raw sources into numbered rules. The rulebook (`../rulebook.md`) compiles these into one page, and the agent opens a concept page only when a rule needs its backing detail.

| Page | Job |
|---|---|
| `content-selection.md` | Pick and order master content for the JD (read every tailor) |
| `bullets.md` | Shape, ownership, and numbers in every bullet |
| `action-verbs.md` | Opening verbs |
| `keywords-and-skills.md` | JD vocabulary and the Skills block |
| `structure.md` | Sections, order, summary, projects |
| `one-page-discipline.md` | Length, cut order, line fill, final pass |
| `ats-and-readers.md` | Parsing, the four readers, pre-ship checks |
| `voice.md` | Drafting discipline and sounding human |
| `ai-bullets.md` | Extra checks for AI-work bullets |
| `cover-letters.md` | `/cover` rules |

## Page format

```markdown
---
type: concept
sources: [raw files this page draws from]
last_updated: YYYY-MM-DD
status: stable | draft | needs-review
---

# Title

One or two lines: what the page covers and when to read it.

## Rules for the tailoring agent

### Optional group heading
1. **Short imperative rule.** One to three sentences. (Hard Constraint or cross-page reference only, when needed)

## Examples
A few short, illustrative lines. Facts are never a real candidate's.

## Disagreements
Where sources conflict, and how it was resolved.
```

Conventions:

- Rules come first, because they're what the agent acts on. Number them continuously across group headings so `page.md Rule N` is unique.
- Every rule holds for any field. No role or field playbooks, no job-title keyword lists. Examples may come from one field, but they stay examples.
- No candidate facts, ever.
- One home per rule. If a rule belongs to another page, link it instead of restating it. Hard Constraints live in `engine/rules/hard-constraints.md` and are cited by number.
- No source citations in the text, and no "Synthesis" or "Citations" sections. The frontmatter `sources:` list is the only link back to `raw/`, which `lint` and `ingest` use for tracing. Disagreements describe positions ("one guide says...") without naming sources.
- Keep pages short. A page past about 1,500 words is doing two jobs.
