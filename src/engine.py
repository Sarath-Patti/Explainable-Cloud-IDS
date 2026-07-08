import joblib
import time

from src.preprocess import preprocess
from src.predictor import predict
from src.shap_explainer import SHAPExplainer


class InferenceEngine:

    def __init__(self):

        self.model = joblib.load(
            "models/xgboost_model.pkl"
        )

        self.encoder = joblib.load(
            "models/label_encoder.pkl"
        )

        self.feature_count = len(
            joblib.load("models/selected_features.pkl")
        )

        self.shap = SHAPExplainer()

    def predict(self, csv_path):

        start = time.time()

        X = preprocess(csv_path)

        prediction, confidence = predict(
            self.model,
            self.encoder,
            X
        )

        shap_result = self.shap.explain(
            csv_path
        )

        inference_time = (
            time.time() - start
        ) * 1000

        return {
            "prediction": prediction[0],
            "confidence": round(
                confidence[0] * 100,
                2
            ),
            "features": self.feature_count,
            "model": "XGBoost",
            "time": round(
                inference_time,
                2
            ),
            "top_features": shap_result.to_dict(
                orient="records"
            )
        }