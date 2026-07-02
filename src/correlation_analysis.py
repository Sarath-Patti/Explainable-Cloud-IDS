import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from dataset_loader import load_dataset

# Load dataset
df = load_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove invalid values
df.replace([float("inf"), float("-inf")], pd.NA, inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Remove target column
X = df.drop(columns=["Label"])

# Correlation matrix
corr_matrix = X.corr(numeric_only=True)

# Plot heatmap
plt.figure(figsize=(18, 14))

sns.heatmap(
    corr_matrix,
    cmap="coolwarm",
    center=0,
    square=True,
    cbar_kws={"shrink": 0.8}
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("reports/correlation_heatmap.png", dpi=300)

plt.show()

# Find highly correlated feature pairs
threshold = 0.90

high_corr = []

columns = corr_matrix.columns

for i in range(len(columns)):
    for j in range(i + 1, len(columns)):

        corr = corr_matrix.iloc[i, j]

        if abs(corr) >= threshold:

            high_corr.append([
                columns[i],
                columns[j],
                corr
            ])

high_corr_df = pd.DataFrame(
    high_corr,
    columns=[
        "Feature 1",
        "Feature 2",
        "Correlation"
    ]
)

high_corr_df.to_csv(
    "reports/high_correlation_features.csv",
    index=False
)

print("=" * 60)
print("CORRELATION ANALYSIS")
print("=" * 60)

print()

print(f"Total Highly Correlated Pairs : {len(high_corr_df)}")

print()

print(high_corr_df.head(20))