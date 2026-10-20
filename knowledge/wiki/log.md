# Wiki Log

Append-only chronological log of ingests, lints, and major edits. Newest entries go at the bottom.

Each entry MUST start with `## [YYYY-MM-DD] <op> | <name>` so the log is greppable:

```bash
grep "^## \[" log.md | tail -10
grep "^## \[.*\] ingest" log.md
grep "^## \[.*\] lint" log.md
```

Ops: `init` · `ingest` · `lint` · `refactor` · `compile` · `rule` · `note`

---

## History before v2 (condensed)

The wiki was first built inside one person's resume workspace. That full log held personal resume details, so it was condensed to the milestones below when the knowledge base became candidate-agnostic. The original entries are omitted from this repository.

- **2026-05-19 to 2026-05-22**: wiki scaffolded on Karpathy's LLM Wiki pattern; first 8 guides ingested (igotanoffer, ai-resume-survival, resume-as-product, ds-keywords, tih, power-packed xlsx, action-verbs PDF, condensed-template); `genai-llm-engineer` split from `ml-engineer`; post-bootstrap lint.
- **2026-06-14**: rules added: no em dashes, no semicolons in any output.
- **2026-07-06**: Kickresume cover-letter guide ingested; `/cover` skill and `concepts/cover-letters.md` created.
- **2026-07-09 to 2026-07-15**: line-fill discipline (no orphan tails) added; lint: master-template icon/color carve-out, cut order never touches spacing.
- **2026-07-23**: project bullet cap added.
- **2026-07-31**: line-fill diagnostics removed from `check_resume.py` (eyeball the PDF instead).
- **2026-08-02**: `roles/quant-trading-analyst.md` added (no source).
- **2026-09-10 to 2026-09-11**: cover letters exempted from Hard Constraint 8 (standard letter margins); `\parindent{0pt}` fix.
- **2026-09-23 to 2026-09-24**: choice-style question gates; bullet-count caps (Hard Constraint 11); fresh-drafting check (Hard Constraint 12).
- **2026-09-29**: HM feedback source ingested; `concepts/builder-bullet-anatomy.md` created.
- **2026-09-30**: Cursor support removed, `CLAUDE.md` is the only schema.

---

## [2026-10-01] refactor | v2: candidate-agnostic knowledge base + repo restructure

Repo restructured for app development: `Wiki/` → `knowledge/wiki/`, `Reference_Materials/` → `knowledge/raw/`, `rules-extracted.md` → `rulebook.md`. Raw sources renamed to share one slug with their summary page (e.g. `resume_guide.md` → `igotanoffer-mle-guide.md`), and every citation was updated.

Personal content removed everywhere: role-page promotion maps, GAP lists, and master evidence audits were replaced with candidate-agnostic **evidence promotion tiers** that the agent fills from `workspace/master-resume.tex` at tailoring time. The robotics and quant role pages were stripped to generic keyword banks and advice (`needs-review`, no source). Concept pages lost their per-person resolutions ("early-career, so...") in favor of rules conditional on the candidate's career stage. Contact details and resume examples were replaced with placeholders.

Source summaries standardized: numbered **Key highlights** first, then unique contributions, claims, quotes, where the source feeds the wiki, and caveats. Ingest bookkeeping was dropped.

## [2026-10-01] ingest | 5 web sources (research notes)

Captured as notes with URLs and short quotes, not verbatim copies:

- `bock-xyz-formula-2014.md`: primary source of the XYZ formula. Adds the baseline/comparison step → `xyz-bullet-format.md` Rule 17, `quantification.md` Rule 12.
- `ladders-eye-tracking-2018.md`: 7.4 s skim, six fields, F/E pattern → `section-order.md` Rule 21, `multi-audience-framing.md` Rule 11, `ats-rules.md` Rule 23.
- `enhancv-ats-rejection-study-2025.md`: ATS as a searchable database, knockout questions as the real auto-reject → `ats-rules.md` Rule 22, `keyword-mirroring.md` Rule 26, `multi-audience-framing.md` Rule 12, `resume-validation-tools.md` Rule 4.
- `resumego-page-length-2018.md`: two-page preference in a simulation → `one-page-discipline.md` Disagreements (noted, not adopted).
- `harvard-resume-guidance.md`: institutional DOs/DON'Ts → `section-order.md` Rules 3c and 21, `xyz-bullet-format.md` Rule 18, `action-verbs.md` Rule 14, `keyword-mirroring.md` Rule 27.

## [2026-10-01] compile | rulebook v2

`rulebook.md` rewritten: 12 headline rules, then 15 topic sections, each rule cited to its concept page and rule number, plus an explicit Open questions section. Status `draft`.

## [2026-10-01] schema | plugin packaging

The repo became a Claude Code plugin (`/setup`, `/tailor`, `/cover`). The tailoring schema moved out of `CLAUDE.md`: the Hard Constraints now live in `packages/engine/rules/hard-constraints.md`, and the workflow, choice gates, and heuristics in `skills/tailor/` (sizing and diff format under `skills/tailor/references/`). Wiki citations of `CLAUDE.md` were repointed to those files. Rule content is unchanged.

## [2026-10-01] schema | roles retired, field-agnostic selection

`roles/` (six playbooks: ML, GenAI/LLM, DS, analyst, robotics, quant) deleted. Tailoring is now defined as selection: `concepts/content-selection.md` scores master content against the JD, selects and orders it, and covers must-haves or lists gaps, for any field. Field-agnostic rules from the playbooks moved to `content-selection.md`, `ai-bullet-criteria.md` Rules 9-11, and `common-mistakes.md` Rules 17-18. Job-title keyword rows (xlsx Sheet 2) retired as a keyword source (`keyword-mirroring.md` Rules 24-25, `skills-section-design.md` Rule 17): keywords come from JD ∩ master only. Rulebook §14 rewritten, §5 and §7 re-cited.

## [2026-10-01] schema | wiki consolidated for agent context (v3)

Concept pages consolidated from 20 to 10, one per job the agent does: `bullets` (xyz-bullet-format + builder-bullet-anatomy + quantification + general mistakes), `keywords-and-skills` (keyword-mirroring + skills-section-design), `ats-and-readers` (ats-rules + resume-validation-tools + multi-audience-framing), `structure` (section-order + summary-headline + projects-section), `voice` (sounding-human-anti-ai-detection + using-ai-to-write-resume), `ai-bullets` (ai-bullet-criteria + AI failure modes from common-mistakes). `action-verbs` and `one-page-discipline` rewritten in place, `content-selection` and `cover-letters` kept (cover-letters rule numbers unchanged, cited by `check_resume.py` and `/cover`). Pages now lead with rules, drop the prose Synthesis and Citations sections, and state every rule field-agnostically. Concepts went from ~27k to ~8k words. Fixed on the way: a candidate fact in the old Skills page, voice examples that used banned punctuation, a mangled `\textbf`. Rulebook v3 is reordered to the workflow (select → keywords → write → AI → voice → structure → fit → ship) with `[page n]` citations, and the cut order now lives only in `one-page-discipline.md` (the `/tailor` sizing reference points to it). Source summaries' links remapped, stale rule numbers dropped.

## [2026-10-01] schema | raw sources converted to research notes

The eight verbatim clips in `knowledge/raw/` (igotanoffer-mle-guide, ai-resume-survival-guide-2025, resume-as-product-meta-ats, ds-keywords-2026, tih-ats-guide, condensed-template, kickresume-cover-letter-guide, hm-feedback-builder-bullets) were rewritten as research notes: provenance, key claims, short quotes, and the original section anchors the wiki cites. `power-packed-sheets.xlsx` and `action-verbs-list.pdf` became `power-packed-sheets.md` (Sheet 1 verb inventory in full, Sheets 2-4 summarized) and `action-verbs-list.md` (full verb inventory). Full originals moved to `knowledge/raw/originals/`, which is gitignored, so the repo and the plugin no longer ship third-party text. Every committed raw file is now notes. Wiki references updated from `.xlsx`/`.pdf` to the `.md` notes, and `openpyxl` is no longer needed.

## [2026-10-01] schema | files renamed for a consistent layout

Source slugs now follow `<author-or-publisher>-<topic>[-<year>]` in both `raw/` and `wiki/sources/`: condensed-template → howell-ds-ml-resume-walkthrough-2025, tih-ats-guide → tech-interview-handbook-resume-guide-2026, resume-as-product-meta-ats → mcdonald-resume-as-product-2026, igotanoffer-mle-guide → igotanoffer-mle-resume-guide-2025, ai-resume-survival-guide-2025 → nate-ai-resume-survival-guide-2025, ds-keywords-2026 → resumeadapter-ds-keywords-2026. Engine `new-tailored.sh` → `scaffold.sh`, `/tailor` reference `one-page.md` → `sizing.md`. Added `knowledge/README.md`. All citations repointed. Entries above this one keep the old names.

## [2026-10-01] schema | topic titles, no inline source citations

Sources renamed to plain topic titles in `raw/`, `raw/originals/`, and `wiki/sources/` (e.g. `xyz-formula`, `recruiter-eye-tracking`, `describing-ai-work`, `resume-as-a-product`), with matching page titles and a rewritten index table. Concept pages and the rulebook no longer cite sources in their text: `(per ...)` tags were removed (keeping any Hard Constraint or cross-page reference), and Disagreements now describe positions without naming sources. Each page's frontmatter `sources:` list is the only link back. Conventions updated in `CLAUDE.md`, `knowledge/README.md`, `concepts/README.md`, and `sources/README.md`. Older log entries keep the names in use at the time.

## [2026-10-01] schema | attribution removed from raw notes

Raw notes no longer carry citations: frontmatter reduced to a topic title, `type: raw`, and the capture date. URLs, authors, publishers, and original titles were removed, named speakers became roles ("a recruiter"), example-resume pseudonyms and author pronouns were dropped, and wiki cross-references were removed from raw. Provenance for all 15 sources was saved first to `knowledge/raw/originals/PROVENANCE.md` (gitignored, local only). Conventions updated in `CLAUDE.md`, `knowledge/README.md`, and `sources/README.md`.

## [2026-10-04] schema | plugin layout finalized

The repo is now a plain Claude Code plugin rather than a monorepo: `packages/engine/` became `engine/`, and the `apps/web/` placeholder, the restructure write-up, and `workspace/README.md` were deleted (the plugin creates `workspace/` in each user's own folder). The maintainer schema moved from `CLAUDE.md` to `.claude/CLAUDE.md`, because plugins never load a root `CLAUDE.md` and `claude plugin validate` flags one. Wiki references to the Hard Constraints now point at `engine/rules/hard-constraints.md`, the rulebook's open questions describe positions without naming sources, and the index status line no longer lists pages that were merged or deleted. Rule content is unchanged.

## [2026-10-04] schema | checker hardened for any field

Three fictional candidates (an ICU nurse, a lifecycle marketer, a construction project engineer) went through `/setup` and `/tailor`, and the checker was fixed where non-tech resumes broke it. Sections are found by kind, since a "Professional Experience" heading silently skipped every Experience check. Dates parse with full month names, en dashes, MM/YYYY, seasons, and an "Expected" prefix. Ratios and times such as 1:2 aren't colon connectors. A promotion listed twice under one employer shares one number scope, and roles listed with `\resumeSubSubheading` under one employer get their own bullet caps. Punctuation copied unchanged from master warns instead of failing a tailor that can't edit master. Hard Constraint 3 gained a mechanical check that every employer, school, role, and project heading comes from master unchanged, which closes a gap that let an invented employer pass. Hard Constraint 11 counts externships as internships. `/setup` now normalizes section titles and punctuation on import, and Company/Role slugs are limited to letters, digits, and hyphens.
