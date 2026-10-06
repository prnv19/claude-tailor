# Sizing: the content budget

Read at /tailor step 3 (sizing the draft) and again if the first compile overflows. The cut order, line-fill rule, and final pass live in `${CLAUDE_PLUGIN_ROOT}/knowledge/wiki/concepts/one-page-discipline.md`.

## Content Budget (draft to fit, don't draft big and then cut)

The one-page limit is a fixed, measured capacity of the template, not something to discover at compile time. Allocate it **before** drafting (/tailor step 3), so the structure decision ("2 projects, no publications, keep MS coursework only") is part of the proposed diff, not five reactive amputations after compiling.

**Page capacity: ~54 rendered text lines** (measured 2026-07-31 by compiling a full master on this template's preamble and counting page-1 lines via `pdftotext`, including the template's normal inter-entry and section spacing. It depends only on the preamble, so it holds for any candidate. Re-checked 2026-10-04 after the icon-font fallback was added: the same content gives identical page-1 line counts under `fontawesome7` and `fontawesome5`.) **Plan to ≤ 52 projected lines.** The 2-line margin absorbs wrap-estimate error. Re-measure only if the preamble ever changes.

**Line costs** (a "line" is one rendered text line, ~114 chars per Hard Constraint 10):

| Element | Lines |
|---|---|
| Header block (name + contact line) | 2 |
| Each `\section` heading | 1 |
| Each `\resumeSubheading` (education / experience entry) | 2 |
| Each `\resumeProjectHeading` | 1 |
| Each bullet | 1–2 (chars ÷ 114, rounded up) |
| Relevant Coursework bullet | 2–3 per school |
| Skills category row (`\textbf{Category}{: ...}`) | 1–2 |
| Each publication | 2–3 |

**How to use it**:

1. During /tailor step 3, sum the planned structure with the table, taking bullet counts from the Hard Constraint 11 caps. Worked example: header 2 + Education with both courseworks 10 + Experience (1 heading + 4 roles × 2 + ~12 bullet-lines from a 3/2/2/1 allocation) 21 + Skills (1 + 5 rows) 6 = **39**, leaving 13 lines for Projects. Spending them: 1 section heading + 3 project headings + ~6 bullet-lines (two projects at 1 bullet, one bumped to 2) = 10, for **49** total, and the ~3 spare lines promote a second project to 2 bullets rather than adding a fourth project. Publications (+8) does not fit, and that trade-off goes in the proposed diff, not in a post-compile scramble.
2. State the projection in the diff (`projected ~51/52 budget lines`) so the user can veto structure choices before any LaTeX is written.
3. **If the first compile still overflows, fix it quantitatively in one pass**, with no cut-one-item-recompile loops. The checker's page error reports how many text lines spilled past page 1 (without `pdftotext`, read page 2 of `workspace/build/<Company>/<Role>/resume.pdf` and count them). Cut at least that many lines' worth of content in a **single batch edit** following the cut order in `one-page-discipline.md` Rule 4, and recompile once to confirm.
4. Line-fill (orphan-tail) fixes still come last, after the page fits, per Hard Constraint 10's sequencing rule.
