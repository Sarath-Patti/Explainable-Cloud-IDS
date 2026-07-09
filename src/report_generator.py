from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


class ReportGenerator:

    def generate(
        self,
        result,
        filename,
        output_path="reports/prediction_report.pdf"
    ):

        styles = getSampleStyleSheet()
        import os

        os.makedirs(
            "reports",
            exist_ok=True
        )
        
        doc = SimpleDocTemplate(output_path)

        elements = []

        elements.append(
            Paragraph(
                "<b>Explainable Cloud IDS</b>",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 0.3 * inch))

        elements.append(
            Paragraph(
                f"<b>Prediction:</b> {result['prediction']}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Confidence:</b> {result['confidence']}%",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Model:</b> {result['model']}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Inference Time:</b> {result['time']} ms",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Features Used:</b> {result['features']}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"<b>Uploaded File:</b> {filename}",
                styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 0.25 * inch))

        elements.append(
            Paragraph(
                "<b>Top SHAP Features</b>",
                styles["Heading2"]
            )
        )

        data = [["Rank", "Feature", "SHAP Value"]]

        for i, feature in enumerate(result["top_features"], start=1):

            data.append(
                [
                    str(i),
                    feature["Feature"],
                    f"{feature['SHAP']:.4f}"
                ]
            )

        table = Table(data)

        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ]
            )
        )

        elements.append(table)

        elements.append(Spacer(1, 0.3 * inch))

        elements.append(
            Paragraph(
                "<b>SHAP Feature Importance</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Image(
                "static/images/shap_bar.png",
                width=6 * inch,
                height=3 * inch
            )
        )

        doc.build(elements)

        return output_path