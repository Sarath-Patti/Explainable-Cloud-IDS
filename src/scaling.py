import pandas as pd

from sklearn.preprocessing import StandardScaler

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

# Remove highly correlated features
corr_matrix = X.corr().abs()

upper = corr_matrix.where(
    __import__("numpy").triu(
        __import__("numpy").ones(corr_matrix.shape),
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

# Scale features
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

scaled_df = pd.DataFrame(
    X_scaled,
    columns=X.columns
)

scaled_df["Label"] = y.values

scaled_df.to_csv(
    "data/processed/scaled_ddos.csv",
    index=False
)

print("=" * 60)
print("FEATURE SCALING")
print("=" * 60)
print()
print(f"Features Scaled : {X.shape[1]}")
print(f"Dataset Shape   : {scaled_df.shape}")