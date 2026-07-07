def predict(model, encoder, X):

    prediction = model.predict(X)

    prediction = encoder.inverse_transform(
        prediction
    )

    return prediction