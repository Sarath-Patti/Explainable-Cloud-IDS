import pandas as pd

from sklearn.model_selection import train_test_split

from dataset_loader import load_dataset

import numpy as np

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

# Remove highly correlated features
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

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("=" * 60)
print("TRAIN TEST SPLIT")
print("=" * 60)
print()

print(f"Training Samples : {X_train.shape[0]}")
print(f"Testing Samples  : {X_test.shape[0]}")
print(f"Training Features: {X_train.shape[1]}")
print(f"Testing Features : {X_test.shape[1]}")