import joblib
import pandas as pd

# Load selected features
selected_features = joblib.load(
    "models/selected_features.pkl"
)

# Load original dataset
df = pd.read_csv(
    "data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

# Clean column names
df.columns = df.columns.str.strip()

# Keep only the selected 43 features
df = df[selected_features]

# First 100 rows
df = df.head(100)

# Save
df.to_csv(
    "data/test/sample_test.csv",
    index=False
)

print("=" * 60)
print("TEST FILE CREATED")
print("=" * 60)
print()

print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

print()

print("Saved to:")
print("data/test/sample_test.csv")