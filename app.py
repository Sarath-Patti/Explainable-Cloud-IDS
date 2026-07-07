import os

from flask import (
    Flask,
    render_template,
    request
)

from src.engine import InferenceEngine

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create the inference engine only once
engine = InferenceEngine()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def prediction():

    if "file" not in request.files:
        return "No file uploaded."

    file = request.files["file"]

    if file.filename == "":
        return "No file selected."

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    try:

        prediction = engine.predict(filepath)

        return render_template(
            "result.html",
            prediction=prediction[0]
        )

    except Exception as e:

        return render_template(
            "result.html",
            prediction=None,
            error=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)