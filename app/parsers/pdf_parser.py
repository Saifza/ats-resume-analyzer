import pdfplumber


class PDFParser:
    """
    Extracts raw text from PDF resumes.
    """

    @staticmethod
    def extract_text(file) -> str:
        """
        Extract text from a PDF file object.

        Args:
            file: Uploaded file-like object

        Returns:
            str: Extracted raw text
        """
        text = ""

        try:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

        except Exception as e:
            raise ValueError(f"Error reading PDF file: {e}")

        return text.strip()
