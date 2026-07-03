import pandas as pd
from pathlib import Path


def load_dataset(file_name):

    dataset_path = Path("data/raw") / file_name

    df = pd.read_csv(
        dataset_path,
        low_memory=False
    )

    df.columns = df.columns.str.strip()

    numeric_columns = [
        "Flow Bytes/s",
        "Flow Packets/s"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    return df