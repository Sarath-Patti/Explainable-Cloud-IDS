import joblib
import pandas as pd
import shap
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os

from src.preprocess import preprocess


class SHAPExplainer:
    """
    Generates SHAP explanations for predictions.
    """

    def __init__(self):

        self.model = joblib.load(
            "models/xgboost_model.pkl"
        )

        self.selected_features = joblib.load(
            "models/selected_features.pkl"
        )

        self.explainer = shap.TreeExplainer(
            self.model
        )

    def explain(self, csv_path):

        X = preprocess(csv_path)

        shap_values = self.explainer.shap_values(X)

        sample = pd.DataFrame(
            {
                "Feature": self.selected_features,
                "SHAP": abs(shap_values[0])
            }
        )

        sample = sample.sort_values(
            by="SHAP",
            ascending=False
        )

        top5 = sample.head(5)

        # -----------------------------------------
        # Generate SHAP Bar Chart
        # -----------------------------------------

        os.makedirs(
            "static/images",
            exist_ok=True
        )

        plt.figure(figsize=(8,4))

        plt.barh(
            top5["Feature"][::-1],
            top5["SHAP"][::-1]
        )

        plt.xlabel("Mean |SHAP Value|")

        plt.title(
            "Top Contributing Features"
        )

        plt.tight_layout()

        plt.savefig(
            "static/images/shap_bar.png"
        )

        plt.close()

        return top5