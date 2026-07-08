import numpy as np


def predict(model, encoder, X):
    """
    Predict the class label and confidence score.
    """

    prediction = model.predict(X)

    probabilities = model.predict_proba(X)

    confidence = np.max(probabilities, axis=1)

    prediction = encoder.inverse_transform(prediction)

    return prediction, confidence