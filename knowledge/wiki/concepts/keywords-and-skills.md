---
type: concept
sources: [ml-engineer-resume-guide.md, resume-as-a-product.md, ats-friendly-resume-guide.md, data-science-keywords.md, data-science-resume-walkthrough.md, how-ats-filters-resumes.md, resume-dos-and-donts.md, describing-ai-work.md]
last_updated: 2026-10-01
status: stable
---

# Keywords and the Skills Section

How JD vocabulary reaches the page, truthfully, and how the Skills block is built. Read when choosing terms or drafting Skills. Selection itself is [`content-selection.md`](./content-selection.md).

## Rules for the tailoring agent

### Keywords

1. **Why exact terms matter.** Recruiters keyword- and Boolean-search parsed ATS fields. A resume missing the JD's exact term never comes up in that search. That's the cost of a missed keyword, not an auto-reject score, and it's why stuffing earns nothing: a human reads what search returns.
2. **Mirror only where master supports it.** A JD term goes into Skills, and into the bullets where it was actually used, only with master evidence. Everything else is a gap. (Hard Constraint 3)
3. **Exact casing and spelling from the JD** (`PyTorch`, `SageMaker`, `GAAP`, `Salesforce`). When sources disagree on casing, the JD wins. (schema rule)
4. **Spell out abbreviations the JD spells out**, or pair both forms once ("AWS (Amazon Web Services)"). Use an abbreviation alone only when it's industry-standard.
5. **Weight by JD emphasis.** A term repeated across the JD outranks a one-off mention, and must-haves outrank filler like "strong communication skills". Spend Skills order and bullet rewrites accordingly.
6. **Mirror the core hiring problem.** "Own the data pipeline" → reliability and ownership evidence. "Scale to 10× users" → performance evidence.
7. **Keywords live in bullets too**, not only Skills. Bullets carry more weight with humans, and Skills alone reads as a list.
8. **Budget about 25-35 JD-matched, evidence-backed terms** across Skills, bullets, and Projects, fewer for JDs that name few tools. Never a 60-term dump. (DR)
9. **Pair general and specific** in one line where both are true ("forecasting models in Python (Prophet)"), never the general term alone.
10. **No stuffing, no buzzword piles.** A bullet naming seven tools to game search reads as noise.
11. **Don't imply false duration.** Some ATS estimate years of a skill from frequency and placement, so don't repeat a term in ways that overstate experience (a 3-month internship isn't years of it).
12. **Model and tool versions as master records them** (`GPT-4.1`, not "GPT"). See [`ai-bullets.md`](./ai-bullets.md).

### Skills block

13. **Template shape.** One `itemize` with `\textbf{Category}{: ...}` rows, the master's pattern. Never tables, columns, bars, or ratings. (template)
14. **Categories follow the JD.** Group into the categories the JD stresses, most important first, items within each ordered by JD priority. Drop categories and items the JD doesn't care about.
15. **4-5 rendered lines.** The master's Skills block is a warehouse to select from, never copied wholesale. Over budget: drop the lowest-priority items, never shrink the font.
16. **Defensible only.** List only what the candidate can discuss in depth, ideally backed by a bullet. No long language laundry lists.
17. **No baseline filler.** Omit tools every applicant to this JD is assumed to have (word processors, NumPy for a data science JD) unless the JD names them. Advanced scope may earn a place ("Excel (Power Query, VBA)").
18. **Method and practice families** the JD names (NLP, Time Series, Agile, GAAP) get a visible place in Skills when master supports them.
19. **No proficiency ratings.** No stars, no bare "expert". For languages only, "proficient in" / "familiar with" may set honest expectations. Tools stay bare and exact-cased.

## Examples

- JD: "PyTorch, distributed training, Hugging Face". Master: PyTorch fine-tuning only. Skills: `PyTorch, Hugging Face Transformers`. "Distributed training" goes to Gaps.
- JD names 8 tools, master supports 1: Skills lists the 1. The other 7 are gaps, not Skills entries.
- Skills for an accounting JD: `\textbf{Accounting}{: GAAP, month-end close, reconciliations} \\ \textbf{Systems}{: NetSuite, Excel (Power Query)}`.

## Disagreements

- **Keyword count**: one source gives 25-35, the others only say "don't stuff". Compatible: the budget counts only JD-matched, evidence-backed terms (Rule 8).
- **Baseline packages**: one source lists them, another says to omit them. Resolved: the JD decides (Rule 17).
- **Summary with keywords**: one source suggests a keyword summary. The default stays no summary ([`structure.md`](./structure.md)).
