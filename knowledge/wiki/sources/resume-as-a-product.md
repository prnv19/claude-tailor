---
type: source
sources: [resume-as-a-product.md]
last_updated: 2026-10-01
status: stable
---

# Resume as a Product

> **Raw source**: `../../raw/resume-as-a-product.md`
> **Author / origin**: Austen McDonald (ex-Meta Senior EM, Hiring Committee Chair; led team ingesting 2M+ engineers' resumes into Meta's internal ATS). Guest post on System Design One newsletter by Neo Kim.
> **Date published / accessed**: Published 2026-04-15 (frontmatter); ingested 2026-05-22.
> **URL**: https://newsletter.systemdesign.one/p/software-engineer-resume

## Key highlights

1. Treat the resume as a **product / landing page** with **four target users**: ATS (machines) → recruiters/sourcers (5–7s skim) → interviewers → hiring managers.
2. **Strongest opinion**: always include a **2–3 sentence tailored summary** at the top — and never let AI write it.
3. Bullets: **lead with results**, not activities (*"Delivered [business value] using [technology/approach]"*); quantify; put best bullets first within each role; embed tech inside accomplishment bullets (not only Skills).
4. Projects are **marginal** except for new grads or career pivots (e.g. into AI); prioritize paid work vertical space.
5. Tailoring: maintain a **small set of role-type versions** (not per-application); weight repeated JD terms; reorder sections/bullets/skills to match core hiring problem.
6. Formatting: one page; simple PDF; Google Docs upload as parse sanity check; visual hierarchy — but **internally tensions** with two-column sidebar suggestion vs ATS warnings.

## Unique contributions

- Only source so far with explicit **four-audience funnel** and per-audience "what they need" checklist — operationalizes why ATS rules and recruiter skim rules coexist.
- Only source that ran Meta's **resume ingestion pipeline** — high credibility on what breaks ATS parsing (tables, text boxes, creative section titles, icons).
- Only source that says **semantic/AI-powered ATS** goes beyond keyword matching — accomplishments must be substantively relevant, not keyword-stuffed.
- Only source with explicit **anti-AI-summary** warning with concrete bad examples ("results-driven", "passionate", "cross-functional teams").
- Only source with **career-gap / layoff** tactical advice (drop months, delay end-date update, one-liner for failed startups).
- Only source recommending **role-type resume variants** instead of tailoring every single application.

## Key claims (with section anchors)

- **Part 1 intro**: Resume = product; four personas; each extracts overlapping but different information.
- **Machines (ATS)**: Parses into structured data; scores keyword relevance + years + recruiter criteria; modern systems do semantic matching; needs clean parseable formatting; keywords + indexed technologies; creative section titles ("My Journey") risky.
- **Recruiters**: 5–7 second in/out after machine filter; need min quals visible immediately + one exciting signal (brand, relevant project, role tech); brevity; one page unless CEO.
- **Interviewers**: Accomplishments as conversation starters; technical details for defensibility; depth + leadership signals; minimize red flags (short stints, gaps).
- **Hiring Managers**: Finalists only; past work alignment; measurable impact + scope; ownership/growth ("agentic coding" readiness); clear visual hierarchy.
- **§ Contact**: Name, email, phone if wanted; LinkedIn linkified in PDF; GitHub/website only if impressive (deployed repos, good READMEs); US citizenship note if not obvious.
- **§ Write a Summary**: ALWAYS include 2–3 sentence summary at top, tailored to role; shorter = more read; specific product/domain/technical specialty; warn against AI-generated summaries; "cute summary" OK only when resume already obviously matches role.
- **§ Writing Bullets**: Lead with results; quantify scope; bullets become interview topics; leadership signals; best bullets first (not chronological); embed tech in accomplishment bullets.
- **§ Projects**: Marginal unless new grad or career pivot; GitHub only if deployed + documented; side projects show initiative but different environment than job; skip generic descriptions.
- **§ Skills**: "Skill soup" for keyword search; only what you can discuss in depth; don't list trivial skills (HTML example).
- **§ Tailoring**: Role-type versions for big companies; repeated JD terms matter; must-have vs nice-to-have; identify core hiring problem; tactics: adjust summary, reorder sections/bullets, expand/condense roles, match skills.
- **§ Formatting**: One page; margins to 0.5"; one-line old roles; two-column option for sidebar (contact/skills/education) — **conflicts with ATS section**.
- **§ Scannable**: Brand names visible; min quals prominent; recent/flagship experience gets vertical space; gap/layoff tactics.
- **§ Mistakes**: Buzzwords, zero impact, hard-to-read templates, irrelevant info, wall of text; don't include photo (US), hobbies unless relevant, references line, ATS white-text tricks.

## Direct quotes worth reusing

- *"You should treat your resume like a product. Think of it as a landing page for your career."*
- *"After reading [the summary], I should immediately come away with the idea that you'd be a good fit for the role."*
- *"Every line decreases your readership by half."* (attributed to college writing instructor)
- *"Lead with results, not activities... 'Delivered [business value] using [technology/approach].'"*
- *"The accomplishments you list will get asked about. Make them interesting enough to discuss and defensible under scrutiny."*
- *"Mentioning technologies within achievement bullets improves your ranking for those keywords, not just in a separate skills section."*
- *"If 'distributed systems' appears three times, it matters more than 'familiarity with GraphQL,' which only appears once."*
- *"Don't try things like packing your resume with white text to rock the ATS layer."*

## Links into the wiki

- **Feeds**: [`../concepts/ats-and-readers.md`](../concepts/ats-and-readers.md) · [`../concepts/structure.md`](../concepts/structure.md)
- **Updated concepts**: `structure`, `bullets`, `ats-and-readers`, `structure`, `one-page-discipline`, `keywords-and-skills`, `keywords-and-skills`, `ai-bullets`, `voice`
- **Compiled into**: [`../rulebook.md`](../rulebook.md) — new Multi-Audience + Projects sections; summary disagreement resolved

## Claims absorbed inline (no dedicated concept page)

- LinkedIn profile photo/cover photo advice — personal branding, not resume `.tex`.
- Career-site "upload resume to see if you're a fit" iteration hack — optional user tip in diff, not a tailoring rule.
- LLM JD-comparison trick ("top 10 concepts") — cross-referenced in `keywords-and-skills.md` synthesis.
- Iterate 3–4 revisions + human feedback — absorbed into `one-page-discipline.md` Rule 8.

## Internal disagreements (within this source)

| Topic | Section A | Section B |
|-------|-----------|-----------|
| Two-column layout | Part 1 ATS: tables/multi-column break parsing | Part 3 Formatting: suggests two-column for space savings |

**Wiki resolution**: ATS + schema single-column wins for all tailored `.tex` output. Two-column noted only as non-LaTeX alternative.

## Caveats & re-ingest notes

- Source is SWE-general; pair with `data-science-keywords.md` for DS keyword bank and `ats-friendly-resume-guide.md` for fuller ATS mechanics corroboration.
- McDonald's bullet formula is compatible with XYZ — no STAR tension after this ingest.
- Summary "always include" directly conflicts with `ml-engineer-resume-guide.md` — resolved in `structure.md` Disagreements.
