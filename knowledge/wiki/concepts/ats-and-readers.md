---
type: concept
sources: [resume-as-a-product.md, ml-engineer-resume-guide.md, ats-friendly-resume-guide.md, how-ats-filters-resumes.md, recruiter-eye-tracking.md, data-science-resume-walkthrough.md]
last_updated: 2026-10-01
status: stable
---

# ATS and the Four Readers

Who reads the resume, in what order, and how the file must be built so each of them finds what they need. Read when a formatting or delivery question comes up, and before shipping (Rules 14-17).

## Rules for the tailoring agent

### The readers

1. **Four readers, in order**: the ATS parses it, a recruiter skims it for about 7 seconds, interviewers mine it for questions, the hiring manager judges fit. A failure at any stage ends the run.
2. **What the ATS really does.** Most setups don't auto-reject on format. They parse the resume into searchable fields that recruiters filter and keyword-search, and knockout questions on the application form are the real auto-filter. Formatting rules exist so titles, employers, dates, and skills parse cleanly. Never promise a trick that "beats the ATS".
3. **The recruiter's 7 seconds** go to six fields: name, current title and employer, current dates, previous title and employer, previous dates, education. Keep them where the template puts them, and put the JD-critical bullet first in each entry. Minimum qualifications must be visible without hunting.
4. **Above the fold** = the top third of the page and the top of each section. JD-critical content goes there.
5. **Interviewers** need bullets that match the team's work, with detail that survives probing and no unexplained red flags. **Hiring managers** need evidence the past work resembles the job, at the right scope, with ownership.
6. **Knockout requirements** (work authorization, licenses, location, minimum years) that master doesn't meet go in the diff's Gaps plainly. The resume can't fix a knockout answer.

### Format

7. **Single column, standard section titles** ("Experience", "Education", "Skills", "Projects"), no symbols or emoji in titles. (Hard Constraint 2)
8. **No images, photos, text boxes, tables, skill bars, or shaded blocks**, and nothing in page headers or footers. No photo also avoids discrimination issues.
9. **Template carve-out.** The master's FontAwesome contact icons and navy section color are approved exceptions (schema decision 2026-07-15): never strip them, never add new icons, images, or colors. (Hard Constraint 2)
10. **Fonts**: whatever the master preamble compiles to under `pdflatex`. Never add `fontspec`, system fonts, or decorative typefaces. Body text never below 10pt. (Hard Constraint 1)
11. **Selectable text.** The preamble's `\input{glyphtounicode}` and `\pdfgentounicode=1` make PDF text extractable. Never remove them. Never build from Photoshop, Canva, or design-tool builders.
12. **No tricks.** White text, hidden keywords, and similar get flagged and rejected. Modern matching is semantic: relevance beats repetition.
13. **PDF by default**, unless the posting asks for `.docx`.

### Before shipping

14. **Plain-text test, every time.** Run `pdftotext -layout` on the final PDF. Fail and fix if a section is missing, characters are garbled, the order is scrambled, or a title, employer, or date doesn't come out on its own line.
15. **Re-run the test after any edit**, however small. (schema rule)
16. **External scanners** (Resume Worded, Jobscan and similar) are hints only. Their keyword suggestions never override truthfulness, and a high score with invented terms is a fail.
17. **Pick the delivery channel.** Human-forward (referral, email to the team): send the PDF. Blind portals (Quick Apply, long web forms): also fill the form fields carefully, since they may be parsed instead of the attachment, and offer a plain standard-font export of the same content if the plain-text test looks shaky. Never abandon the LaTeX pipeline for it.
18. **Don't apply to many unrelated roles at one company.** The ATS shows recruiters every application. Say so if the user mentions it.

## Disagreements

- **Two-column sidebars**: one guide suggests a sidebar to save space while warning elsewhere that columns break parsing, and eye tracking found columns hurt the skim. Resolved: single column (Rule 7).
- **Icons and color**: every source says none. Resolved for this template: keep the master's, add nothing (Rule 9).
- **"Create it in Word or Google Docs"** vs this LaTeX pipeline: resolved by the glyph preamble plus the plain-text test (Rules 11, 14).
