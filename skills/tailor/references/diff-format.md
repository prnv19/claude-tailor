# resume-diff.md format

Write `resume-diff.md` once, at /tailor step 7, after the final compile passes. Use this structure every time. Hard Constraints 5 and 6 apply to this file too: no em dashes, and no semicolons or colons as connectors. Line labels such as `BEFORE:` are structure, not connectors.

```
## Tailored for <Company>, <Role>
JD source: jd.md (saved verbatim in this folder)

### Keyword map (JD → resume evidence)
- Salesforce → Experience > Acme bullet 2 (kept, promoted to first)
- vendor negotiation → Experience > Globex bullet 1 (rewritten)
- Tableau → GAP, no evidence in master

### Section changes
**Skills**
- BEFORE: Excel, HubSpot, Salesforce, Canva, ...
- AFTER:  Salesforce, HubSpot, Excel (pivot tables, forecasting), ...
- Why: the JD emphasizes CRM ownership and forecasting. Demoted Canva, added grouping.

**Experience > <Employer> > bullet 3** (illustrative only, not real resume content)
- BEFORE: Responsible for the customer renewal process.
- AFTER:  Redesigned the renewal outreach sequence for 1,200 accounts, lifting on-time renewals from 71% to 86% in two quarters.
- Why: XYZ shape with quantified impact, mirroring the JD's "drive measurable business outcomes".

### Dropped
- Experience > X > bullet 5 (weak signal for this JD, freed space for the project rewrite)

### Compile notes (only if something happened)
- First compile spilled 3 lines, so Projects > Y dropped to 1 bullet.
- Experience > Z bullet 1 keeps a short last line after trim and expand attempts both failed (Hard Constraint 10).

### Gaps to discuss with the user (do NOT auto-add)
- "5+ years managing a P&L", no matching evidence.
- "PMP certification", none on file.
```
