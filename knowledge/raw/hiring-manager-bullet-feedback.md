---
title: "Hiring-Manager Bullet Feedback"
type: raw
captured: 2026-09-29
---
> Research notes: key claims and short quotes, keeping the original's section numbers and headings. Not a copy of the original.

## What the resume answers

- A clear picture of what you did, "for what team, working on what surfaces / features, with what impact and with what tools," so the reader can picture you solving their problem.

## The anatomy of a bullet point

- "A strong bullet has four parts, and most weak ones are missing two or three of them": **Verb** (an active builder or ownership verb, not a contributor verb), **Surface** (the specific team, feature, or system), **Mechanism** (how you built it), **Outcome** (what changed).
- Progression: "worked on the payments system" (nothing) → "built the payments system" (a verb, but the surface is a category) → "built the double-entry ledger" (names what you owned) → + "authored the RFC, shipped v1 solo" (mechanism, proves it was yours) → + "$40m/mo across 2,000 merchants with zero reconciliation breaks" (outcome and scale).
- "Not every bullet has a clean number and that's fine (it probably shouldn't anyways it comes off too try hard)." Readers often don't know the scale or the business, so context matters.

## Explicit ownership

- The most repeated theme across all feedback was builder versus operator: "HMs read your verbs to decide which one you are." Decisions flipped on "built" vs "maintained" for the same profile. One company: "contributor-at-scale doesn't count."
- Operator verbs: maintained, supported, operated, responsible for, contributed to, worked on. Builder verbs: designed, built, authored, shipped, owned. "If your real work was building and your bullets use operator verbs, you're getting rejected for a job you can do."
- Bad: "maintained CI/CD pipelines serving 400 engineers". Good: "designed and built the remote-cache layer for our bazel fleet, cut median build from 11m to 90s."

## Name the surface

- "HMs don't hire 'backend engineers,' they hire the person who built denial prediction or the person who owned the runner scheduler."
- Bad: "built ML models for healthcare claims", "developed internal tools". Good: "built the model that predicts claim denials before submission, cut denial rate 23% across 40 provider groups."
- "Someone should read your bullet and know exactly which system you'd own at their company."

## Add context

- For an employer the HM doesn't recognize, "the surface and the metric both float in a vacuum." Add one clause: what the product is, who uses it, its scale (e.g. a freight marketplace with 3,000 carriers, latency cut from 4s to 800ms).
- "Improved performance by 80%" reads as filler: performance of what, measured how, from what baseline, for whom.
- Big-tech logos have the opposite problem: readers assume you owned a small widget. Name the team, its headcount, and what your corner shipped.

## Quantify the right thing

- Numbers that move HMs: **scale** (400 engineers, 2,000 merchants), **delta** (11m to 90s, denial rate down 23%), **money** (revenue, cost, spend), **time** (p95 12s to 3s, a migration shipped in two weeks).
- Noise: lines of code, meeting counts, "10+ projects", interviews run.
- "Never put a number on the page you can't actually talk about because they will ask."

## Be specific - AI/ML is too general

- "Knowing you have 'AI/ML experience' is not very helpful." An AI-data-platform company rejected strong ML-infra profiles for lacking "actual production agentic systems experience" (harnesses, tool calling, orchestration loops, evals, multi-agent systems, latency/cost/reliability tradeoffs).
- The HM splits: **agentic / LLM application engineering** (what most are hiring for), **ML training infra** ("actively an anti-signal at product companies": training pipelines, feature stores, distributed training), **RAG / vector plumbing** ("adjacent but not the thing").
- "'used LangChain' is a maybe, but 'built X because LangChain didn't fit' is a yes." Strong bullets carry the exact vocabulary plus "evidence it ran in production."

## Time stamping

- One fintech-infra HM: at companies near 10 years old, "only people who joined sub-50 headcount have interesting experience." What matters is whether you were there while it was being built.
- Good: "joined at ~40 people / eng #12, left at 400 ...", "employee #8, owned billing from first invoice to $30M ARR."

## Ownership artifacts beat titles

- For senior and staff candidates: did you own anything, and can you prove it? Accepted proof: RFCs authored, systems started from zero, talks, public postmortems, promotion velocity, being the escalation point.
- "'led various initiatives' is the most ignorable phrase in tech resumes. it claims ownership while naming nothing."

## How to rewrite tonight

- Read your resume for what it leaves out. Find the next question a reader would ask and answer it inside the line ("rebuilt the ingestion pipeline at [co], logistics data for 200 carriers, cut nightly load from 6 hours to 20 minutes").
- Checklist per bullet: what team, what tool, what surface, who used it, what moved.
- Final test: "can a hiring manager picture exactly what i'd build for them in month one?"
