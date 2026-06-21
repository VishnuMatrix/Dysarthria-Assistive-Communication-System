from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import uuid
import os


def generate_report(data):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    filename = (
        f"report_{uuid.uuid4()}.pdf"
    )

    filepath = os.path.join(
        "reports",
        filename
    )

    doc = SimpleDocTemplate(
        filepath
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Dysarthria Speech Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    for key, value in data.items():

        content.append(
            Paragraph(
                f"<b>{key}</b>: {value}",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 5)
        )

    doc.build(
        content
    )

    return filename