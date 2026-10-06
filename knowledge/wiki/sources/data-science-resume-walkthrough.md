---
type: source
sources: [data-science-resume-walkthrough.md]
last_updated: 2026-10-01
status: stable
---

# Data Science Resume Walkthrough

> **Raw source**: `../../raw/data-science-resume-walkthrough.md`
> **Author / origin**: Egor Howell — Towards Data Science article; practitioner + career coach (100+ DS/ML resumes reviewed).
> **Date published / accessed**: Published 2025-10-20; ingested 2026-05-22.
> **URL**: https://towardsdatascience.com/this-resume-landed-me-100k-data-science-ml-offers/

## Key highlights

1. Practitioner walkthrough of a resume that landed multiple $100K+ DS/ML offers — section-by-section, not FAANG-recruiter formal like `ml-engineer-resume-guide.md`.
2. **Dual-format strategy**: LaTeX PDF when a human will read it; Google Doc (standard fonts) for blind ATS paths (LinkedIn Quick Apply, Indeed forms).
3. **Skills discipline**: 4–5 lines max; list differentiators (Git, AWS, Databricks), not assumed DS packages (NumPy, Pandas, Matplotlib).
4. **Experience bullet framework** (4 steps): problem modeled → tech/algorithms → metrics improved → business/financial value.
5. **Summary optional** — skip if resume is self-explanatory; never use "passionate / hardworking / determined"; factual 2-sentence pattern when tailoring for ATS.

## Unique contributions

What this source adds that others don't (or state less explicitly):

1. **Application-channel pick** — same content, two delivery formats by funnel type (human-forward vs machine-only). Only source that recommends maintaining a parallel Google Doc for high-ATS-risk applies while keeping LaTeX for recruiter/HM paths.
2. **Assumed-DS-package filter** — for DS roles, omit NumPy/Pandas/Matplotlib from Skills (recruiter assumes them); surface Git, AWS, Argo, Bash, Databricks instead. Conflicts with `data-science-keywords.md` 8-category template — resolved in [`keywords-and-skills.md`](../concepts/keywords-and-skills.md).
3. **Skills line budget** — hard 4–5 line cap (not just "don't list Word").
4. **Proficiency qualifiers** — "proficient" / "familiar with" for languages; LeetCode-easy bar; forbid star ratings and bare "advanced".
5. **Financial impact as ideal metric** — "profit is profit"; companies care about financial benefit over model family.
6. **Named 4-step bullet checklist** — parallel to XYZ but framed as analysis → stack → metric → business value (not attributed to Lazlo Bock).
7. **Activities / extracurricular as first cut** — optional personality section; cut before other sections when space tight.
8. **Course certs generally skip** — unless AWS practitioner-tier or spare space.
9. **Internship vs full-time** labeling and **no sub-bullets** in Experience.

**Mostly redundant with**: `ml-engineer-resume-guide.md`, `resume-as-a-product.md`, `ats-friendly-resume-guide.md`, xlsx Impact Examples (XYZ structure).

**Template note**: Article uses Timmy Chan's DS LaTeX template (CC BY 4.0). This repo uses the **custom master template** in `workspace/master-resume.tex` — lineage only, not a format switch.

## Key claims (with section anchors)

- **§ATS / dual format**: LaTeX PDF can struggle with ATS; Google Doc safer for portals with no human guarantee; PDF fine when recruiter/HM will read. (§The Resume at a glance)
- **§General Principles**: No spelling/grammar errors; 1 page unless 10+ years; consistent fonts; no fancy formatting/graphics/icons; avoid bias fields; bullets not block text; Google Doc fonts Times New Roman / Calibri / Georgia; LaTeX for PDF; tailor every section to JD.
- **§Header**: Name; optional job title; phone, email; city + country; working LinkedIn/GitHub/Kaggle/Medium links.
- **§Summary Statement**: Optional; skip if redundant; good for company/role tailoring and ATS; ban passionate/hardworking/determined; 2-sentence factual who + domain example.
- **§Technical Skills**: 4–5 lines max; high on resume for recruiter scan; don't list too many languages (buzzword suspicion); proficient/familiar with for coding; no star ratings; omit assumed DS packages; list Git, AWS, Argo, Bash, Databricks.
- **§Experience/Projects**: Numbers and figures always; financial impact ideal; technical step + model name + metric + business tie; be explicit on tech for ATS; paid work only (research OK); reverse chronological; label internships vs full-time; no sub-bullets; no experience → Projects with same framing.
- **§Education**: No experience → Education before Work then Projects; 4+ years → simple block; master's in STEM often required; GPA if impressive only; hackathons/projects/awards; skip module lists; skip course certs unless AWS practitioner or space.
- **§Activities / Extracurricular**: Optional; first to cut; personality OK (YouTube, blog) in rare cases.

## Direct quotes worth reusing

- *"That's the baseline of anyone a company wants to hire."* — on passionate/hardworking/determined summary fluff.
- *"Whether you use a neural network or linear regression, it doesn't matter. Profit is profit."* — business framing for ML bullets.
- *"If you feel comfortable answering easy Leetcode problems in that language, then you are proficient."* — proficiency bar for languages.
- *"I assume you are familiar with NumPy, Pandas, and Matplotlib; there is no need to explicitly state this."* — DS skills filter (for DS JDs without explicit JD mention).

## Links into the wiki

- **Also feeds**: [`../concepts/ats-and-readers.md`](../concepts/ats-and-readers.md) · [`../concepts/keywords-and-skills.md`](../concepts/keywords-and-skills.md) · [`../concepts/bullets.md`](../concepts/bullets.md) · [`../concepts/one-page-discipline.md`](../concepts/one-page-discipline.md) · [`../concepts/structure.md`](../concepts/structure.md)
- **Updated roles**: `data-scientist.md` (retired 2026-10-01) · `ml-engineer.md` (retired 2026-10-01) (cross-link only)
- **Compiled into**: [`../rulebook.md`](../rulebook.md) — 8-source regeneration.

## Claims absorbed inline (no dedicated concept page)

- Timmy Chan template / Overleaf reference — informational in source only; the custom master template (`master-resume.tex`) remains the schema template.
- Marketing ATS stats (99% Fortune 500, 75% fail ATS) — not compiled to rules; cite here only.
- Embedded iframe / coaching CTA — ignored.

## Disagreements (source-level index)

| Topic | data-science-resume-walkthrough | Wiki resolution |
|-------|--------|-----------------|
| LaTeX vs ATS | LaTeX risky; use Doc for blind apply | Keep LaTeX default; add channel rule for blind portals |
| Pandas/NumPy in Skills | Omit assumed packages | JD ∩ xlsx ∩ master wins; data-science-resume-walkthrough trim when not in JD |
| Multi-page | 10+ years OK | Pipeline stays 1 page; 10+ years recorded as the two-page threshold |
| Summary | Optional, ATS-useful | Default none; data-science-resume-walkthrough pattern on `diff_first` approval |
