---
type: compiled-rulebook
version: 3
sources: [ml-engineer-resume-guide.md, data-science-resume-walkthrough.md, describing-ai-work.md, data-science-keywords.md, resume-as-a-product.md, ats-friendly-resume-guide.md, verb-and-impact-sheets.md, action-verbs-by-skill.md, cover-letter-guide.md, hiring-manager-bullet-feedback.md, xyz-formula.md, recruiter-eye-tracking.md, how-ats-filters-resumes.md, page-length-study.md, resume-dos-and-donts.md]
last_updated: 2026-10-01
status: draft
---

# Tailoring Rulebook (v3)

Read on every `/tailor`, after the Hard Constraints. Sections follow the workflow in order. Every rule holds for any field, and the candidate's facts come only from `workspace/master-resume.tex`.

- **Precedence**: Hard Constraints (`engine/rules/hard-constraints.md`, cited `[HC n]`) override this file. This file is compiled from `concepts/`, so edit the concept page and recompile, never this file alone.
- **Citations**: `[page n]` = `concepts/page.md` Rule n. Open a concept page only when a rule here needs its detail or examples.

## Highlights

1. **Truth first.** Rephrase, reorder, re-emphasize master's facts. Never invent an employer, tool, metric, or scope. Missing numbers are asked for, missing skills become gaps. [HC 3] [voice 1-5]
2. **Tailoring is selection.** Score master content against the JD's requirements, keep the most relevant, most relevant first. [content-selection 1-4]
3. **XYZ with a baseline.** Outcome, proof, method, and the number says "of what" and "from what". [bullets 1, 18]
4. **Name the surface, prove ownership.** Builder verb + the specific thing owned + how + what changed. [bullets 9-10]
5. **JD words only where true**, exact casing. Recruiters search parsed fields, so a missing term is invisible, and stuffing earns nothing. [keywords-and-skills 1-3]
6. **Unique, context-fit openers.** [action-verbs 2-3]
7. **One page by cutting content**, never layout. [one-page-discipline 2, 4]
8. **Sound human**: tactile verbs, varied rhythm, no em dashes, semicolons, or colon connectors. [voice 9-13]
9. **Built for the 7-second skim**: titles, employers, dates where the eye expects them, the JD-critical bullet first. [ats-and-readers 3-4]
10. **Ask, don't guess**, always as choice questions at the gates. (`/tailor` skill)

## 1. Select

1. List the JD's must-haves, nice-to-haves, and exact terms. Identify the core hiring problem. [content-selection 1] [keywords-and-skills 5-6]
2. Score every master project, bullet, and skill by how directly it evidences a requirement. Direct with an outcome > related > unrelated. [content-selection 2]
3. Fill the budget from the top score down, within bullet caps. Every Experience entry stays. [content-selection 3] [HC 7, 11]
4. Order bullets within each entry, and projects, by relevance. Entries stay reverse-chronological. [content-selection 4] [HC 7]
5. Every must-have gets evidence or a "Gaps to discuss" entry. Knockout requirements (authorization, license, location, years) master doesn't meet are flagged plainly. [content-selection 5] [ats-and-readers 6]
6. Claim depth only to the evidence. Prefer evidence of real use when two items tie. [content-selection 8-9]
7. Show the selection in the diff: kept, left out, and the requirement each kept item serves. [content-selection 10]

## 2. Keywords and Skills

1. Mirror a JD term only with master evidence, in Skills and in the bullets where it was really used. [keywords-and-skills 2, 7]
2. Exact JD casing, spell out abbreviations the JD spells out, versions as master records them. [keywords-and-skills 3-4, 12]
3. Weight by JD emphasis. About 25-35 matched terms across the page, general and specific paired. Never stuffing, never implied false duration. [keywords-and-skills 5, 8-11]
4. Skills block: the template's `\textbf{Category}{: ...}` rows, categories and items in JD priority, 4-5 lines, irrelevant items dropped. [keywords-and-skills 13-15]
5. Only defensible skills, no baseline filler unless the JD names it, no ratings. Skills-only terms never enter a bullet. [keywords-and-skills 16-19] [bullets 26]

## 3. Write each bullet

1. **Compose fresh from the fact inventory**, never reword master's sentence: new opener, new lead fact, new clause order, numbers byte-for-byte. [HC 12, 3]
2. XYZ, impact first, problem before tool, concrete tools and methods named. [bullets 1-5]
3. Phrases not sentences, active voice, correct tense, interview-defensible. [bullets 6-8]
4. Verb + Surface + Mechanism + Outcome. Name the specific thing, never the category. Partial ownership names the owned slice. No ownership without an object. [bullets 9-12]
5. One context clause for an unfamiliar employer, from master only. Team size and growth figures only when the user supplies them. Run the next-question audit. [bullets 13-15]
6. Real metrics wherever they prove the outcome, never forced, never invented. Every number with a baseline or object. Prefer money, user change, time, scale. No noise numbers. Selectivity counts. At most 3-4 numbers. [bullets 16-22]
7. Flag figures the user may not be able to defend. Figures never migrate between claims. [bullets 23-24]
8. Opener: names the primary action, unique on the page, from the technical or skill-set verb lists, builder over operator, tactile over safe, the JD's verb when true. Never Helped/Assisted/Aided. [action-verbs 1-9]
9. Reject buzzwords, zero-impact activity, walls of text, tricks. [bullets 25]

## 4. AI-work bullets

1. 5-point audit, 3 of 5 minimum: model + version, what the AI did, why it mattered, an outcome, the judgment. [ai-bullets 1]
2. Production-leaning JDs: at least 2 system-level facts (evals, fallbacks, cost, monitoring, guardrails, scale). [ai-bullets 2]
3. Capability claims need a bullet behind them. Adjacent work is never relabeled. [ai-bullets 3]
4. Classify weak AI bullets against the nine failure modes before rewriting. Undersold real work is asked about, never dropped. [ai-bullets 4]

## 5. Voice

1. Substance before drafting. Reframe, never generate. No overgeneralizing, overpolishing, or overclaiming. [voice 1-3]
2. Keep the candidate's voice. Acid test: their work, their words, their numbers. [voice 4-5]
3. Offer framings as choices, and reflect on patterns across master. [voice 6-7]
4. Vary rhythm and phrasing. Structure first, voice last. No interchangeable summary prose. [voice 9-12]
5. No em dashes, semicolons, or colon connectors anywhere in output. Template-syntax colons are the only exception. [voice 13] [HC 5-6]

## 6. Structure

1. Master's section order is the default. Change it only on a JD signal or a career pivot, as a proposed diff change. [structure 1-4]
2. Header: name, contact, location and remote preference. No address, photo, age, labels. GitHub only if it shows real work. [structure 5-8]
3. Experience: paid work, reverse-chronological, flat bullet lists. Old roles may compress to one line. Dates never stretched. [structure 9-11]
4. Education: newest first, GPA only if competitive, coursework only early-career and only when it helps. [structure 12]
5. Projects: load-bearing early-career and on pivots, secondary otherwise. Specific, 1 bullet default, 2 maximum. [structure 13-15] [HC 11]
6. Summary: none by default. Propose only under the stated conditions, through Gate 3. Never fluff words. [structure 16-17]
7. Awards with selectivity, interests only when distinctive, publications only when the JD values research. [structure 18-20]

## 7. Fit the page

1. One page, white space intact, cut content never layout. [one-page-discipline 1-3] [HC 1, 8]
2. Cut order: filler → projects 2→1 bullets → optional lines → least relevant project → merge weak bullets → weakest Experience bullet (floor 1) → ask. [one-page-discipline 4]
3. Fix overflow in one batch, then fix line-fill tails last. [one-page-discipline 5-6] [HC 10]

## 8. Parse and ship

1. Single column, standard titles, no images, tables, bars, or header/footer content. Keep the master's icons and color, add none. [ats-and-readers 7-9] [HC 2]
2. Master fonts only, 10pt minimum, glyph-mapping lines kept, no tricks, PDF by default. [ats-and-readers 10-13]
3. Plain-text test on the final PDF (titles, employers, dates on their own lines), re-run after any edit. Scanners are hints only. [ats-and-readers 14-16]
4. Final pass: proofread both directions. Suggest a second reader on high-stakes applications. [one-page-discipline 7-8]
5. Blind portals: form fields matter, a plain export is the fallback. Don't scatter applications at one company. [ats-and-readers 17-18]

## 9. Cover letters (`/cover` only)

1. On request only, never bundled into a tailor. [cover-letters 1]
2. Read order: `cover-letters.md` → `voice.md` → the target's `resume.tex` + `resume-diff.md` → the JD. [cover-letters 2]
3. Address at least 2 of the JD's top 3 pain points with evidence. Missing 2-3 requirements is fine, and never apologize for gaps. [cover-letters 3, 9]
4. Complement the resume, never restate it. A real company hook or a role-focused fallback, never generic praise. [cover-letters 4, 6]
5. Shape: who + why fit → achievements with numbers → hook → thanks. 200-300 words, one page. [cover-letters 7]
6. Facts only from master or the tailored resume. No fluff words, cliches, em dashes, or semicolons. Read-aloud test. [cover-letters 8, 10]
7. Draft first, approve by selection, then write the `.tex` from the master's preamble with letter margins. [cover-letters 11-12, 15]
8. Degree tense follows the calendar. [cover-letters 13]

## Open questions

- **Summary for experienced candidates**: a hiring-committee chair says always, as 2-3 sentences of prose, and a recruiter says rarely, as two bullets. Default none. (`structure.md` Disagreements)
- **One vs two pages for experienced candidates**: the pipeline stays one page, and a two-page mode is the open design question. (`one-page-discipline.md` Disagreements)

## Regeneration notes

- v3 (2026-10-01): concept pages consolidated from 20 to 10, rules made field-agnostic, the rulebook reordered to follow the workflow. v2 and v1 live in git.
