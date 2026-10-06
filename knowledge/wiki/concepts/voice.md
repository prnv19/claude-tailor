---
type: concept
sources: [describing-ai-work.md, resume-as-a-product.md]
last_updated: 2026-10-01
status: stable
---

# Voice: sounding human, drafting honestly

How tailored text should sound, and how the agent should behave while drafting it. Read before drafting any bullet, summary, or cover letter. This page is about the agent's own defaults: smooth, even, predictable prose is exactly what AI detectors and tired recruiters flag.

## Rules for the tailoring agent

### Drafting discipline (the agent is a junior editor, not the author)

1. **Substance before drafting.** If the master fact is thin (no what, no tool, no outcome), ask for the substance before writing. Drafting without it produces generic or inflated bullets.
2. **Reframe the candidate's content, never generate new content.** Generation needs facts only the candidate has.
3. **Avoid the three failure modes**: overgeneralizing (five bullets turned into "drove AI innovation"), overpolishing (the candidate's voice sanded into LinkedIn prose), and overclaiming (an invented number to fill a gap).
4. **Keep the candidate's voice.** Tighten their phrasing, don't replace it. A vivid concrete detail beats a clean abstraction, and a little roughness reads as credible.
5. **Acid test before shipping a line**: would the candidate recognize it as something they did, in words they might use, with numbers they actually have? Any "no" → revise or ask.
6. **Offer alternatives when framing is a real choice** (more technical vs more impact-focused), with a one-line rationale each, through the gates.
7. **Reflect, not only rewrite.** Surface patterns across master that matter for the JD ("12 of 18 bullets are about building, 1 about launching").

### Sounding human

8. **AI detection is a second filter** after the ATS and before the recruiter. ATS-clean isn't enough.
9. **Vary rhythm (burstiness).** Never ship a section where every bullet has the same length and shape (`Verb + tool + outcome` five times). Vary openers, clause order, and length in at least a couple of them.
10. **Avoid predictable phrasing (low perplexity).** Repeated templates and safe verbs (`leveraged`, `utilized`, `enhanced`, `streamlined`) read as machine-written. Prefer tactile verbs ([`action-verbs.md`](./action-verbs.md) Rule 6).
11. **Structure first, voice last.** Never break ATS or bullet-shape rules for voice. Order: ATS-safe → XYZ → human-voiced. (schema rule)
12. **No interchangeable top-of-page prose.** Summaries that could fit anyone ("results-driven", "passionate", "cross-functional teams") are banned.
13. **Punctuation**: no em dashes, no semicolons, no colons as connectors in bullets, `resume-diff.md`, cover letters, application answers, or chat (Hard Constraints 5-6). Use commas, periods, or parentheses.
14. **High-stakes application**: suggest running the final PDF through a detector (GPTZero). If flagged, rework the lowest-scoring section's rhythm and verbs.

## Examples

- Overgeneralized: "Built AI-powered support tooling leveraging cutting-edge LLM capabilities." Right move: ask what model, what the AI did, what changed.
- Overpolished: the candidate wrote "hacked together a prompt that sorts weekly support emails into 6 buckets, wrong about 11% of the time (mostly billing edge cases), cut sorting from 3 hours to 20 minutes". Keep the specifics and the edge-case admission, tighten only.
- Overclaimed: "Built a churn model lifting retention 18%" when master has no 18%. Ask for the real figure instead.
- Rhythm: "Built X with Y, lifting Z." / "Cut Z in half by rewriting X on Y." / "When the old pipeline buckled at 2× load, rebuilt it on Y and held p99 under 80ms."
