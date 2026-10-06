---
type: source
sources: [verb-and-impact-sheets.md]
last_updated: 2026-10-01
status: stable
---

# Verb and Impact Sheets

> **Raw source**: `../../raw/verb-and-impact-sheets.md`
> **Author / origin**: Unknown (spreadsheet workbook; four structured sheets)
> **Date published / accessed**: In workspace 2026-05-22; ingested 2026-05-22.

## Key highlights

1. Four lookup sheets: **Action Verbs** (103), **ATS Tech Stack Keywords** (85 position titles), **Accomplishment Examples** (99), **Impact Examples** (99 strict XYZ templates).
2. Sheet 1 is the **canonical verb picker** — every tailored bullet opener should map to a verb + matching "Context for Tech Roles" column.
3. Sheet 2 is **Position Title → comma-separated keyword row** — use only when keyword appears in **both** the JD and the candidate's master; intersect with [`data-science-keywords.md`](./data-science-keywords.md) DS bank (data-science-keywords is the superset for DS).
4. Sheets 3–4 are **structural inspiration only** — never copy sample sentences verbatim; map density/scope/stack/outcome patterns to the candidate's real numbers.
5. No **Data Engineer** position row in Sheet 2; DE signal lives in Impact/Accomplishment contexts (ETL, Spark, pipelines).

## Unique contributions

- Only raw source with a **verb + context lookup table** (103 rows) — directly implements the schema verb rule (now in the `/tailor` skill) that was deferred until this ingest.
- Only source with **85 role-type ATS keyword rows** in one table — fastest way to cross-check JD must-haves against a title-matched row (DS, MLE, Data Analyst, DevOps, Solutions Architect, etc.).
- Only source with **99 pre-rendered "Accomplished [X] as measured by [Y] by doing [Z]"** impact lines — structural gold for [`bullets.md`](../concepts/bullets.md).
- Overlaps `data-science-keywords.md` on DS keywords but xlsx DS row is **shorter** (15 terms, no Transformers/MLOps/HuggingFace). **data-science-keywords remains primary** for DS tailoring; xlsx row = minimum ATS intersection baseline.
- Overlaps `describing-ai-work.md` on verbs — xlsx includes `Utilized`, `Spearheaded`, `Architected`, `Streamlined`, `Optimized` that Nate flags as "safe AI-tone"; wiki resolves: sheet = allowed list, tactile verbs = preferred defaults.
- Cross-validated by [`action-verbs-by-skill.md`](./action-verbs-by-skill.md) (`action-verbs-by-skill.md`, 2026-05-22): 52-verb intersection; xlsx retains primacy for tech/DS/ML bullets.

## Sheet inventory

### Sheet 1: Action Verbs (103 entries)

| Column | Content |
|--------|---------|
| Action Verb | Past-tense opener (e.g. Built, Trained, Optimized) |
| Context for Tech Roles | When to use this verb (sprint velocity, ML models, data pipelines, etc.) |

**Data quality notes:**
- Duplicate verb rows: `Automated`, `Implemented`, `Orchestrated`, `Instrumented`, `Provisioned`, `Validated` each appear **twice** with slightly different context strings — treat as one verb.
- ~42 of 103 contexts are DS/ML-relevant (ML models, data pipelines, metrics, algorithms, observability, etc.).

**DS/ML-relevant verb sample** (full list in concept page): Built, Developed, Trained, Optimized, Analyzed, Deployed, Engineered, Automated, Integrated, Scaled, Reduced, Validated, Visualized, Benchmarked, Profiled, Prototyped, Synthesized, Instrumented, Hardened, Dockerized.

### Sheet 2: ATS Tech Stack Keywords (85 position titles)

Each row: `Position Title` | `Tech Stack Keywords` (comma-separated).

**Rows most relevant to DS/ML JDs (illustrative only, keywords come from JD ∩ master):**

| Position Title | Keywords (verbatim from sheet) |
|----------------|-------------------------------|
| Data Scientist | Python, R, SQL, TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy, Jupyter, Spark, Hadoop, Tableau, Matplotlib, Keras, XGBoost |
| Machine Learning Engineer | Python, TensorFlow, PyTorch, Scikit-learn, Keras, Docker, Kubernetes, MLflow, Kubeflow, Apache Airflow, Spark, AWS SageMaker, Azure ML, Jupyter, FastAPI |
| Data Analyst | SQL, Excel, Tableau, Power BI, Python, R, Google Analytics, Looker, Snowflake, BigQuery, SPSS, SAS, Google Data Studio, Alteryx, Redshift |
| DevOps Engineer | Kubernetes, Docker, Terraform, Ansible, Jenkins, GitLab CI/CD, AWS, Azure, GCP, Prometheus, Grafana, ELK Stack, Helm, ArgoCD, CircleCI |
| Solutions Architect | AWS, Azure, GCP, Terraform, Docker, Kubernetes, Microservices, REST APIs, GraphQL, MongoDB, PostgreSQL, Redis, Kafka, Elasticsearch, Snowflake |
| Research Scientist | Python, R, MATLAB, SPSS, SAS, Jupyter, GraphPad Prism, Origin, LabVIEW, ImageJ, EndNote, Zotero, Mendeley, Git, LaTeX |
| Software Engineer | Python, Java, JavaScript, TypeScript, C++, Go, Ruby, React, Node.js, Git, Docker, Kubernetes, AWS, Jenkins, PostgreSQL |

**Notable absence:** no `Data Engineer` row. DE keywords inferred from Impact contexts (ETL, Spark, Airflow, pipeline) — absorbed inline, not a dedicated role page unless the user requests.

**Other titles** (85 total): PM, marketing, sales, healthcare, civil/mechanical engineering, etc. — useful when a user targets those roles.

### Sheet 3: Accomplishment Examples (99 contexts)

| Column | Content |
|--------|---------|
| Context of Accomplishment | Scenario label (e.g. "Built data pipeline for analytics") |
| Sample Sentence | Full example bullet — **do not copy** |

**DS/ML-ish contexts (~12):** Built data pipeline for analytics; Built real-time data processing system; Implemented machine learning model deployment; Built data validation and quality framework; Optimized database performance; etc.

**Use:** structural density — team size + stack + quantified outcome in one line.

### Sheet 4: Impact Examples (99 contexts)

| Column | Content |
|--------|---------|
| Context | Domain label (e.g. "Machine Learning Engineering / Data Science") |
| Impact Statements | Strict `Accomplished [X] as measured by [Y] by doing [Z]` template — **do not copy** |

**DS/ML-ish impact contexts (~13):**
- Data Engineering / Search Engineering
- Data Engineering / ETL Development
- Data Engineering / Big Data
- Data Engineering / Stream Processing
- Machine Learning Engineering / AI
- Machine Learning Engineering / Data Science
- (+ container/DevOps contexts when JD is MLOps-heavy)

**Example structure** (ML accuracy — paraphrase only):
> Accomplished 60% improvement in ML model accuracy as measured by F1 score from 0.70 to 0.88 by implementing feature engineering, hyperparameter tuning, and ensemble methods in Python, scikit-learn

## Key claims (with sheet anchors)

- **Sheet 1**: Strong bullets start with action verbs whose context column matches the bullet's domain. (schema: `/tailor` skill, "Verbs and XYZ")
- **Sheet 2**: ATS systems match Position Title keyword rows — mirror JD tools that appear in the matching row AND in master. (schema + tailoring heuristic)
- **Sheet 3**: Accomplishment density = action + scope + stack + quantified outcome in one sentence. (structural)
- **Sheet 4**: Impact statements follow Lazlo Bock XYZ verbatim phrasing. (corroborates `ml-engineer-resume-guide.md` §5.4.2)
- **Casing**: Sheet uses `Scikit-learn` (capital S); master/data-science-keywords often use `scikit-learn` — **mirror JD casing** when tailoring.

## Direct quotes worth reusing

None verbatim from the workbook (examples are generic SWE/enterprise templates). Use as **shape references** only.

## Links into the wiki

- **Created**: `data-analyst.md` (retired 2026-10-01)
- **Also feeds**: [`../concepts/action-verbs.md`](../concepts/action-verbs.md), [`../concepts/keywords-and-skills.md`](../concepts/keywords-and-skills.md), [`../concepts/bullets.md`](../concepts/bullets.md), `data-scientist.md` (retired 2026-10-01), `ml-engineer.md` (retired 2026-10-01), `genai-llm-engineer.md` (retired 2026-10-01) (cross-link only)
- **Compiled**: [`../rulebook.md`](../rulebook.md)

## Claims absorbed inline (no dedicated page)

- **Data Engineer** playbook: no Sheet 2 row; promote ETL/Spark/pipeline bullets from Impact contexts when DE-titled JD appears — no field-specific page (the wiki has none since 2026-10-01).
- **Accomplishment Examples** structural rules folded into `bullets.md` (not a separate concept page).

## Disagreements with other sources

| Topic | xlsx | Other source | Wiki resolution |
|-------|------|--------------|-----------------|
| Safe AI verbs | Includes Utilized, Spearheaded, Architected, Streamlined, Optimized | `describing-ai-work.md` §9 warns against them | Sheet = allowed; **prefer tactile verbs** when true |
| DS keyword bank | 15-term DS row | `data-science-keywords.md` 60+ term bank | **data-science-keywords primary**; xlsx row = minimum intersection set |
| scikit-learn casing | `Scikit-learn` | `scikit-learn` in data-science-keywords/master | Mirror **JD casing** |
| Verb duplicates | 6 verbs listed twice | — | Dedupe in agent rules |
