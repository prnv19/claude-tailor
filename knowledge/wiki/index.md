# Resume Tailoring Wiki — Index

Catalog of every page in the wiki. Update on every ingest.

> **Status (2026-10-04)**: 15 raw sources ingested (10 guides + 5 web sources added in the v2 rebuild). The wiki is **candidate-agnostic and field-agnostic**: it holds no personal resume facts and no role playbooks. Per-candidate evidence comes only from `workspace/master-resume.tex` at tailoring time. Open questions (see the rulebook): a summary for experienced candidates, and one vs two pages.

---

## Compiled output

| Page | Purpose |
|------|---------|
| [`rulebook.md`](./rulebook.md) | The v3 tailoring rulebook: 10 highlights, then the rules in workflow order (select → keywords → write → AI → voice → structure → fit → ship → cover letters), each cited `[page n]` to a concept rule |

## Sources (`sources/`)

One summary page per raw note in `../raw/`, same filename, titled by topic. Concept pages don't cite these in their text. Each page's frontmatter `sources:` list is the link. See [`sources/README.md`](./sources/README.md) for the template.

| Source | What it covers | Status |
|--------|----------------|--------|
| [`action-verbs-by-skill`](./sources/action-verbs-by-skill.md) | 247 action verbs in 8 skill-set groups | stable |
| [`ats-friendly-resume-guide`](./sources/ats-friendly-resume-guide.md) | ATS setup, fonts, sections, keyword frequency, plain-text test | stable |
| [`cover-letter-guide`](./sources/cover-letter-guide.md) | Short, pain-point-first cover letters | stable |
| [`data-science-keywords`](./sources/data-science-keywords.md) | Data science keyword groups, a 25-35 term budget | stable |
| [`data-science-resume-walkthrough`](./sources/data-science-resume-walkthrough.md) | Section-by-section resume walkthrough, 4-step bullets, delivery channels | stable |
| [`describing-ai-work`](./sources/describing-ai-work.md) | Describing AI work credibly: 9 failure modes, 5-point audit, AI detectors | stable |
| [`hiring-manager-bullet-feedback`](./sources/hiring-manager-bullet-feedback.md) | Real hiring-manager feedback: builder verbs, naming the surface, the right numbers | stable |
| [`how-ats-filters-resumes`](./sources/how-ats-filters-resumes.md) | What ATS really does: searchable fields, knockout questions | draft |
| [`ml-engineer-resume-guide`](./sources/ml-engineer-resume-guide.md) | Recruiter and coach advice, section-by-section DOs and DON'Ts, a checklist | stable |
| [`page-length-study`](./sources/page-length-study.md) | A hiring simulation favoring two-page resumes (counter-evidence) | draft |
| [`recruiter-eye-tracking`](./sources/recruiter-eye-tracking.md) | The 7-second recruiter skim, six fields, F/E reading pattern | draft |
| [`resume-as-a-product`](./sources/resume-as-a-product.md) | Four readers of a resume, summaries, tailoring, design | stable |
| [`resume-dos-and-donts`](./sources/resume-dos-and-donts.md) | General DOs and DON'Ts for any field | draft |
| [`verb-and-impact-sheets`](./sources/verb-and-impact-sheets.md) | Technical action verbs with usage context, XYZ example patterns | stable |
| [`xyz-formula`](./sources/xyz-formula.md) | The XYZ formula and its baseline step | stable |

## Concepts (`concepts/`)

One page per job the tailoring agent does, each with numbered `## Rules for the tailoring agent` that feed the rulebook. All rules are field-agnostic. Format: [`concepts/README.md`](./concepts/README.md).

| Slug | Job | Status |
|------|-----|--------|
| [`content-selection`](./concepts/content-selection.md) | Score master content against the JD, select, order, cover must-haves (read every tailor) | draft |
| [`bullets`](./concepts/bullets.md) | XYZ shape, Verb-Surface-Mechanism-Outcome ownership, numbers, general failure modes | stable |
| [`action-verbs`](./concepts/action-verbs.md) | Context-first, unique, tactile openers from the xlsx and PDF inventories | stable |
| [`keywords-and-skills`](./concepts/keywords-and-skills.md) | Exact JD terms, budget, abbreviations, the Skills block | stable |
| [`structure`](./concepts/structure.md) | Section order, header, Experience/Education, projects, summary, optional sections | draft |
| [`one-page-discipline`](./concepts/one-page-discipline.md) | One page, cut order, line fill, final pass | stable |
| [`ats-and-readers`](./concepts/ats-and-readers.md) | Four readers, 7-second skim, parse-safe format, plain-text test, delivery channel | stable |
| [`voice`](./concepts/voice.md) | Junior-editor drafting discipline, sounding human, punctuation | stable |
| [`ai-bullets`](./concepts/ai-bullets.md) | 5-point audit, system-level evidence, nine AI failure modes | draft |
| [`cover-letters`](./concepts/cover-letters.md) | `/cover` rules: pain points, hook, template, tense | draft |

---

## Log

See [`log.md`](./log.md) for chronological ingests, lints, and major edits.
