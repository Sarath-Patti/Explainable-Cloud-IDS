import joblib
import pandas as pd

# ============================================================
# LOAD PREPROCESSING ARTIFACTS
# ============================================================

scaler = joblib.load(
    "models/scaler.pkl"
)

selected_features = joblib.load(
    "models/selected_features.pkl"
)


# ============================================================
# PREPROCESS FUNCTION
# ============================================================

def preprocess(csv_path):
    """
    Preprocess the uploaded CSV file using the
    same pipeline as the training phase.
    """

    # Load CSV
    df = pd.read_csv(csv_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Replace infinite values
    df.replace(
        [float("inf"), float("-inf")],
        pd.NA,
        inplace=True
    )

    # Remove rows containing missing values
    df.dropna(inplace=True)

    # --------------------------------------------------------
    # Validate required features
    # --------------------------------------------------------

    missing_features = [
        feature
        for feature in selected_features
        if feature not in df.columns
    ]

    if missing_features:
        raise ValueError(
            "Uploaded CSV is missing the following required columns:\n\n"
            + "\n".join(missing_features)
        )

    # Keep only the selected features
    df = df[selected_features]

    # Scale features
    X = scaler.transform(df)

    return X