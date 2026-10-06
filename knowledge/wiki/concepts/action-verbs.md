---
type: concept
sources: [ml-engineer-resume-guide.md, describing-ai-work.md, verb-and-impact-sheets.md, action-verbs-by-skill.md, hiring-manager-bullet-feedback.md, resume-dos-and-donts.md]
last_updated: 2026-10-01
status: stable
---

# Action Verbs

Which verb opens each bullet. Read when picking or deduplicating openers. `check_resume.py` enforces uniqueness and the weak-opener ban (Hard Constraint 4).

## Rules for the tailoring agent

1. **Every bullet opens with a strong action verb.** Never "Responsible for", "Worked on", "Helped with", "Was tasked with", "Assisted in", "Was involved in", or a pronoun. Active voice.
2. **Context first.** Name the bullet's primary action (deploy, automate, negotiate, diagnose, teach, reconcile), then pick the verb that says exactly that. Never a generic synonym chosen only to avoid a repeat, and never `Reduced`/`Improved` by default when the work was building, automating, or instrumenting. (schema practice 2026-05-22)
3. **Unique on the page.** No opening verb repeats across Experience, Projects, and Awards bullets. Coursework lines are exempt. Dedupe only after Rule 2 picks the right verb. (Hard Constraint 4)
4. **Pick from the two inventories.** Technical work: the technical verb list, matching its "use for" context. Everything else (communication, leadership, research, creative, management, organizational, financial): the eight skill-set verb lists. Both lists are in `knowledge/raw/` (`verb-and-impact-sheets.md`, `action-verbs-by-skill.md`). A tactile verb outside both (Rule 6) is fine when it names the action more precisely.
5. **Builder verbs over operator verbs.** When master shows the candidate built, designed, wrote, trained, or shipped something, say so. `Maintained`, `Supported`, `Operated`, `Contributed to` are only for work that truly was upkeep, and then name what was kept running.
6. **Tactile over safe.** Don't reach first for `leveraged`, `utilized`, `developed`, `enhanced`, `streamlined`, `optimized`, `executed`, `implemented`, `spearheaded`, `architected`. They're allowed when accurate (once per page), but tactile verbs that name a real motion (`built`, `rewrote`, `cut`, `debugged`, `migrated`, `scrapped`, `retrained`, `instrumented`, `tuned`, `hardened`) are the default.
7. **Mirror the JD's verb when it's true.** If the JD says "design distributed systems" and the bullet is that work, open with `Designed`.
8. **Vary skill signals.** Across the page, openers should signal the different skills the JD asks for (leadership, analysis, building, communication), not one move repeated.
9. **Never `Helped`, `Assisted`, `Aided`** as openers, even though the leadership verb list includes them.
10. **Tense** follows [`bullets.md`](./bullets.md) Rule 7.

## Quick pick

| Primary action | Verbs |
|---|---|
| Build, ship, deploy | Built, Shipped, Deployed, Launched, Stood up, Wired up |
| Automate, integrate | Automated, Integrated, Scripted, Orchestrated |
| Speed up, cut cost | Cut, Sped up, Compressed, Parallelized, Trimmed |
| Measure, observe | Instrumented, Profiled, Benchmarked, Audited |
| Fix, harden | Debugged, Hardened, Stabilized, Rewrote, Migrated |
| Analyze, research | Analyzed, Investigated, Modeled, Forecasted, Tested |
| Lead, teach | Led, Coached, Mentored, Trained, Facilitated |
| Communicate, persuade | Presented, Authored, Negotiated, Pitched, Briefed |
| Organize, run | Coordinated, Scheduled, Prioritized, Standardized |
| Money | Budgeted, Reconciled, Saved, Raised, Recovered |

**Safe → tactile swaps** (use the right column only when it's true):

| Safe | Tactile |
|---|---|
| Leveraged / Utilized | Used, Adapted, Pulled in |
| Developed / Implemented | Built, Wrote, Stood up, Wired up |
| Enhanced / Optimized | Tightened, Sped up, Tuned, Cut |
| Streamlined | Cut, Merged, Collapsed |
| Spearheaded / Executed | Led, Drove, Ran, Shipped |
| Architected | Designed, Sketched |

## Disagreements

- **Verb list vs anti-detection**: the technical list includes several "safe" verbs (`Utilized`, `Spearheaded`, `Optimized`). Resolved: the list is an allowed inventory, tactile verbs are the default (Rule 6). Mirroring a JD's exact verb once is fine.
- **Which list**: the technical list for technical bullets, the skill-set lists for the rest (Rule 4). The leadership list's `Helped`/`Assisted`/`Aided` are overridden (Rule 9).
- **Operator verbs on the technical list** (`Maintained`, `Supported`): allowed only for genuine upkeep (Rule 5).
