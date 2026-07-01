from dataset_loader import load_dataset
from preprocessing import clean_column_names

df = load_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

df = clean_column_names(df)

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

rows, columns = df.shape

print(f"Rows    : {rows}")
print(f"Columns : {columns}")

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing_values = df.isnull().sum()

missing_columns = missing_values[missing_values > 0]

print(missing_columns)

print(f"\nTotal Missing Values : {missing_values.sum()}")
total_missing = missing_values.sum()

print(f"\nTotal Missing Values : {total_missing}")

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()

print(f"Duplicate Rows : {duplicates}")

print("\n" + "=" * 60)
print("LABEL DISTRIBUTION")
print("=" * 60)

print(df["Label"].value_counts())

import numpy as np

print("\n" + "=" * 60)
print("INFINITE VALUES")
print("=" * 60)

infinite_values = df.isin([np.inf, -np.inf]).sum()

infinite_columns = infinite_values[infinite_values > 0]

print(infinite_columns)

print(f"\nTotal Infinite Values : {infinite_values.sum()}")