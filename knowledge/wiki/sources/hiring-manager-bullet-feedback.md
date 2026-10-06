---
type: source
sources: [hiring-manager-bullet-feedback.md]
last_updated: 2026-10-01
status: stable
---

# Hiring-Manager Bullet Feedback

> **Raw source**: `../../raw/hiring-manager-bullet-feedback.md`
> **Author / origin**: Unknown. Pasted in by the user 2026-09-29, no URL or byline. Written by someone who collected hiring-manager (HM) screening feedback from several startups (devtools-infra, payroll-infra, enterprise-automation, AI-data-platform, fintech-infra) on candidate profiles.
> **Date published / accessed**: Unknown publish date. Ingested 2026-09-29.

## Key highlights

1. A bullet should let the HM **picture you building the same thing for them in month one**.
2. **Four-part bullet anatomy**: Verb (builder, not contributor) + Surface (the specific feature/system/team) + Mechanism (how you built it) + Outcome (what changed). Weak bullets miss two or three parts.
3. **Builder vs operator** is the most repeated HM theme. Operator verbs (maintained, supported, operated, responsible for, contributed to, worked on) get rejected even when the underlying work was building.
4. **Name the surface**: "built the model that predicts claim denials before submission", not "built ML models for healthcare claims".
5. **Add one clause of context** (what the product is, who uses it, scale) when the employer isn't a name the HM knows. For big logos, name the team and its size.
6. **Quantify the right thing**: scale, delta, money, time. Noise numbers are lines of code, meetings, "10+ projects", and naked percentages. Not every bullet needs a number, and never ship one you can't explain.
7. **"AI/ML" is too general.** HMs split candidates into agentic/LLM application engineering (hot), ML training infra (anti-signal at product companies), and RAG/vector plumbing (adjacent, not the thing).
8. **Time stamping and ownership artifacts** (headcount at join, employee #, RFCs, 0→1 systems, promo velocity) matter for senior profiles.

## Unique contributions

- Only source built from **real HM rejection feedback** rather than a single author's opinion. It quotes the reasons verbatim.
- Only source with an explicit **Surface** slot. XYZ ([`bullets.md`](../concepts/bullets.md)) covers outcome, metric, and method, but never demands naming the specific system owned.
- Only source with a **named operator-verb blocklist that includes "contributed to"** (conflicts with `describing-ai-work.md` Cat 7, resolved in [`bullets.md`](../concepts/bullets.md)).
- Only source that calls **ML training infra / feature stores an anti-signal** for agentic product roles, and **RAG alone "adjacent but not the thing"**.
- Only source with a **noise-number blocklist** and a "don't force numbers" stance.
- **Context clause for unknown employers**, which matters most for candidates whose employers aren't household names.
- **Next-question audit**: find the question the reader would ask next and answer it inside the line (what team, what tool, what surface, who used it, what moved).

## Mostly redundant with existing wiki

- Strong action verbs, no "responsible for / worked on" → [`action-verbs.md`](../concepts/action-verbs.md) Rule 1.
- Outcome plus metric → [`bullets.md`](../concepts/bullets.md).
- Judgment framing ("built X because LangChain didn't fit") → [`ai-bullets.md`](../concepts/ai-bullets.md) Rule 1 (criterion 5).
- "Worked on the payments team" as a zero-impact bullet → `resume-as-a-product.md` via [`bullets.md`](../concepts/bullets.md) Rule 25.

## Applicability

- **High**: anatomy, builder verbs, surface naming, context clause, number types, AI-specificity splits.
- **Low**: time stamping (employee #, headcount at join) and ownership artifacts (RFCs, promo velocity). They target senior startup and big-tech profiles, and most masters contain no headcount or employee-number facts. Use them only when master records them or the user supplies them through a Gate 1 clarifier.

## Key claims (with section anchors)

- **§ The anatomy of a bullet point**: Verb + Surface + Mechanism + Outcome. The ledger example shows each part added in turn.
- **§ Explicit ownership**: builder vs operator. "contributor-at-scale doesn't count" (enterprise-automation HM).
- **§ Name the surface**: someone should read the bullet and know exactly which system you'd own at their company.
- **§ Add context**: one clause of product, users, scale for unknown employers. Team and headcount for big logos.
- **§ Quantify the right thing**: scale, delta, money, time. Noise numbers listed. Never put a number on the page you can't talk about.
- **§ Be specific - AI/ML is too general**: agentic vocabulary (harness, tool calling, orchestration loops, evals, multi-agent, prompt caching, fallback chains, p95, cost per request). Training infra is an anti-signal at product companies. RAG is adjacent.
- **§ Time stamping**: headcount at join and growth multiple carry more signal than the logo.
- **§ Ownership artifacts beat titles**: RFCs, 0→1 systems, talks, postmortems, promo velocity. "led various initiatives" names nothing.
- **§ How to rewrite tonight**: next-question audit plus the month-one test.

## Direct quotes worth reusing

- *"contributor-at-scale doesn't count."* (enterprise-automation HM)
- *"led various initiatives" is the most ignorable phrase in tech resumes.*
- *can a hiring manager picture exactly what i'd build for them in month one?*

## Pages this source feeds

- Feeds: [`concepts/bullets.md`](../concepts/bullets.md)
- Also feeds: [`action-verbs.md`](../concepts/action-verbs.md), [`ai-bullets.md`](../concepts/ai-bullets.md), `genai-llm-engineer.md` (retired 2026-10-01), `ml-engineer.md` (retired 2026-10-01), [`rulebook.md`](../rulebook.md)
