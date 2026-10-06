---
type: source
sources: [ats-friendly-resume-guide.md]
last_updated: 2026-10-01
status: stable
---

# ATS-Friendly Resume Guide

> **Raw source**: `../../raw/ats-friendly-resume-guide.md`
> **Author / origin**: Yangshun (Tech Interview Handbook); clipped from https://www.techinterviewhandbook.org/resume/
> **Date published / accessed**: Published 2026-04-05 (frontmatter); ingested 2026-05-22.

## Key highlights

1. FAANG SWE resume pipeline in four steps: ATS-safe template → substantive content → keyword optimization → validation with free tools.
2. **Format for machines**: create in Word/Google Docs (highlightable text), submit PDF; **Arial, Calibri, or Garamond** at **≥10pt**; **0.5in** margins instead of headers/footers; standard section titles; **no symbols in section headers**.
3. **Never** build resumes in Photoshop, graphic-design tools, or flashy online resume builders — ATS misreads them.
4. **Validate** with plain-text paste test + optional scanners (Resume Worded, targeted-JD tools); fix missing/garbled/scrambled text before applying.
5. **Keywords**: mirror JD language (including spelled-out abbreviations), weight by frequency/importance, distribute across Skills + Experience — no stuffing; one page; fewer strong bullets beat many weak ones.
6. **Application hygiene**: employer portal forms may be the only artifact recruiters see; don't spray unrelated roles at the same company.

## Unique contributions

- Only ingested source with an explicit **safe font whitelist** (Arial / Calibri / Garamond) and **10pt floor** tied to ATS glyph mapping failures on exotic fonts.
- Only source that mandates **highlightable body text** as the ATS precondition (Word/Docs workflow) — maps to LaTeX via `glyphtounicode` + plain-text test for this repo's LaTeX pipeline.
- Explicit **no header/footer** space tactic (use margin reduction to 0.5in) — corroborates schema margin rules.
- **Plain-text file test** procedure (copy PDF content → paste → check missing text, wrong characters, section order).
- **Third-party ATS scanner** names (Resume Worded, AI Resume Judge, Targeted Resume, Resume Shortlister) as optional pre-flight — not in other wiki sources.
- **3–5 JD collate + frequency analyzer** workflow for role-type variants (Online-Utility.org Text Analyzer).
- **ATS placement inference** caveat: some systems estimate years-of-skill from keyword placement/duration context — avoid misleading repetition.
- **Spell-out abbreviations** when mirroring (e.g. `Amazon Web Services` not only `AWS`).
- **Application-form** warning (resume may never be seen) and **multi-application same company** anti-pattern.

## Mostly redundant with existing wiki

- One-page, no photos/icons/columns, keyword mirroring, accomplishment = action + quantified outcome → [`ats-and-readers.md`](../concepts/ats-and-readers.md), [`keywords-and-skills.md`](../concepts/keywords-and-skills.md), [`one-page-discipline.md`](../concepts/one-page-discipline.md), [`bullets.md`](../concepts/bullets.md).
- Professional summary / section ordering / contact block shape → **intentionally not ingested** (those topics are owned by `concepts/structure.md` and `concepts/structure.md`, which synthesize them from other sources).

## Key claims (with section anchors)

- **§ How to set up an ATS-friendly resume**: Top companies use ATS before humans; template must be machine-readable first.
- **§ Only use Microsoft Word or Google Docs**: PDF output preserves formatting; text must be highlightable; commonplace formats parse better; narrow margins 0.5in per side instead of headers/footers.
- **§ Don'ts**: No Photoshop, graphic tools, or online resume builders; no Word header/footer zones.
- **§ Only use standard fonts**: Arial, Calibri, Garamond; exotic fonts → special characters ATS can't read; minimum **10pt** for human readability later.
- **§ Standard headings**: Use conventional section names (`Skills`, `Work Experience`, `Education`, `Projects`); **never add symbols to headers**.
- **§ Optimize — Less is more**: One page; highlight best achievements only; don't list every average win.
- **§ Keyword optimization**: Scan for JD skills/experiences; mirror language in Skills + Experience + Education; spell out abbreviation full forms; tune frequency by JD importance; 3–5 JD collate + frequency tool for generalized variants; no stuffing.
- **§ ATS placement inference**: Frequency and placement may imply years of experience with a skill — be truthful in context.
- **§ Tools**: Resume Worded / AI Resume Judge for readability; Targeted Resume / Resume Shortlister for JD match; **plain text paste test** for missing/garbled/disorganized content.
- **§ Final tips**: Employer application forms may replace resume visibility; don't apply to many disparate roles at one company (recruiter sees all applications).
- **§ Cover letter** (not compiled to agent rules): complement resume, don't duplicate; one page; tailored — retained in source only.

## Direct quotes worth reusing

- *"Submit your resume as a PDF file to preserve formatting, but always create it from Microsoft Word or Google Docs. It is important to ensure that the text in your resume is easily highlightable, which is a precondition for easy parsing."*
- *"New fonts may convert letters into special characters which are not readable by the ATS. Fonts you should use - Arial, Calibri, Garamond."*
- *"Never add symbols to your headers to avoid ATS readability issues."*
- *"Simply copy the content from your resume and paste it into a plain text document!"* (validation procedure)
- *"Do not do keyword stuffing for the sake of it - always remember that the resume will be read by a recruiter or hiring manager eventually."*
- *"If the company requires you to fill in the 'Work Experience' and 'Education' sections into their own form, do not take it lightly! ... it is possible that your resume is never seen."*

## Links into the wiki

- **Also feeds**: [`../concepts/ats-and-readers.md`](../concepts/ats-and-readers.md), [`../concepts/keywords-and-skills.md`](../concepts/keywords-and-skills.md), [`../concepts/one-page-discipline.md`](../concepts/one-page-discipline.md)
