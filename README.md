# An Explainable and Efficient Machine Learning Framework for Cloud Intrusion Detection using SHAP-Guided Feature Selection

## Overview

Cloud computing has become the backbone of modern digital infrastructure, making cloud environments an attractive target for cyber attacks such as Distributed Denial of Service (DDoS), Port Scanning, Botnets, and Web-based attacks. Intrusion Detection Systems (IDS) play a vital role in protecting these environments by identifying malicious network traffic.

Although Machine Learning (ML) based IDS models achieve high detection accuracy, they often function as black-box systems, making it difficult for security analysts to understand the reasoning behind their predictions.

This project proposes an **Explainable and Efficient Machine Learning Framework** for cloud intrusion detection using the **CIC-IDS2017 dataset**. The framework integrates **SHAP (SHapley Additive exPlanations)** to improve model interpretability and introduces **SHAP-guided feature selection** to reduce redundant features while maintaining high detection performance.

---

# Research Problem

Traditional intrusion detection systems either:

- Depend on manually designed signatures and fail to detect unknown attacks.
- Achieve high detection accuracy using machine learning but lack interpretability.
- Utilize all available network-flow features, increasing computational complexity.

The objective of this research is to design an intrusion detection framework that is:

- Accurate
- Explainable
- Computationally efficient
- Suitable for real-world cloud environments

---

# Research Objectives

- Study the CIC-IDS2017 intrusion detection dataset.
- Build a reproducible data preprocessing pipeline.
- Perform Exploratory Data Analysis (EDA).
- Train Random Forest and XGBoost models.
- Explain model predictions using SHAP.
- Reduce redundant features using correlation analysis.
- Develop an efficient IDS through SHAP-guided feature selection.

---

# Research Contribution

The primary contribution of this work is a **two-stage feature selection strategy** for cloud intrusion detection.

### Stage 1

Correlation Analysis

- Identify highly correlated features.
- Remove redundant network-flow features.

### Stage 2

SHAP-based Feature Selection

- Train baseline machine learning models.
- Compute SHAP values.
- Rank features according to importance.
- Select Top-K features.
- Retrain the model using the reduced feature set.

The proposed framework aims to improve:

- Model interpretability
- Training efficiency
- Computational cost
- Feature dimensionality
- Trustworthiness of intrusion detection decisions

---

# Dataset

Dataset:
CIC-IDS2017

Current Dataset Used:

Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

Dataset Statistics

- Original Samples: 225,745
- Clean Samples: 223,082
- Features: 79
- Target Classes:
  - BENIGN
  - DDoS

---

# Project Workflow

```
                CIC-IDS2017 Dataset
                         │
                         ▼
                Data Validation
                         │
                         ▼
                 Data Cleaning
                         │
                         ▼
          Exploratory Data Analysis
                         │
                         ▼
      Correlation-Based Feature Selection
                         │
                         ▼
      Random Forest / XGBoost Models
                         │
                         ▼
              SHAP Explainability
                         │
                         ▼
          SHAP Feature Ranking
                         │
                         ▼
          Top-K Feature Selection
                         │
                         ▼
          Performance Comparison
                         │
                         ▼
        Explainable Cloud IDS
```

---

# Repository Structure

```
Explainable-Cloud-IDS/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── reports/

│

├── src/

│   ├── dataset_loader.py

│   ├── explorer.py

│   ├── validation.py

│   ├── preprocessing.py

│   ├── cleaning.py

│   ├── eda.py

│   ├── feature_distribution.py

│   ├── outlier_analysis.py

│   ├── correlation_analysis.py

│

├── CHANGELOG.md

├── README.md

└── requirements.txt
```

---

# Project Progress

## Phase 1 — Project Foundation

- [x] Project Setup
- [x] GitHub Repository
- [x] Dataset Loading
- [x] Dataset Exploration
- [x] Data Validation
- [x] Data Cleaning

---

## Phase 2 — Advanced Exploratory Data Analysis

- [x] Summary Statistics
- [x] Class Distribution
- [x] Feature Distribution Analysis
- [x] Outlier Analysis
- [x] Correlation Analysis

---

## Phase 3 — Feature Engineering

- [ ] Correlation-Based Feature Selection
- [ ] Feature Scaling
- [ ] Train/Test Split

---

## Phase 4 — Machine Learning Models

- [ ] Random Forest
- [ ] XGBoost
- [ ] Model Evaluation

---

## Phase 5 — Explainable AI

- [ ] SHAP Explainability
- [ ] Global Feature Importance
- [ ] Local Explanation
- [ ] SHAP Feature Ranking
- [ ] Top-K Feature Selection

---

## Phase 6 — Performance Analysis

- [ ] Accuracy Comparison
- [ ] Precision
- [ ] Recall
- [ ] F1 Score
- [ ] ROC-AUC
- [ ] Training Time Comparison

---

# Current Research Findings

## Data Validation

- Missing Values: 4
- Infinite Values: 64
- Duplicate Rows: 2633

---

## Data Cleaning

- Infinite values replaced.
- Missing records removed.
- Duplicate records removed.

Final Dataset

223,082 network-flow records.

---

## Exploratory Data Analysis

Completed

- Summary Statistics
- Class Distribution
- Feature Distributions
- Outlier Analysis
- Correlation Analysis

Key Observation

Correlation analysis identified **87 highly correlated feature pairs**, indicating significant feature redundancy. These findings motivate the proposed correlation-based feature reduction prior to SHAP-guided feature selection.

---

# Technologies Used

Programming Language

- Python

Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP

Development Tools

- VS Code
- Git
- GitHub

---

# Future Work

- Correlation-based feature engineering.
- Train Random Forest and XGBoost models.
- Perform SHAP explainability analysis.
- Rank features using SHAP values.
- Develop reduced-feature IDS models.
- Compare performance across multiple feature subsets.
- Build a complete Explainable Cloud IDS framework.

---

# Author

**Patti Sarath**

M.Tech Computer Science and Engineering

National Institute of Technology Rourkela

Summer Research Project

2026

---

# License

This repository is intended for academic and research purposes.