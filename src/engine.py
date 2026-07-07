import joblib

from src.preprocess import preprocess
from src.predictor import predict


class InferenceEngine:
    """
    Handles the complete inference pipeline.
    """

    def __init__(self):
        # Load model once when the application starts
        self.model = joblib.load(
            "models/xgboost_model.pkl"
        )

        # Load label encoder once
        self.encoder = joblib.load(
            "models/label_encoder.pkl"
        )

    def predict(self, csv_path):
        """
        Complete prediction workflow:
        1. Preprocess uploaded CSV
        2. Predict using XGBoost
        3. Convert prediction back to original label
        """

        X = preprocess(csv_path)

        prediction = predict(
            self.model,
            self.encoder,
            X
        )

        return prediction