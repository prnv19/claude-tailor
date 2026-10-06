---
type: source
sources: [action-verbs-by-skill.md]
last_updated: 2026-10-01
status: stable
---

# Action Verbs by Skill

> **Raw source**: `../../raw/action-verbs-by-skill.md`
> **Author / origin**: Unknown career-center / university handout (single-page reference sheet; no author or URL on page)
> **Date published / accessed**: In workspace 2026-05-22; ingested 2026-05-22.
> **Extraction note**: PDF is **image-only** (embedded 1120×1359 PNG). `pypdf` text extraction returns only the title line. Verb inventory below transcribed from the rendered page image.

## Key highlights

1. One-page handout: **ACTION VERBS: ORGANIZED BY SKILL SET** — eight boxed categories, two columns of verbs each.
2. **247 unique verbs** total (duplicates across boxes count once); organized by **soft-skill domain**, not tech stack context.
3. **52 verbs overlap** with `verb-and-impact-sheets.md` Sheet 1 (97 unique); **45 tech verbs are xlsx-only**; **195 are PDF-only**.
4. Footer callout: *"Use a variety of action verbs in your resume to effectively describe your skills and experiences."*
5. **Complements** xlsx — does **not** replace it for DS/ML/MLOps tailoring. Use PDF when JD stresses communication, leadership, research rigor, or program management.

## Unique contributions

- Only raw source with verbs grouped by **Communication / Leadership / Research / Creative / Management / Organizational / Financial / Technical** — maps to recruiter skill buckets (especially leadership- and stakeholder-heavy JDs).
- Broadest verb inventory in `knowledge/raw/` (~2.5× xlsx count) — useful when diversifying openers across non-technical bullets on the same page.
- **Technical** box is generic SWE/handyman verbs (`Built`, `Programmed`, `Utilized`) — **not** ML-production vocabulary (`Deployed`, `Dockerized`, `Trained`). Confirms xlsx as tech canonical.
- Overlaps `describing-ai-work.md` tension: PDF lists `Utilized` (Technical), `Helped`/`Assisted`/`Aided` (Leadership), `Developed`/`Enhanced`/`Streamlined`/`Executed`/`Implemented` (Management/Creative) — same "safe" set Nate warns against.

## Verb inventory by skill set

Verbs listed alphabetically within each box (as on the PDF). Cross-box duplicates (e.g. `Developed`, `Influenced`) appear in multiple boxes on the sheet — wiki treats each as **one verb** for dedupe (see [`action-verbs.md`](../concepts/action-verbs.md) Rule 3).

### Communication (44)

Addressed, Advertised, Arbitrated, Articulated, Authored, Collaborated, Communicated, Condensed, Conferred, Consulted, Contacted, Conveyed, Convinced, Corresponded, Debated, Elicited, Enlisted, Formulated, Furnished, Influenced, Informed, Interacted, Interpreted, Marketed, Mediated, Moderated, Negotiated, Outlined, Participated, Persuaded, Presented, Promoted, Proposed, Publicized, Recruited, Referred, Reinforced, Resolved, Responded, Solicited, Specified, Suggested, Synthesized

### Leadership / Mentoring (29)

Advanced, Advocated, Aided, Assisted, Coached, Contributed, Cooperated, Counseled, Demonstrated, Educated, Encouraged, Facilitated, Familiarized, Furthered, Guided, Helped, Influenced, Instructed, Intervened, Launched, Motivated, Provided, Represented, Staffed, Supplied, Supported, Trained, Volunteered

### Research (26)

Assessed, Benchmarked, Compared, Conducted, Critiqued, Detected, Determined, Diagnosed, Evaluated, Examined, Experimented, Explored, Extracted, Gathered, Identified, Inspected, Invented, Investigated, Located, Measured, Researched, Solved, Summarized, Surveyed, Tested

### Creative (26)

Combined, Composed, Conceptualized, Condensed, Created, Customized, Designed, Developed, Directed, Displayed, Established, Founded, Illustrated, Integrated, Introduced, Modeled, Modified, Originated, Performed, Planned, Published, Revised, Revitalized, Shaped

### Management (72)

Accelerated, Accomplished, Achieved, Administered, Affected, Appointed, Approved, Assigned, Attained, Authorized, Bolstered, Broadened, Chaired, Completed, Conducted, Considered, Consolidated, Controlled, Converted, Coordinated, Decided, Delegated, Developed, Directed, Eliminated, Emphasized, Enforced, Enhanced, Established, Exceeded, Executed, Expanded, Expedited, Generated, Handled, Headed, Hired, Implemented, Improved, Incorporated, Increased, Initiated, Instituted, Launched, Led, Managed, Mastered, Merged, Navigated, Originated, Overhauled, Oversaw, Pinpointed, Presided, Prioritized, Produced, Recommended, Reorganized, Replaced, Restored, Reviewed, Satisfied, Saved, Secured, Selected, Started, Streamlined, Strengthened, Supervised, Sustained, Used, Won

### Organizational (25)

Arranged, Catalogued, Categorized, Charted, Classified, Collected, Compiled, Devised, Distributed, Formed, Located, Maintained, Monitored, Obtained, Operated, Organized, Processed, Scheduled, Structured, Submitted, Supplied, Systematized, Transformed, Updated, Validated, Verified

### Financial (22)

Adjusted, Allocated, Analyzed, Appraised, Assessed, Audited, Balanced, Budgeted, Calculated, Computed, Conserved, Corrected, Estimated, Evaluated, Forecasted, Planned, Prepared, Projected, Proved, Qualified, Reconciled, Reduced

### Technical (26)

Adapted, Applied, Assembled, Built, Conserved, Constructed, Converted, Designed, Determined, Engineered, Fabricated, Fortified, Installed, Maintained, Operated, Programmed, Rectified, Regulated, Remodeled, Repaired, Revamped, Specialized, Standardized, Studied, Upgraded, Utilized

## Overlap with xlsx Sheet 1 (Action Verbs)

| Set | Unique count | Tailoring role |
|-----|--------------|----------------|
| xlsx Sheet 1 | 97 | **Canonical** for tech/DS/ML bullets — verb + "Context for Tech Roles" |
| PDF (all boxes) | 247 | **Secondary** for soft-skill / leadership / stakeholder bullets |
| Intersection | 52 | Shared pool — e.g. Analyzed, Built, Developed, Evaluated, Led, Managed, Researched, Streamlined, Validated |
| xlsx-only | 45 | Production/ML/infra — Deployed, Dockerized, Trained, Scaled, Hardened, Automated, … |
| PDF-only | 195 | Communication, management, financial, general research — Negotiated, Facilitated, Budgeted, … |

**DS/ML-relevant intersection sample** (usable from either source): Analyzed, Built, Conducted, Coordinated, Developed, Engineered, Evaluated, Executed, Identified, Implemented, Improved, Increased, Integrated, Investigated, Led, Managed, Measured, Optimized, Produced, Programmed, Reduced, Researched, Streamlined, Tested, Validated, Visualized (Visualized is xlsx-only; listed for DS fit).

## Key claims

- Organize verb choice by **skill set** the bullet is meant to signal, not only by tech stack. (PDF structure)
- **Variety** across verbs strengthens resume readability. (footer callout)
- **Technical** verbs on this sheet are entry-level/generic — insufficient alone for MLE/DS ATS keyword matching. (cross-check vs xlsx + `ml-engineer-resume-guide.md` §5.4.2 stack-in-Z rule)

## Direct quotes worth reusing

> Use a variety of action verbs in your resume to effectively describe your skills and experiences.

(footer callout — paraphrase in tailoring notes, not as a resume bullet)

## Links into the wiki

- **Also feeds**: [`../concepts/action-verbs.md`](../concepts/action-verbs.md) (Rules 4, 8-9, Disagreements)
- **Compiled**: [`../rulebook.md`](../rulebook.md) (Bullet Writing rules 17–18)

## Disagreements with other sources

| Topic | PDF | Wiki resolution |
|-------|-----|-----------------|
| Tech bullet openers | Technical box + overlap | **xlsx Sheet 1 wins** — context column required |
| Weak openers | `Helped`, `Assisted`, `Aided`, `Used` | **Forbidden** per `ml-engineer-resume-guide.md` — do not use PDF Leadership verbs as excuse |
| Safe AI-tone verbs | `Utilized`, `Developed`, `Enhanced`, `Streamlined`, `Executed`, `Implemented` | **Allowed when accurate**, tactile preferred — same as xlsx vs `describing-ai-work.md` |
| Verb dedupe | Same verb in multiple PDF boxes | One use per page — same rule as xlsx duplicate rows |

## Claims absorbed inline (no dedicated page)

- PDF does not warrant a separate `soft-skills-verbs.md` concept — folded into [`action-verbs.md`](../concepts/action-verbs.md).
- No role-page updates — leadership/communication promotion already covered in MLE skill-scan Rule 3.
