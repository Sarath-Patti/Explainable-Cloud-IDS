import joblib
import numpy as np
import pandas as pd
import shap
import os
import matplotlib.pyplot as plt

os.makedirs("reports", exist_ok=True)
from dataset_loader import load_dataset

print("=" * 60)
print("SHAP ANALYSIS")
print("=" * 60)

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("models/xgboost_model.pkl")

print("\nModel loaded successfully.")

# ============================================================
# LOAD DATASET
# ============================================================

df = load_dataset(
    "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

# ============================================================
# CLEANING
# ============================================================

df.replace(
    [float("inf"), float("-inf")],
    np.nan,
    inplace=True
)

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# ============================================================
# FEATURES
# ============================================================

X = df.drop(columns=["Label"])

# Correlation-based feature selection
corr_matrix = X.corr().abs()

upper = corr_matrix.where(
    np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
)

threshold = 0.90

to_drop = [
    column
    for column in upper.columns
    if any(upper[column] > threshold)
]

X = X.drop(columns=to_drop)

print(f"\nFeatures used: {X.shape[1]}")
print(f"Samples: {X.shape[0]}")

# ============================================================
# CREATE SHAP EXPLAINER
# ============================================================

print("\nCreating SHAP Explainer...")

explainer = shap.TreeExplainer(model)

print("Explainer created successfully.")

# ============================================================
# COMPUTE SHAP VALUES
# ============================================================

print("\nComputing SHAP values...")

sample = X.sample(
    n=1000,
    random_state=42
)

shap_values = explainer(sample)

print("SHAP values computed successfully.")

print("\nSHAP Value Shape:")
print(shap_values.values.shape)
# ============================================================
# SHAP SUMMARY PLOT
# ============================================================

print("\nGenerating SHAP Summary Plot...")

plt.figure(figsize=(12, 8))

shap.summary_plot(
    shap_values,
    sample,
    max_display=20,
    show=False
)

plt.tight_layout()

plt.savefig(
    "reports/shap_summary_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("SHAP Summary Plot saved.")

# ============================================================
# SHAP BAR PLOT
# ============================================================

print("Generating SHAP Feature Importance Plot...")

plt.figure(figsize=(10, 8))

shap.plots.bar(
    shap_values,
    show=False
)

plt.tight_layout()

plt.savefig(
    "reports/shap_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("SHAP Feature Importance Plot saved.")