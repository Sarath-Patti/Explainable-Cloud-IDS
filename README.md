# Explainable Cloud Intrusion Detection System

An Explainable Artificial Intelligence (XAI) based Intrusion Detection System for cloud environments using Machine Learning and SHAP explainability.

This project is being developed as a Summer Research Project at the Department of Computer Science and Engineering, National Institute of Technology Rourkela.

---

## Project Motivation

Cloud computing has become the backbone of modern applications, making it a major target for cyber attacks such as DDoS, Port Scans, and Web Attacks.

Although Machine Learning based Intrusion Detection Systems achieve high detection accuracy, they often behave as **black-box models**, making it difficult for security analysts to understand why a particular network flow is classified as malicious.

This project addresses that limitation by integrating **Explainable Artificial Intelligence (XAI)** into the intrusion detection pipeline using **SHAP (SHapley Additive exPlanations)**.

The goal is to develop an IDS that is not only accurate but also transparent and trustworthy.

---

# Research Objectives

- Build a machine learning based Cloud IDS
- Perform comprehensive data preprocessing
- Analyze network traffic characteristics
- Train high-performance ML models
- Explain predictions using SHAP
- Identify the most influential network traffic features
- Develop a lightweight and explainable intrusion detection framework

---

# Proposed Research Extension

Most existing IDS research focuses primarily on improving classification accuracy.

This project extends traditional IDS by introducing:

- Explainable AI using SHAP
- Global and local prediction explanations
- SHAP-guided feature selection
- Lightweight IDS using Top-K important features
- Comparative performance analysis between full-feature and reduced-feature models

---

# Dataset

Dataset Used

**CIC-IDS2017**

Working Dataset

- Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

Dataset contains

- Benign traffic
- DDoS attacks

---

# Project Structure

```text
Explainable-Cloud-IDS/

├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── random_forest_model.pkl
│   └── xgboost_model.pkl
│
├── reports/
│   ├── research_notes.md
│   ├── class_distribution.png
│   ├── random_forest_metrics.csv
│   ├── random_forest_confusion_matrix.png
│   ├── random_forest_feature_importance.csv
│   ├── random_forest_feature_importance.png
│   ├── xgboost_metrics.csv
│   ├── xgboost_confusion_matrix.png
│   ├── xgboost_feature_importance.csv
│   └── xgboost_feature_importance.png
│
├── src/
│   ├── dataset_loader.py
│   ├── validation.py
│   ├── cleaning.py
│   ├── eda.py
│   ├── feature_distribution.py
│   ├── outlier_analysis.py
│   ├── correlation_analysis.py
│   ├── feature_selection.py
│   ├── scaling.py
│   ├── data_split.py
│   ├── random_forest.py
│   └── xgboost_model.py
│
├── README.md
├── CHANGELOG.md
└── requirements.txt
```

---

# Research Workflow

```text
Raw Dataset
      │
      ▼
Dataset Validation
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Correlation Analysis
      │
      ▼
Feature Selection
      │
      ▼
Feature Scaling
      │
      ▼
Train-Test Split
      │
      ▼
Random Forest
      │
      ▼
XGBoost
      │
      ▼
SHAP Explainability
      │
      ▼
Top-K Feature Selection
      │
      ▼
Performance Comparison
```

---

# Completed Work

## Phase 1 — Project Foundation

- Project setup
- GitHub repository
- Dataset loading
- Dataset validation
- Data cleaning

---

## Phase 2 — Exploratory Data Analysis

- Summary statistics
- Dataset exploration
- Class distribution
- Feature distributions
- Outlier analysis
- Correlation analysis

---

## Phase 3 — Feature Engineering

- Correlation-based feature selection
- 45% feature reduction
- Feature scaling
- Train-test split

---

## Phase 4 — Machine Learning Models

### Random Forest

Accuracy

99.99%

Generated

- Trained model
- Evaluation metrics
- Confusion matrix
- Feature importance report
- Feature importance visualization

---

### XGBoost

Accuracy

100.00%

Generated

- Trained model
- Evaluation metrics
- Confusion matrix
- Feature importance report
- Feature importance visualization

---

# Current Results

| Model | Accuracy |
|--------|----------|
| Random Forest | 99.99% |
| XGBoost | 100.00% |

---

# Current Research Progress

| Phase | Status |
|--------|--------|
| Dataset Validation | ✅ |
| Data Cleaning | ✅ |
| Exploratory Data Analysis | ✅ |
| Feature Engineering | ✅ |
| Random Forest | ✅ |
| XGBoost | ✅ |
| SHAP Explainability | 🔄 In Progress |
| Feature Optimization | ⏳ |
| Performance Comparison | ⏳ |
| Final Report | ⏳ |

Overall Project Progress

**Approximately 75% Completed**

---

# Upcoming Work

- SHAP Explainability
- SHAP Summary Plot
- SHAP Waterfall Plot
- SHAP Feature Importance
- Top-30 Feature Selection
- Top-20 Feature Selection
- Top-10 Feature Selection
- Retraining ML Models
- Comparative Performance Analysis
- Final Report
- Research Presentation

---

# Technologies Used

Programming Language

- Python

Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- SHAP
- Joblib

Tools

- Git
- GitHub
- Jupyter Notebook
- Visual Studio Code

---

# Future Scope

- Multi-class intrusion detection
- Real-time cloud traffic monitoring
- Deep learning based IDS
- Hybrid Explainable AI models
- Deployment using Flask/FastAPI
- Cloud-native intrusion detection framework

---

# Author

**Patti Sarath**

M.Tech, Computer Science and Engineering

National Institute of Technology Rourkela

Summer Research Project 2026

---

# License

This repository is intended for academic and research purposes.