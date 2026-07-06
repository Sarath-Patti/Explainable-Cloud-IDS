# Explainable Cloud Intrusion Detection System
## Summer Research Progress Notes

**Student:** Patti Sarath  
**Institute:** National Institute of Technology Rourkela  
**Department:** Computer Science and Engineering

---

# Research Title

Explainable Cloud Intrusion Detection System using Machine Learning and SHAP-based Explainable AI

---

# Research Objective

Develop an intrusion detection framework for cloud environments that not only achieves high detection accuracy but also provides interpretable explanations for every prediction using Explainable Artificial Intelligence (XAI).

The proposed framework aims to improve the trustworthiness of intrusion detection systems by identifying the most influential network-flow features responsible for attack detection.

---

# Current Research Progress

## Phase 1 – Project Foundation ✅

### Completed

- Project setup
- GitHub repository creation
- Project documentation
- Dataset loading module
- Dataset exploration
- Data validation
- Data cleaning

### Dataset

Dataset Used:
- CIC-IDS2017

Working Dataset:
- Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

---

## Data Validation

Initial Samples:
225,745

Issues Identified

- Missing values
- Infinite values
- Duplicate records
- Mixed data types

---

## Data Cleaning Results

| Item | Count |
|------|-------:|
| Missing Values Removed | 4 |
| Infinite Values Removed | 64 |
| Duplicate Rows Removed | 2,633 |
| Final Samples | 223,082 |

Observation

The dataset is now free from invalid entries and suitable for machine learning experiments.

---

# Phase 2 – Exploratory Data Analysis ✅

Completed

- Summary statistics
- Dataset exploration
- Class distribution
- Feature distribution
- Outlier analysis
- Correlation analysis

---

## Summary Statistics

Performed statistical analysis including

- Mean
- Standard Deviation
- Minimum
- Maximum
- Quartiles

Purpose

Understand the behaviour of network traffic features.

---

## Class Distribution

Classes

- BENIGN
- DDoS

Observation

The selected subset contains a balanced distribution suitable for binary classification.

---

## Feature Distribution

Visualized important network-flow features.

Generated histograms for numerical attributes.

Purpose

Understand feature behaviour before model development.

---

## Outlier Analysis

Detected extreme values using

- Boxplots
- Distribution plots

Observation

Large variations exist in several traffic features, which is expected in real-world network traffic.

---

## Correlation Analysis

Performed Pearson Correlation Analysis.

Threshold Used

0.90

Results

Original Features : 78

Highly Correlated Features Removed : 35

Remaining Features : 43

Feature Reduction

Approximately 45%

Observation

Removing redundant features reduces dimensionality while preserving most of the useful information.

---

# Phase 3 – Feature Engineering ✅

Completed

- Correlation-based Feature Selection
- Feature Scaling
- Train-Test Split

---

## Feature Scaling

Technique

StandardScaler

Purpose

Prepare standardized datasets for future experiments and improve compatibility with multiple machine learning algorithms.

---

## Train-Test Split

Training Samples

178,465

Testing Samples

44,617

Training Features

43

Testing Features

43

Random State

42

Train-Test Ratio

80 : 20

---

# Phase 4 – Machine Learning Models ✅

## Random Forest

Status

Completed

Model Parameters

- RandomForestClassifier
- Number of Trees : 100
- Random State : 42

Performance

| Metric | Value |
|---------|------:|
| Accuracy | 99.99% |
| Precision | 99.99% |
| Recall | 99.99% |
| F1 Score | 99.99% |

Confusion Matrix

```
[[19011     3]
 [    2 25601]]
```

Observation

Random Forest produced excellent classification performance with only five misclassified instances.

---

## Random Forest Feature Importance

Generated

- Feature Importance CSV
- Feature Importance Plot

Top Important Features

1. Fwd Packet Length Max
2. Init_Win_bytes_forward
3. Total Length of Fwd Packets
4. Total Fwd Packets
5. act_data_pkt_fwd

---

## XGBoost

Status

Completed

Model Parameters

- XGBClassifier
- Estimators : 100
- Max Depth : 6
- Learning Rate : 0.1

Performance

| Metric | Value |
|---------|------:|
| Accuracy | 100.00% |
| Precision | 100.00% |
| Recall | 100.00% |
| F1 Score | 100.00% |

Confusion Matrix

```
[[19014     0]
 [    1 25602]]
```

Observation

XGBoost slightly outperformed Random Forest by reducing the number of misclassified samples to only one.

---

# Research Extension

The research extension has now been successfully completed.

Unlike conventional Intrusion Detection Systems that primarily focus on maximizing prediction accuracy, this work demonstrates how Explainable Artificial Intelligence (XAI) can improve both model transparency and computational efficiency.

SHAP (SHapley Additive exPlanations) was integrated into the proposed framework to:

- Explain model predictions
- Identify the most influential network-flow features
- Reduce feature dimensionality
- Build lightweight IDS models without sacrificing detection performance

This transforms the IDS from a black-box classifier into an interpretable and explainable security framework.

---

# Phase 5 – SHAP Explainability

## Completed

Generated

- SHAP Summary Plot
- SHAP Feature Importance Plot
- Global SHAP Feature Ranking

Top Influential Features

- Fwd Packet Length Max
- Total Length of Fwd Packets
- Destination Port
- Bwd Packet Length Max
- Init_Win_bytes_forward
- Bwd IAT Total
- Init_Win_bytes_backward

Observation

SHAP clearly identified the features contributing most significantly to DDoS attack detection while providing global model interpretability.

---

# Phase 6 – SHAP-Based Feature Optimization

Three lightweight feature subsets were created using SHAP rankings.

Generated Feature Sets

- Top-30 Features
- Top-20 Features
- Top-10 Features

Each feature subset was used to retrain both

- Random Forest
- XGBoost

---

# Experimental Results

| Model | Features | Accuracy | Precision | Recall | F1 Score |
|--------|---------:|----------:|-----------:|---------:|----------:|
| Random Forest | 30 | 99.9888% | 99.99% | 99.99% | 99.99% |
| XGBoost | 30 | 99.9978% | 100.00% | 99.996% | 99.998% |
| Random Forest | 20 | 99.9888% | 99.99% | 99.99% | 99.99% |
| XGBoost | 20 | 99.9978% | 100.00% | 99.996% | 99.998% |
| Random Forest | 10 | 99.9910% | 99.99% | 99.996% | 99.992% |
| XGBoost | 10 | 99.9978% | 100.00% | 99.996% | 99.998% |

---

# Experimental Analysis

Generated Reports

- SHAP Summary Plot
- SHAP Feature Importance Plot
- SHAP Feature Ranking
- Top-30 Features
- Top-20 Features
- Top-10 Features
- Accuracy Comparison
- F1 Score Comparison
- Training Time Comparison
- Comparison Table
- Research Summary

---

# Key Findings

- Successfully reduced the feature space from **43 to 10** using SHAP.
- Detection accuracy remained nearly identical after feature reduction.
- XGBoost consistently achieved the best overall performance.
- Random Forest training time decreased significantly with fewer features.
- SHAP proved valuable for both explainability and feature optimization.

---

# Research Contribution

The proposed framework demonstrates that explainability can be used not only for interpreting predictions but also for constructing efficient machine learning models.

Major contributions include:

- Explainable Cloud IDS using SHAP
- Lightweight IDS through SHAP-guided feature selection
- Comparative evaluation of Random Forest and XGBoost
- Performance analysis across Top-30, Top-20, and Top-10 feature subsets
- Experimental validation of feature reduction with negligible accuracy loss

---

# Work Completed

✅ Dataset Validation

✅ Data Cleaning

✅ Exploratory Data Analysis

✅ Feature Distribution Analysis

✅ Outlier Detection

✅ Correlation Analysis

✅ Feature Selection

✅ Feature Scaling

✅ Train-Test Split

✅ Random Forest

✅ Random Forest Feature Importance

✅ XGBoost

✅ SHAP Explainability

✅ SHAP Summary Plot

✅ SHAP Feature Importance

✅ SHAP Feature Ranking

✅ Top-30 Feature Selection

✅ Top-20 Feature Selection

✅ Top-10 Feature Selection

✅ Retrained Random Forest

✅ Retrained XGBoost

✅ Comparative Performance Analysis

✅ Research Documentation

---

# Next Phase

The next stage of the project focuses on transforming the research framework into a practical application.

Planned features include:

- Explainable Cloud IDS Web Application
- CSV Upload Interface
- Attack Prediction Dashboard
- Confidence Score Visualization
- SHAP-Based Prediction Explanations
- Downloadable Analysis Reports

---

# GitHub Progress

Current Modules

- Dataset Loader
- Validation
- Cleaning
- EDA
- Feature Distribution
- Outlier Analysis
- Correlation Analysis
- Feature Selection
- Feature Scaling
- Train-Test Split
- Random Forest
- XGBoost
- SHAP Analysis
- SHAP Feature Selection
- Lightweight IDS Training
- Experimental Analysis

Generated Outputs

- Trained Models
- Metrics Reports
- Confusion Matrices
- Feature Importance Reports
- SHAP Visualizations
- Feature Ranking Reports
- Comparison Table
- Research Summary
- Architecture Diagram

---

# Current Progress

Overall Completion

**Research Phase: 100% Complete**

**Overall Project: Approximately 80% Complete**

Remaining Work

- Explainable Cloud IDS Web Application
- Interactive Dashboard
- Report Generation
- Deployment
- Final Demonstration