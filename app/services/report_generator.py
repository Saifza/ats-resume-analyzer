from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable
from reportlab.lib.styles import ListStyle
from reportlab.lib.enums import TA_LEFT


class ReportGenerator:

    @staticmethod
    def generate_report(result: dict, filename="ats_report.pdf"):

        doc = SimpleDocTemplate(filename)
        elements = []

        styles = getSampleStyleSheet()

        elements.append(Paragraph("<b>ATS Resume Analysis Report</b>", styles["Title"]))
        elements.append(Spacer(1, 0.3 * inch))

        elements.append(Paragraph(f"<b>Match Percentage:</b> {result['match_percentage']}%", styles["Normal"]))
        elements.append(Spacer(1, 0.2 * inch))

        elements.append(Paragraph("<b>Matched Keywords:</b>", styles["Heading2"]))
        elements.append(Spacer(1, 0.1 * inch))

        matched_list = [ListItem(Paragraph(kw, styles["Normal"])) for kw in result["matched_keywords"]]
        elements.append(ListFlowable(matched_list, bulletType='bullet'))

        elements.append(Spacer(1, 0.3 * inch))

        elements.append(Paragraph("<b>Missing Keywords:</b>", styles["Heading2"]))
        elements.append(Spacer(1, 0.1 * inch))

        missing_list = [ListItem(Paragraph(kw, styles["Normal"])) for kw in result["missing_keywords"]]
        elements.append(ListFlowable(missing_list, bulletType='bullet'))

        doc.build(elements)

        return filename
