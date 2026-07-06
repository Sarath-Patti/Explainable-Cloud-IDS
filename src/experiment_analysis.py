import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("reports", exist_ok=True)

print("=" * 60)
print("EXPERIMENT ANALYSIS")
print("=" * 60)

# ============================================================
# LOAD RESULTS
# ============================================================

comparison = pd.read_csv("reports/comparison_table.csv")

# ============================================================
# FEATURE REDUCTION
# ============================================================

baseline_features = 43

comparison["Feature Reduction (%)"] = (
    (baseline_features - comparison["Features"])
    / baseline_features
) * 100

comparison = comparison.round(4)

comparison.to_csv(
    "reports/comparison_table.csv",
    index=False
)

print("\nUpdated comparison table saved.")

# ============================================================
# RANDOM FOREST
# ============================================================

rf = comparison[
    comparison["Model"] == "Random Forest"
].sort_values("Features")

# ============================================================
# XGBOOST
# ============================================================

xgb = comparison[
    comparison["Model"] == "XGBoost"
].sort_values("Features")

# ============================================================
# ACCURACY COMPARISON
# ============================================================

plt.figure(figsize=(9,5))

labels = [
    "RF-30",
    "XGB-30",
    "RF-20",
    "XGB-20",
    "RF-10",
    "XGB-10"
]

accuracy = comparison["Accuracy"] * 100

bars = plt.bar(labels, accuracy)

plt.ylabel("Accuracy (%)")
plt.title("Model Accuracy Comparison")

plt.ylim(99.98,100.00)

for bar in bars:

    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():.4f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig(
    "reports/accuracy_comparison.png",
    dpi=300
)

plt.close()

print("Accuracy comparison generated.")

# ============================================================
# TRAINING TIME
# ============================================================

plt.figure(figsize=(8,5))

plt.plot(
    rf["Features"],
    rf["Training Time"],
    marker="o",
    linewidth=2,
    label="Random Forest"
)

plt.plot(
    xgb["Features"],
    xgb["Training Time"],
    marker="o",
    linewidth=2,
    label="XGBoost"
)

plt.xlabel("Number of Features")
plt.ylabel("Training Time (seconds)")
plt.title("Training Time vs Number of Features")
plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/training_time_vs_features.png",
    dpi=300
)

plt.close()

print("Training time graph generated.")

# ============================================================
# F1 SCORE COMPARISON
# ============================================================

plt.figure(figsize=(9,5))

f1 = comparison["F1"] * 100

bars = plt.bar(labels, f1)

plt.ylabel("F1 Score (%)")
plt.title("Model F1 Score Comparison")

plt.ylim(99.98,100.00)

for bar in bars:

    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():.4f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig(
    "reports/f1_comparison.png",
    dpi=300
)

plt.close()

print("F1 comparison generated.")

# ============================================================
# SUMMARY
# ============================================================

best_rf = comparison[
    comparison["Model"] == "Random Forest"
].sort_values(
    "Accuracy",
    ascending=False
).iloc[0]

best_xgb = comparison[
    comparison["Model"] == "XGBoost"
].sort_values(
    "Accuracy",
    ascending=False
).iloc[0]

with open(
    "reports/research_summary.txt",
    "w"
) as f:

    f.write("Explainable Cloud IDS Research Summary\n")
    f.write("=" * 45 + "\n\n")

    f.write(f"Random Forest Best Accuracy : {best_rf['Accuracy']:.6f}\n")
    f.write(f"Random Forest Features      : {int(best_rf['Features'])}\n\n")

    f.write(f"XGBoost Best Accuracy       : {best_xgb['Accuracy']:.6f}\n")
    f.write(f"XGBoost Features            : {int(best_xgb['Features'])}\n\n")

    f.write("Research Conclusion\n")
    f.write("-------------------\n")
    f.write(
        "SHAP successfully identified the most informative "
        "network-flow features. Reduced feature models "
        "maintained nearly identical detection performance "
        "while decreasing computational complexity.\n"
    )

print("Research summary generated.")

print()
print("=" * 60)
print("FILES GENERATED")
print("=" * 60)

print("reports/accuracy_comparison.png")
print("reports/training_time_vs_features.png")
print("reports/f1_comparison.png")
print("reports/research_summary.txt")