from src.shap_explainer import SHAPExplainer

explainer = SHAPExplainer()

result = explainer.explain(
    "data/test/sample_test.csv"
)

print("=" * 60)
print("TOP 5 FEATURES")
print("=" * 60)
print()

print(result)