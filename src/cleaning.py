from pathlib import Path

import numpy as np
import pandas as pd

from dataset_loader import load_dataset
from preprocessing import clean_column_names


def replace_infinite_values(df):
    """
    Replace positive and negative infinity with NaN.
    """
    infinite_count = df.isin([np.inf, -np.inf]).sum().sum()

    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    print(f"Infinite values replaced      : {infinite_count}")

    return df


def remove_missing_values(df):
    """
    Remove rows containing missing values.
    """
    before = len(df)

    df = df.dropna()

    removed = before - len(df)

    print(f"Rows removed (Missing Values) : {removed}")

    return df


def remove_duplicate_rows(df):
    """
    Remove duplicate rows.
    """
    before = len(df)

    df = df.drop_duplicates()

    removed = before - len(df)

    print(f"Rows removed (Duplicates)     : {removed}")

    return df


def save_clean_dataset(df):
    """
    Save the cleaned dataset.
    """
    output_path = Path("data/processed/cleaned_ddos.csv")

    df.to_csv(output_path, index=False)

    print(f"\nClean dataset saved to:")
    print(output_path)


def main():

    print("=" * 60)
    print("DATA CLEANING PIPELINE")
    print("=" * 60)

    df = load_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print(f"\nOriginal Shape : {df.shape}")

    df = clean_column_names(df)

    df = replace_infinite_values(df)

    df = remove_missing_values(df)

    df = remove_duplicate_rows(df)

    print(f"\nFinal Shape : {df.shape}")

    save_clean_dataset(df)


if __name__ == "__main__":
    main()