# Explainable Cloud IDS

An Explainable Machine Learning Framework for Cloud Intrusion Detection using the CIC-IDS2017 dataset.

---

## Overview

Cloud environments are increasingly vulnerable to cyber attacks such as Distributed Denial of Service (DDoS), brute-force attacks, and network intrusions. Traditional intrusion detection systems often fail to provide accurate detection while also lacking interpretability.

This project aims to develop an Explainable Machine Learning based Intrusion Detection System (IDS) capable of accurately identifying malicious network traffic and explaining the predictions using Explainable AI (XAI) techniques.

The project is being developed as part of a Summer Research Internship.

---

## Objectives

- Build a complete machine learning pipeline for intrusion detection.
- Perform comprehensive data preprocessing and cleaning.
- Analyze network traffic using Exploratory Data Analysis (EDA).
- Train and evaluate multiple machine learning models.
- Compare model performance using standard evaluation metrics.
- Explain model predictions using SHAP.
- Create a reproducible and modular research workflow.

---

## Dataset

**Dataset:** CIC-IDS2017

The CIC-IDS2017 dataset contains modern network traffic including both normal and malicious activities such as:

- DDoS
- Port Scan
- Brute Force
- Web Attacks
- Botnet
- Infiltration

Current implementation uses the **Friday Working Hours - Afternoon DDoS** dataset.

---

## Project Structure

```text
Explainable-Cloud-IDS/

├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── reports/
│   ├── figures/
│   └── research_notes.md
│
├── src/
│   ├── cleaning.py
│   ├── dataset_loader.py
│   ├── eda.py
│   ├── explorer.py
│   ├── preprocessing.py
│   ├── test_loader.py
│   └── validation.py
│
├── CHANGELOG.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Current Progress

- [x] Project Setup
- [x] Dataset Loading
- [x] Dataset Exploration
- [x] Data Validation
- [x] Data Cleaning
- [x] Initial Exploratory Data Analysis
- [ ] Feature Engineering
- [ ] Baseline Machine Learning Model
- [ ] Model Evaluation
- [ ] Model Optimization
- [ ] Explainable AI (SHAP)

---

## Data Cleaning Summary

Original Dataset

- Rows: **225,745**
- Columns: **79**

After Cleaning

- Rows: **223,082**
- Columns: **79**

Cleaning operations performed:

- Removed leading/trailing spaces from feature names.
- Replaced infinite values with NaN.
- Removed rows containing missing values.
- Removed duplicate records.
- Saved cleaned dataset for further analysis.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- SHAP
- Jupyter Notebook

---

## Future Work

- Complete Exploratory Data Analysis
- Feature Selection
- Train Random Forest model
- Train XGBoost model
- Hyperparameter Optimization
- SHAP Explainability
- Performance Comparison
- Final Research Report

---

## Research Status

This project is currently under active development.

Progress is documented through:

- `CHANGELOG.md`
- `reports/research_notes.md`

---

## Author

**Sarath Patti**

M.Tech Computer Science and Engineering

National Institute of Technology Rourkela

---

## License

This project is intended for academic and research purposes.