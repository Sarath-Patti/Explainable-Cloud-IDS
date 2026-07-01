from dataset_loader import load_dataset

def clean_column_names(df):
    """
    Remove leading and trailing spaces from all column names.
    """
    df.columns = df.columns.str.strip()
    return df


if __name__ == "__main__":
    df = load_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print("=" * 60)
    print("BEFORE CLEANING")
    print("=" * 60)
    print(df.columns.tolist())

    df = clean_column_names(df)

    print("\n" + "=" * 60)
    print("AFTER CLEANING")
    print("=" * 60)
    print(df.columns.tolist())