from app.parsers.pdf_parser import PDFParser
from app.parsers.docx_parser import DOCXParser
from app.parsers.text_cleaner import TextCleaner


def test_pdf():
    with open("sample_data/sample_resume.pdf", "rb") as f:
        raw = PDFParser.extract_text(f)
        clean = TextCleaner.clean(raw)
        print(clean[:500])


def test_docx():
    with open("sample_data/sample_resume.docx", "rb") as f:
        raw = DOCXParser.extract_text(f)
        clean = TextCleaner.clean(raw)
        print(clean[:500])


if __name__ == "__main__":
    test_pdf()
