<div align="center">

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=180&section=header&text=ACM%20SIGAI&fontSize=70&fontColor=ffffff&fontAlignY=38&desc=Week%201%20%26%20Week%202%20%E2%80%94%20Individual%20Task%20Submissions&descAlignY=58&descSize=18&descColor=90cdf4&animation=fadeIn" width="100%"/>

<br/>

<table border="0" cellpadding="0" cellspacing="0">
<tr>
<td align="center">

```
  🧠  Engineer · Model · Evaluate  🎯
```

</td>
</tr>
</table>

<br/>

<img src="https://img.shields.io/badge/Recruitment-ACM%20SIGAI-0ea5e9?style=flat-square&labelColor=0f172a" />
&nbsp;
<img src="https://img.shields.io/badge/Tasks-2%20Submitted-8b5cf6?style=flat-square&labelColor=0f172a" />
&nbsp;
<img src="https://img.shields.io/badge/Week%201-Feature%20Engineering-10b981?style=flat-square&labelColor=0f172a" />
&nbsp;
<img src="https://img.shields.io/badge/Week%202-Classification%20Pipeline-f97316?style=flat-square&labelColor=0f172a" />

<br/><br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-FF6600?style=for-the-badge&logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io)

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0f2027,100:2c5364&height=3&section=header" width="85%"/>

<br/>

</div>

---

## 📋 Overview

This repository holds my **ACM SIGAI recruitment submissions for Week 1 and Week 2**, kept together in one place so both tasks can be reviewed from a single link.

| | Week 1 (Mandatory) | Week 2 (Elective — Task 2) |
|---|---|---|
| **Task** | Feature Engineering Challenge | Classification Pipeline |
| **Dataset** | Santander Customer Transaction Prediction | IBM HR Analytics — Employee Attrition |
| **Goal** | Push Logistic Regression Recall from 0.83 → 0.88+ | Compare LR / RF / XGBoost head-to-head, select best model |
| **Constraint** | Model family locked to Logistic Regression | Must use LogisticRegression, RandomForestClassifier, XGBClassifier |
| **Folder** | [`feature-engineering-challenge/`](./feature-engineering-challenge) | [`workpulse/`](./workpulse) |

---

## 📂 Repository Structure

```
acm-week1-2-tasks/
│
├── feature-engineering-challenge/     ⬅ Week 1 (Mandatory)
│   ├── data/raw/
│   ├── notebooks/
│   │   └── santander_feature_engineering.ipynb
│   ├── logs/
│   │   └── experiment_log.csv
│   ├── reports/
│   │   └── report.md
│   └── artifacts/
│
├── workpulse/                          ⬅ Week 2 (Task 2 — Classification Pipeline)
│   ├── config/
│   ├── src/
│   ├── notebooks/
│   ├── data/
│   ├── artifacts/
│   ├── reports/
│   └── README.md                       (full project write-up)
│
└── README.md                           ← you are here
```

---

## 🧩 Week 1 — Feature Engineering Challenge

**Mandatory task.** Dataset: [Santander Customer Transaction Prediction](https://www.kaggle.com/c/santander-customer-transaction-prediction) (Kaggle) — 200 anonymized numeric features, binary target.

A baseline Logistic Regression model starts at **Recall = 0.83**. The task is to improve Recall to **0.88+** through feature engineering alone — no changing the model family, no external data.

**Approach:**
- Frequency/count encoding across all 200 `var_` columns
- Row-wise statistical aggregates (mean, std, min, max, skew)
- Targeted interaction terms on the top-correlated features
- Light outlier handling (IQR clipping)
- Hyperparameter tuning (`C`, `penalty`, `class_weight`)

**Deliverables:** commented notebook, auto-logged experiment CSV (including failed attempts), short markdown report.

📁 [`feature-engineering-challenge/`](./feature-engineering-challenge)

---

## 🧩 Week 2 — WorkPulse: Employee Attrition Classification Pipeline

**Task 2 (chosen elective).** Dataset: [IBM HR Analytics Attrition Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) — 1,470 employees, 35 features.

A full config-driven classification pipeline comparing **Logistic Regression, Random Forest, and XGBoost** to predict employee attrition, with 10+ domain-engineered features, SMOTE for class imbalance, GridSearch/RandomSearch tuning, and SHAP explainability.

**Result:** XGBoost selected as the winning model — **F1-macro 0.7165**, **ROC-AUC 0.7963**.

📁 [`workpulse/`](./workpulse) — see the folder's own README for the full write-up (pipeline diagram, feature engineering table, model comparison, misclassification analysis, quickstart).

---

## ⚙️ Tech Stack

<div align="center">

| Layer | Tools |
|---|---|
| Language | Python 3.10+ |
| ML | scikit-learn, XGBoost |
| Imbalance Handling | imbalanced-learn (SMOTE) |
| Explainability | SHAP |
| Data | pandas, NumPy |
| Visualization | matplotlib, seaborn |
| Config | PyYAML |

</div>

---

<div align="center">

**Nithish Kumar S**
B.Tech Computer Science · Amrita Vishwa Vidyapeetham
[GitHub](https://github.com/nithishkumar-dev-10)

</div>
