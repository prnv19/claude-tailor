---
type: concept
sources: [xyz-formula.md, ml-engineer-resume-guide.md, hiring-manager-bullet-feedback.md, resume-as-a-product.md, data-science-resume-walkthrough.md, describing-ai-work.md, resume-dos-and-donts.md, verb-and-impact-sheets.md]
last_updated: 2026-10-01
status: stable
---

# Bullets: shape, ownership, numbers

How every Experience and Projects bullet is built. Read when drafting or checking a bullet. Openers have their own page ([`action-verbs.md`](./action-verbs.md)), and AI-work bullets add [`ai-bullets.md`](./ai-bullets.md) on top of this page.

## Rules for the tailoring agent

### Shape

1. **XYZ.** Every bullet carries `Accomplished [X] as measured by [Y] by doing [Z]`: X the outcome, Y the proof, Z the method and tools. The slots may reorder in the sentence (verb first, metric mid, tools last), but all three are present.
2. **Lead with impact, not the task.** Responsibility phrasing ("Responsible for", "Worked on", "Helped with") has no X and no Y: rewrite or drop it.
3. **Frame the problem solved, not the tool used.** Z opens with the problem or user need, then the method.
4. **Name the concrete tools, methods, or materials in Z**: the language, library, instrument, framework, or process actually used, with exact names. Generic phrasing ("using various tools", "a machine learning model") fails both search and interviews. Name the specific algorithm or method where master does.
5. **Four-question pass.** Each bullet answers: what was built, analyzed, or done; with what tools or methods; what metric moved; what business or user value followed (financial when master has it).
6. **Phrases, not sentences.** Open with the verb, no subject, no pronouns, active voice.
7. **Tense.** Present tense for ongoing duties in the current role, past tense for past roles and for completed achievements in the current role.
8. **Interview-defensible.** Every bullet must be interesting enough to discuss and backed by detail the candidate can explain under probing.

### Ownership

9. **Four parts: Verb, Surface, Mechanism, Outcome.** Surface is the specific system, product, process, report, or team the candidate owned. A bullet missing two or more parts gets redrafted. Mechanism = Z, Outcome = X + Y.
10. **Name the surface, never the category.** "Built ML models for energy data", "developed internal tools", "managed projects" fail. Name the specific thing and what it does, from master. The reader should be able to picture what the candidate would own in month one.
11. **Partial ownership names the owned slice** with a builder verb ("Built the <slice> of <system>"), never "Contributed to" and never the whole system. (schema decision 2026-09-29)
12. **No ownership without an object.** "Led various initiatives", "drove multiple projects", "worked across teams" name nothing. Name it or cut it.
13. **Context clause for unfamiliar employers.** On the strongest bullet of an entry whose employer a reader may not know, add one clause on what the product or team is, who uses it, or its scale, from master only. No facts, no clause.
14. **Team size, headcount, employee number, and growth multiples** appear only when the user supplies them (a Gate 1 clarifier), never estimated. (Hard Constraint 3)
15. **Next-question audit.** After drafting, ask what team, what tool, what surface, who used it, what moved. Answer inside the line whatever master can answer. Stop when the rest has no master facts.

### Numbers

16. **Use a real master metric wherever it proves the outcome.** Never invent, never round. Unknown figure: ask. Only a rough order known: write the order the user states ("200K+"). (Hard Constraint 3)
17. **Don't force numbers.** A numberless bullet is fine when surface plus mechanism is strong. This never licenses dropping a strong master metric. (schema decision 2026-09-29)
18. **Every number needs a baseline or object.** Pair a percentage with its starting point, absolute scale, or comparison ("from 5 days to 1 day", "30% ($500k)", "vs a 98% team average"). Answer "is that a big deal?" inside the bullet.
19. **Prefer the numbers that move readers**: money (revenue, cost), user or behavior change, time (latency, turnaround), and scale (users, records, sites). Ranked roughly money > user change > efficiency > internal quality metrics.
20. **No noise numbers**: lines of code, meeting counts, "10+ projects", or a percentage with no object.
21. **Selectivity counts as a number** when there's no natural metric ("one of three engineers chosen to...", "1st of 22 teams"). Awards always carry their denominator.
22. **Not a math problem.** Four or more numbers in one bullet is usually two bullets. Keep it readable.
23. **Defensible numbers only.** If the fact inventory doesn't say how a figure the bullet leans on was measured, flag it in the diff so the user confirms they can explain it.
24. **Figures never migrate.** A number stays attached to its own master claim, even within the same employer. The checker scopes numbers per employer, so it can't catch a move between claims at one job. (schema rule)

### General failure modes

25. **Reject on sight, any bullet**: buzzwords that fit any candidate ("results-driven", "synergy", "leverage"), zero-impact activity ("worked on the payments team"), walls of text, irrelevant filler, and ATS tricks like hidden text.
26. **Skills-only terms stay in Skills.** A tool on master's Skills line with no bullet behind it is never written into a bullet as if it were used there. (schema rule)
27. **Paraphrase, never copy, example sentences** from source material. They are shape references: verb + scope + named tools + quantified outcome in one line.

## Examples

Illustrative only. Every fact must come from master.

- Weak: "Responsible for customer churn models." Strong: "Built a churn model over 12M customer records in Python (XGBoost), lifting retention-campaign ROI 18% in a 6-week A/B test."
- Weak: "Worked on the payments system." Strong: "Built the double-entry ledger all payouts settle through, $40M/month across 2,000 merchants."
- Non-technical: "Rebuilt the night-shift handoff checklist for a 24-bed ICU, cutting missed medication flags from 9 to 2 per month."
- Baseline: "Cut report turnaround from 5 days to 1" beats "Cut report turnaround 80%".
- Overloaded (split it): "Cut p95 from 240ms to 80ms (-66%) on a 12M-DAU service at 4.2B requests/day, saving $84K/yr across 2 regions."

## Disagreements

- **XYZ vs builder anatomy**: compatible. Anatomy adds the Surface slot and a builder-verb test (Rules 9-12).
- **"Contributed to" for partial ownership**: one source recommends it for honesty, hiring-manager feedback calls it an operator verb that gets rejected. Resolved 2026-09-29: name the owned slice (Rule 11).
- **Metric density**: "always quantify" vs "not every bullet has a clean number". Resolved 2026-09-29: keep every real metric that proves the outcome, allow numberless bullets otherwise (Rules 16-17).
