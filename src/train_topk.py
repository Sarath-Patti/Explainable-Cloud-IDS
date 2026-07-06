import os
import time
import joblib
import numpy as np
import pandas as pd

from dataset_loader import load_dataset

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

os.makedirs("models", exist_ok=True)
os.makedirs("reports", exist_ok=True)

print("=" * 60)
print("SHAP TOP-K FEATURE EXPERIMENTS")
print("=" * 60)
def prepare_data(feature_file):

    df = load_dataset(
        "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
    )

    df.replace(
        [float("inf"), float("-inf")],
        np.nan,
        inplace=True
    )

    df.dropna(inplace=True)

    df.drop_duplicates(inplace=True)

    feature_df = pd.read_csv(feature_file)

    selected_features = feature_df["Feature"].tolist()

    X = df[selected_features]

    y = df["Label"]

    encoder = LabelEncoder()

    y = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )
def evaluate_model(
    model,
    X_test,
    y_test
):

    prediction = model.predict(X_test)

    return {

        "Accuracy": accuracy_score(
            y_test,
            prediction
        ),

        "Precision": precision_score(
            y_test,
            prediction
        ),

        "Recall": recall_score(
            y_test,
            prediction
        ),

        "F1": f1_score(
            y_test,
            prediction
        ),

        "Confusion Matrix":
        confusion_matrix(
            y_test,
            prediction
        )

    }
def train_random_forest(
    X_train,
    y_train,
    X_test,
    y_test,
    experiment_name
):

    print(f"\nTraining Random Forest ({experiment_name})...")

    start = time.time()

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    training_time = time.time() - start

    joblib.dump(
        model,
        f"models/rf_{experiment_name}.pkl"
    )

    metrics = evaluate_model(
        model,
        X_test,
        y_test
    )

    metrics["Training Time"] = training_time

    metrics["Model"] = "Random Forest"

    metrics["Features"] = X_train.shape[1]

    return metrics
def train_xgboost(
    X_train,
    y_train,
    X_test,
    y_test,
    experiment_name
):

    print(f"Training XGBoost ({experiment_name})...")

    start = time.time()

    model = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        random_state=42,
        n_jobs=-1,
        eval_metric="logloss"
    )

    model.fit(
        X_train,
        y_train
    )

    training_time = time.time() - start

    joblib.dump(
        model,
        f"models/xgb_{experiment_name}.pkl"
    )

    metrics = evaluate_model(
        model,
        X_test,
        y_test
    )

    metrics["Training Time"] = training_time

    metrics["Model"] = "XGBoost"

    metrics["Features"] = X_train.shape[1]

    return metrics
def run_experiment(
    feature_file,
    experiment_name
):

    X_train, X_test, y_train, y_test = prepare_data(
        feature_file
    )

    rf_metrics = train_random_forest(
        X_train,
        y_train,
        X_test,
        y_test,
        experiment_name
    )

    xgb_metrics = train_xgboost(
        X_train,
        y_train,
        X_test,
        y_test,
        experiment_name
    )

    return [
        rf_metrics,
        xgb_metrics
    ]
if __name__ == "__main__":

    experiments = [

        ("reports/top30_features.csv", "top30"),

        ("reports/top20_features.csv", "top20"),

        ("reports/top10_features.csv", "top10")

    ]

    all_results = []

    print()

    print("=" * 60)
    print("RUNNING ALL EXPERIMENTS")
    print("=" * 60)

    for feature_file, experiment_name in experiments:

        print(f"\nExperiment : {experiment_name}")

        results = run_experiment(
            feature_file,
            experiment_name
        )

        all_results.extend(results)

    comparison = pd.DataFrame(all_results)

    comparison = comparison.drop(
        columns=["Confusion Matrix"]
    )

    comparison = comparison[[
        "Model",
        "Features",
        "Accuracy",
        "Precision",
        "Recall",
        "F1",
        "Training Time"
    ]]

    comparison.to_csv(
        "reports/comparison_table.csv",
        index=False
    )

    print()

    print("=" * 60)
    print("FINAL COMPARISON")
    print("=" * 60)

    print(comparison)

    print()

    print("=" * 60)
    print("FILES GENERATED")
    print("=" * 60)

    print("reports/comparison_table.csv")