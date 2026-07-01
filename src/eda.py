import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
dataset_path = Path("data/processed/cleaned_ddos.csv")

df = pd.read_csv(dataset_path)
print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print(df.describe())

print("\n" + "=" * 60)
print("LABEL DISTRIBUTION")
print("=" * 60)

print(df["Label"].value_counts())

df["Label"].value_counts().plot(
    kind="bar",
    figsize=(6,4)
)

plt.title("Class Distribution")

plt.xlabel("Class")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig("reports/class_distribution.png")

plt.show()