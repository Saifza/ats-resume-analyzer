import pdfplumber
from docx import Document
from typing import Optional


class ResumeParser:
    """
    Handles resume file parsing for PDF and DOCX formats.
    """

    @staticmethod
    def parse_pdf(file) -> str:
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        return text.strip()

    @staticmethod
    def parse_docx(file) -> str:
        doc = Document(file)
        paragraphs = [para.text for para in doc.paragraphs]
        return "\n".join(paragraphs).strip()

    @staticmethod
    def parse(file, filename: str) -> Optional[str]:
        filename = filename.lower()

        if filename.endswith(".pdf"):
            return ResumeParser.parse_pdf(file)

        elif filename.endswith(".docx"):
            return ResumeParser.parse_docx(file)

        else:
            raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
