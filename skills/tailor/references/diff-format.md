# resume-diff.md format

Write `resume-diff.md` once, at /tailor step 7, after the final compile passes. Use this structure every time. Hard Constraints 5 and 6 apply to this file too: no em dashes, and no semicolons or colons as connectors. Line labels such as `BEFORE:` are structure, not connectors.

```
## Tailored for <Company>, <Role>
JD source: jd.md (saved verbatim in this folder)

### Keyword map (JD → resume evidence)
- PyTorch → Experience > Acme bullet 2 (kept, promoted to first)
- RAG → Projects > LegalQA bullet 1 (rewritten)
- scikit-learn → GAP, no evidence in master

### Section changes
**Skills**
- BEFORE: Python, R, SQL, Java, ...
- AFTER:  Python, SQL, PyTorch, Transformers, ...
- Why: the JD emphasizes deep learning and LLMs. Demoted Java, added grouping.

**Experience > <Employer> > bullet 3** (illustrative only, not real resume content)
- BEFORE: Worked on customer churn model in Python.
- AFTER:  Built XGBoost churn model on 12M-row dataset, lifting retention-campaign ROI by 18% (A/B tested over 6 weeks).
- Why: XYZ shape with quantified impact, mirroring the JD's "drive measurable business outcomes".

### Dropped
- Experience > X > bullet 5 (weak signal for this JD, freed space for the project rewrite)

### Compile notes (only if something happened)
- First compile spilled 3 lines, so Projects > Y dropped to 1 bullet.
- Experience > Z bullet 1 keeps a short last line after trim and expand attempts both failed (Hard Constraint 10).

### Gaps to discuss with the user (do NOT auto-add)
- "5+ years Kubernetes in production", no matching evidence.
- "Published at NeurIPS/ICML", none on file.
```
