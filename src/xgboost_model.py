import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dataset_loader import load_dataset

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

from xgboost import XGBClassifier

os.makedirs("models", exist_ok=True)
os.makedirs("reports", exist_ok=True)

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
# FEATURES & LABEL
# ============================================================

X = df.drop(columns=["Label"])

y = df["Label"]

# ============================================================
# VERIFY DATA TYPES
# ============================================================

object_columns = X.select_dtypes(include=["object"]).columns.tolist()

if len(object_columns) > 0:
    print("\nObject columns detected:")
    print(object_columns)

    for column in object_columns:
        X[column] = pd.to_numeric(
            X[column],
            errors="coerce"
        )

    valid_rows = X.notna().all(axis=1)

    X = X.loc[valid_rows]

    y = y.loc[valid_rows]

print("\nRemaining object columns:")

print(
    X.select_dtypes(include=["object"]).columns.tolist()
)

# ============================================================
# CORRELATION FEATURE REDUCTION
# ============================================================

corr_matrix = X.corr().abs()

upper = corr_matrix.where(
    np.triu(
        np.ones(corr_matrix.shape),
        k=1
    ).astype(bool)
)

threshold = 0.90

to_drop = [
    column
    for column in upper.columns
    if any(upper[column] > threshold)
]

X = X.drop(columns=to_drop)

print(f"\nFeatures after reduction: {X.shape[1]}")

# ============================================================
# LABEL ENCODING
# ============================================================

encoder = LabelEncoder()

y = encoder.fit_transform(y)

# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training Samples : {X_train.shape[0]}")
print(f"Testing Samples  : {X_test.shape[0]}")

# ============================================================
# XGBOOST MODEL
# ============================================================

model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    random_state=42,
    n_jobs=-1,
    eval_metric="logloss"
)

print("\nTraining XGBoost Model...\n")

model.fit(X_train, y_train)

# ============================================================
# SAVE MODEL
# ============================================================

joblib.dump(
    model,
    "models/xgboost_model.pkl"
)

# ============================================================
# PREDICTIONS
# ============================================================

y_pred = model.predict(X_test)

# ============================================================
# EVALUATION
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

print("=" * 60)
print("XGBOOST RESULTS")
print("=" * 60)

print()

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

print()

cm = confusion_matrix(
    y_test,
    y_pred
)

print("=" * 60)
print("CONFUSION MATRIX")
print("=" * 60)

print(cm)

print()

print("=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

print(
    classification_report(
        y_test,
        y_pred,
        target_names=encoder.classes_
    )
)

# ============================================================
# SAVE METRICS
# ============================================================

metrics = pd.DataFrame({

    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],

    "Value": [
        accuracy,
        precision,
        recall,
        f1
    ]

})

metrics.to_csv(
    "reports/xgboost_metrics.csv",
    index=False
)
# ============================================================
# SAVE CONFUSION MATRIX
# ============================================================

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=encoder.classes_
)

disp.plot(cmap="Blues")

plt.title("XGBoost Confusion Matrix")

plt.tight_layout()

plt.savefig(
    "reports/xgboost_confusion_matrix.png",
    dpi=300
)

plt.close()

# ============================================================
# FEATURE IMPORTANCE
# ============================================================

importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

importance.to_csv(
    "reports/xgboost_feature_importance.csv",
    index=False
)

print()

print("=" * 60)
print("TOP 10 IMPORTANT FEATURES")
print("=" * 60)

print(importance.head(10))

# ============================================================
# FEATURE IMPORTANCE PLOT
# ============================================================

top10 = importance.head(10)

plt.figure(figsize=(10,6))

plt.barh(
    top10["Feature"][::-1],
    top10["Importance"][::-1]
)

plt.xlabel("Importance")

plt.ylabel("Feature")

plt.title("Top 10 XGBoost Feature Importance")

plt.tight_layout()

plt.savefig(
    "reports/xgboost_feature_importance.png",
    dpi=300
)

plt.close()

print()

print("=" * 60)
print("FILES GENERATED")
print("=" * 60)

print("Model:")
print("  models/xgboost_model.pkl")

print()

print("Reports:")
print("  reports/xgboost_metrics.csv")
print("  reports/xgboost_confusion_matrix.png")
print("  reports/xgboost_feature_importance.csv")
print("  reports/xgboost_feature_importance.png")