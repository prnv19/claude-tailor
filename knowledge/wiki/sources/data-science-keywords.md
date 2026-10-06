---
type: source
sources: [data-science-keywords.md]
last_updated: 2026-10-01
status: stable
---

# Data Science Keywords

> **Raw source**: `../../raw/data-science-keywords.md`
> **Author / origin**: ResumeAdapter blog (https://www.resumeadapter.com/blog/data-scientist-resume-keywords)
> **Date published / accessed**: Published 2026-01-02; clipped 2026-05-19; ingested 2026-05-22.
> **URL**: https://www.resumeadapter.com/blog/data-scientist-resume-keywords

## Key highlights

1. The only raw source with a **complete DS keyword taxonomy** (60+ terms in 8 category tables) organized for ATS mirroring.
2. Top recurring terms: **Machine Learning**, **Python**, **TensorFlow**, **PyTorch**, **Deep Learning**, **SQL**, **NLP**, **MLOps**, **Data Science**, **Model Deployment**.
3. Target **25–35 highly relevant keywords** that match the specific JD — not a dump of every term in the guide.
4. Keywords must appear **naturally in context** (Experience bullets, Skills, Projects) — stuffing fails human review even if ATS passes.
5. Strong vs weak side-by-side examples: weak resumes omit ML frameworks, MLOps terms, and quantified model metrics.

## Unique contributions

- Only source that provides a **DS-specific 8-category Skills section template** (ML Frameworks → Programming → Data Science Tools → ML Methodologies → MLOps → Cloud → Databases → Statistics).
- Only source that explicitly pairs **general methodology terms** (Machine Learning, Deep Learning) with **specific tools** (TensorFlow, PyTorch) in the same bullet.
- Overlaps heavily with `ml-engineer-resume-guide.md` / `ml-engineer.md` on production/MLOps keywords but **emphasizes analytics, EDA, statistics, and experimentation** more than MLE-specific guides.
- Marketing statistics (97% ATS usage, 75% rejection rate) are **unverified** — do not promote to `rulebook.md`.

## Key claims (with section anchors)

- **TL;DR** (lines 22–23): Include 25–35 keywords matching the job description; top terms listed.
- **§Why keywords matter** (lines 36–76): ATS scans for ML frameworks, languages, methodologies, tools, MLOps, cloud; vocabulary mismatch = filtered out.
- **§DS vs Data Scientist keywords** (lines 80–100): Broader "data science" vs role-specific "data scientist" — guide treats both as one bank; also notes MLE and AI Researcher overlap.
- **§ML Frameworks table** (lines 108–116): TensorFlow/Keras/TFX, PyTorch/Lightning/ONNX, scikit-learn, XGBoost/LightGBM/CatBoost, Spark MLlib.
- **§Programming & tools** (lines 120–128): Python, R, SQL, Pandas, NumPy, Jupyter, Matplotlib, Seaborn, Plotly; Statistical Analysis, Hypothesis Testing, A/B Testing.
- **§ML Methodologies** (lines 132–141): Supervised/Unsupervised, Deep Learning, CNN/RNN/LSTM/Transformers, NLP/BERT/GPT, Computer Vision, Reinforcement Learning.
- **§Data Science & Analytics** (lines 145–153): EDA, Feature Engineering, Big Data/Spark, Time Series/ARIMA/Prophet, Recommendation Systems, Anomaly Detection.
- **§MLOps** (lines 157–165): MLOps, Model Deployment/Serving, Docker, Kubernetes, Flask/FastAPI, CI/CD for ML, Model Monitoring/Drift, MLflow, W&B.
- **§Cloud** (lines 169–177): AWS SageMaker, Azure ML, GCP Vertex AI, Databricks, Snowflake/Snowpark.
- **§Databases** (lines 181–188): SQL/PostgreSQL/MySQL, NoSQL, Data Warehouses, ETL/Airflow/Prefect.
- **§Model Evaluation** (lines 192–198): Cross-validation, hyperparameter tuning, Accuracy/Precision/Recall/F1/ROC-AUC/RMSE.
- **§Strong example** (lines 204–228): Bullets embed frameworks + methodologies + metrics + MLOps + cloud in one line each; Skills use 8 categories.
- **§Weak example** (lines 232–254): "Worked with data", Python-only skills, no frameworks — explicit failure modes.
- **§Integration strategy** (lines 257–297): (1) Match JD, (2) natural integration across sections, (3) general + specific terms, (4) impact with keywords, (5) modern ML practices (MLOps, Transformers, cloud ML).
- **§FAQ** (lines 351–368): 25–35 keyword count; MLOps essential on modern JDs; research/projects keywords encouraged with metrics.

## Direct quotes worth reusing

- *"Include 25-35 highly relevant keywords that match the job description. Focus on ML frameworks, programming languages, and methodologies you've actually used in production."* — FAQ
- *"Don't keyword stuff. Integrate keywords into: Experience Bullets, Skills Section, Projects Section"* — Integration strategy
- Strong bullet pattern: *"Developed **machine learning models** using **Python**, **TensorFlow**, and **PyTorch**, improving prediction accuracy by 25%..."*
- Weak pattern (anti-pattern): *"Worked with data to build predictive models"* / *"Used Python for analysis"*

## Links into the wiki

- **Created roles**: `data-scientist.md` (retired 2026-10-01)
- **Also feeds**: [`../concepts/keywords-and-skills.md`](../concepts/keywords-and-skills.md), [`../concepts/structure.md`](../concepts/structure.md)
- **Updated roles**: `ml-engineer.md` (retired 2026-10-01) (cross-link only)
- **Compiled into**: [`../rulebook.md`](../rulebook.md)

## Claims absorbed inline (no dedicated concept page)

- Full keyword tables → in the raw source `knowledge/raw/data-science-keywords.md` (the role page that held them was retired 2026-10-01).
- Marketing ATS rejection stats → noted here only; not compiled into rules.
- Related-tool cross-links (TensorFlow doc, PyTorch doc, Kaggle) → reference links for the user, not agent rules.

## Caveats & re-ingest notes

- Pair with `verb-and-impact-sheets.md` Sheet 2 (Position Title: Data Scientist) on next xlsx ingest — cross-validate keyword list and exact casing.
- If `ats-friendly-resume-guide.md` ingest adds conflicting keyword-density advice, update [`../concepts/keywords-and-skills.md`](../concepts/keywords-and-skills.md) Disagreements section.
