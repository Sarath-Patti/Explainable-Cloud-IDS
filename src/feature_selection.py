import pandas as pd
import numpy as np
from dataset_loader import load_dataset

# Load dataset
df = load_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove invalid values
df.replace([float("inf"), float("-inf")], pd.NA, inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Separate features and target
X = df.drop(columns=["Label"])
y = df["Label"]

# Compute correlation matrix
corr_matrix = X.corr().abs()

# Keep only upper triangle
upper = corr_matrix.where(
    np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
)
# Identify highly correlated features
threshold = 0.90

to_drop = [
    column
    for column in upper.columns
    if any(upper[column] > threshold)
]

# Remove redundant features
X_reduced = X.drop(columns=to_drop)

# Combine with target
reduced_df = pd.concat([X_reduced, y], axis=1)

# Save reduced dataset
reduced_df.to_csv(
    "data/processed/reduced_ddos.csv",
    index=False
)

print("=" * 60)
print("FEATURE SELECTION")
print("=" * 60)

print()

print(f"Original Features : {X.shape[1]}")

print(f"Removed Features  : {len(to_drop)}")

print(f"Remaining Features: {X_reduced.shape[1]}")

print()

print("Removed Features")

for feature in to_drop:
    print("-", feature)