---
type: concept
sources: [ml-engineer-resume-guide.md, resume-as-a-product.md, ats-friendly-resume-guide.md, data-science-resume-walkthrough.md, page-length-study.md, recruiter-eye-tracking.md]
last_updated: 2026-10-01
status: stable
---

# One-Page Discipline

The length rule, the cut order when a draft overflows, line fill, and the final pass. Read when sizing a draft, when a compile overflows, and before delivering. The template's measured line budget lives in `skills/tailor/references/sizing.md`.

## Rules for the tailoring agent

1. **One page, by construction.** `check_resume.py` fails a two-page PDF (Hard Constraint 1). Every source agrees for early-career candidates. Two pages become defensible only around 10+ years of experience, which this pipeline doesn't support yet.
2. **Cut content, never layout.** Fonts stay at or above 10pt, and margins and template spacing are never touched to make room (Hard Constraint 8). A page that fits only because it was squeezed fails the "white space to breathe" bar.
3. **Few strong over many average.** When something has to go, cut the weakest content first.
4. **Cut order** when a draft overflows, each step before the next:
   1. Trim filler ("successfully", "various", "multiple", "several").
   2. Demote projects from 2 bullets to 1, least JD-relevant first.
   3. Drop optional lines: activities, relevant coursework, generic awards, course certificates, publications the JD doesn't value.
   4. Drop the least JD-relevant project.
   5. Merge two weak Experience bullets into one stronger one.
   6. Drop the weakest Experience bullet in the longest role, never below 1 bullet per entry (Hard Constraint 11).
   7. Still over: ask the user what to cut.
   (schema rule; Projects yield before paid Experience per [`structure.md`](./structure.md) Rule 13)
5. **Fix overflow in one batch.** Count the spilled lines on page 2, cut at least that much in a single edit following Rule 4, recompile once. No cut-one-thing-recompile loops. (schema rule)
6. **Line fill comes last.** After the page fits, no Experience or Projects bullet may end in a last line holding only 2-5 words. Trim back to the previous line or expand with real master specifics (tools, scale, metric) until the last line is at least ~40% full. Aim for bullets of about 1.0 or 1.7-2.0 rendered lines (~114 characters per line). Ship a tail only after both attempts fail, and note it in `resume-diff.md`. Not machine-checked: read the PDF. (Hard Constraint 10)
7. **Final pass before delivering**: proofread top to bottom, then bottom to top, run the plain-text test ([`ats-and-readers.md`](./ats-and-readers.md) Rule 14), and re-check after any later edit.
8. **Suggest a second reader** (a recruiter, a peer) for high-stakes applications, and expect a few revision rounds. After interviews, cut or rework bullets that went badly and promote ones that landed.

## Disagreements

- **Two pages preferred?** One hiring simulation (482 people) found recruiters chose two-page resumes 2.3× as often. Noted, not adopted: a single vendor-run study whose two-page versions also had more content. The eye-tracking skim data and every guide favor one page early in a career. It's the strongest case for a future optional two-page mode for experienced candidates.
- **Senior threshold**: "one page unless you're a CEO" vs two pages after 10+ years. Recorded as 10+ years. The pipeline stays one page either way.
