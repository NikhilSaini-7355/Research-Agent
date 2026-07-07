from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def save_markdown_as_pdf(markdown_text: str, filename: str):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for line in markdown_text.split("\n"):

        line = line.strip()

        if not line:
            continue

        if line.startswith("# "):
            story.append(
                Paragraph(f"<b><font size=18>{line[2:]}</font></b>", styles["Heading1"])
            )

        elif line.startswith("## "):
            story.append(
                Paragraph(f"<b><font size=14>{line[3:]}</font></b>", styles["Heading2"])
            )

        else:
            story.append(
                Paragraph(line, styles["BodyText"])
            )

    doc.build(story)