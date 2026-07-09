import os
import traceback

from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from src.engine import InferenceEngine
from src.report_generator import ReportGenerator

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize components
engine = InferenceEngine()
report_generator = ReportGenerator()

# Store latest prediction for PDF generation
latest_result = None
latest_filename = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def prediction():

    global latest_result
    global latest_filename

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

        result = engine.predict(filepath)

        latest_result = result
        latest_filename = file.filename

        return render_template(
            "result.html",
            result=result,
            filename=file.filename
        )

    except Exception as e:

        print("=" * 80)
        print("ERROR DURING PREDICTION")
        traceback.print_exc()
        print("=" * 80)

        return render_template(
            "result.html",
            error=f"{type(e).__name__}: {e}"
        )


@app.route("/download_report")
def download_report():

    global latest_result
    global latest_filename

    if latest_result is None:
        return "No prediction available. Please upload a file first."

    report_path = report_generator.generate(
        latest_result,
        latest_filename
    )

    return send_file(
        report_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=True
    )