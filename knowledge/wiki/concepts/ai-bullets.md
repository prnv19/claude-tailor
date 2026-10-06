---
type: concept
sources: [describing-ai-work.md, hiring-manager-bullet-feedback.md]
last_updated: 2026-10-01
status: draft
---

# AI-Work Bullets

Extra checks for any bullet describing AI, LLM, automation, or agent work, in any field (engineering, PM, ops, design, analysis). It sits on top of [`bullets.md`](./bullets.md): that page sets the shape, this one sets the content. Read when a selected bullet touches AI work.

## Rules for the tailoring agent

### The 5-point audit

1. **Every AI bullet is scored on five criteria.** 3 of 5 is acceptable, 4 is strong, below 3 gets rewritten (or the missing facts asked for).
   1. **Model or tool with version** (`GPT-4.1`, `Claude 3.5`, `LangChain`), never just "AI", "LLM", or "chatbot". Use the version master records, never a newer one, even if the JD names it.
   2. **What the AI actually did**: a concrete verb (summarized, classified, extracted, routed, drafted, ranked, retrieved).
   3. **Why it mattered**: the user, product, or business value (time, cost, accuracy, adoption).
   4. **A measurable or observable outcome**, per [`bullets.md`](./bullets.md) Rules 16-24.
   5. **Judgment**: a tradeoff, fallback, iteration, or failure-aware design ("added human handoff on low confidence", "chose X over Y for Z"). The most often missed, the hardest to fake.
2. **System-level evidence** on production-leaning JDs: show at least 2 of evals against a baseline, fallbacks, retries or rate limits, latency or cost, monitoring, guardrails, scale, model choice, eval-driven iteration. Each needs a master fact. An empty box stays empty.
3. **Capability claims need bullet evidence.** "Agents", "fine-tuning", "autonomous workflows" go into a bullet only when a master bullet shows that work. On master's Skills line only: mirror in Skills, raise a Gate 1 clarifier before using it in a bullet. Otherwise it's a gap. Never relabel adjacent work (retrieval is not agents).

### The nine failure modes

4. **Classify weak AI bullets before rewriting.** Each mode maps to a fix.

| Mode | Looks like | Fix |
|---|---|---|
| Vague Observer | "Following trends in GenAI" | Drop from the resume |
| Tool-Dumper | A list of AI tools, nothing built | Name what was built and what changed. Tools go to Skills |
| Inflated Generalist | "Architected an end-to-end AI transformation" for a POC | Scale the language down to the real work |
| Undersold Real Work | "Worked on AI tooling for support" | Never drop. Ask for the workflow, the AI's role, the trust signal |
| Generic Contribution | "Collaborated on LLM integration" | Say what the candidate did, or drop the claim |
| Buzzword Blender | "zero-shot semantic clustering agents" | Read-aloud test with a non-specialist, name the task |
| Over-Owner | "Built the bot that powers all of support" (wrote a few prompts) | Name the owned slice ([`bullets.md`](./bullets.md) Rule 11) |
| Disconnected Win | "Cut onboarding 30% through AI enhancements" | Name what the AI did to cause it |
| Prompt-as-Product | "Launched an intelligent legal assistant" (one prompt, no users) | Call it a prototype, with its iterations |

## Examples

- 5 of 5: "Built a GPT-4.1 + LangChain assistant over 12K HR docs answering Slack policy questions. Added hybrid search and human handoff after a 2-week eval showed 18% confident-but-wrong answers on edge cases. Cut HR inbound 35%."
- 3 of 5: "Built a GPT-4.1 ticket summarizer that auto-fills CRM notes, cutting manual documentation 60%." Missing value context and judgment. Ask whether there was an eval or a fallback.
- 1 of 5: "Used LLMs to improve support workflows." Undersold real work. Ask, don't drop.

## Disagreements

- **"Contributed to" for partial ownership** (Over-Owner fix): resolved in favor of naming the owned slice. See [`bullets.md`](./bullets.md) Disagreements.
