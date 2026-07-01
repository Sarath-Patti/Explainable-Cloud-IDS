import pandas as pd
from pathlib import Path


def load_dataset(file_name):
    """
    Load a dataset from the data/raw folder.

    Parameters:
        file_name (str): Name of the CSV file.

    Returns:
        pandas.DataFrame
    """

    dataset_path = Path("data/raw") / file_name

    df = pd.read_csv(dataset_path)

    return df