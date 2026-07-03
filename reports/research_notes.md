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

Unlike traditional IDS implementations that focus only on maximizing classification accuracy, this research proposes an Explainable Intrusion Detection Framework.

The proposed extension integrates Explainable Artificial Intelligence using SHAP to provide transparent explanations for every prediction.

The explainability framework will also be used to identify the most influential features and construct a lightweight intrusion detection model using only the most informative network-flow features.

---

# Work Completed So Far

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

---

# Next Research Tasks

⬜ SHAP Explainability

⬜ SHAP Summary Plot

⬜ SHAP Waterfall Plot

⬜ SHAP Feature Importance

⬜ Top-30 Feature Selection

⬜ Top-20 Feature Selection

⬜ Top-10 Feature Selection

⬜ Retrain Random Forest

⬜ Retrain XGBoost

⬜ Performance Comparison

⬜ Final Evaluation

---

# Expected Final Contribution

The final system will provide

- High intrusion detection accuracy
- Explainable predictions
- Feature-level interpretation
- Lightweight IDS through SHAP-guided feature selection
- Better transparency and trust for cloud security applications

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

Generated Outputs

- Metrics Reports
- Confusion Matrices
- Feature Importance Reports
- Trained Models

---

Current Progress

Overall Completion

Approximately **75% Complete**

Remaining Work

- Explainable AI
- Feature Optimization
- Comparative Analysis
- Documentation
- Final Presentation