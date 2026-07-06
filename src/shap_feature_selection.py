import os
import joblib
import numpy as np
import pandas as pd
import shap

from dataset_loader import load_dataset

os.makedirs("reports", exist_ok=True)

print("=" * 60)
print("SHAP FEATURE SELECTION")
print("=" * 60)

# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("models/xgboost_model.pkl")

# ============================================================
# LOAD DATASET
# ============================================================

df = load_dataset(
    "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

# ============================================================
# CLEAN DATA
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

print(f"Features Used : {X.shape[1]}")

# ============================================================
# SHAP VALUES
# ============================================================

sample = X.sample(
    n=1000,
    random_state=42
)

explainer = shap.TreeExplainer(model)

shap_values = explainer(sample)

# ============================================================
# MEAN ABSOLUTE SHAP
# ============================================================

importance = np.abs(
    shap_values.values
).mean(axis=0)

feature_importance = pd.DataFrame({

    "Feature": sample.columns,

    "Mean_SHAP": importance

})

feature_importance = feature_importance.sort_values(
    by="Mean_SHAP",
    ascending=False
)

# ============================================================
# SAVE COMPLETE RANKING
# ============================================================

feature_importance.to_csv(
    "reports/shap_feature_ranking.csv",
    index=False
)

# ============================================================
# TOP 30
# ============================================================

top30 = feature_importance.head(30)

top30.to_csv(
    "reports/top30_features.csv",
    index=False
)

# ============================================================
# TOP 20
# ============================================================

top20 = feature_importance.head(20)

top20.to_csv(
    "reports/top20_features.csv",
    index=False
)

# ============================================================
# TOP 10
# ============================================================

top10 = feature_importance.head(10)

top10.to_csv(
    "reports/top10_features.csv",
    index=False
)

# ============================================================
# PRINT RESULTS
# ============================================================

print()

print("=" * 60)
print("TOP 10 SHAP FEATURES")
print("=" * 60)

print(top10)

print()

print("=" * 60)
print("FILES GENERATED")
print("=" * 60)

print("reports/shap_feature_ranking.csv")
print("reports/top30_features.csv")
print("reports/top20_features.csv")
print("reports/top10_features.csv")