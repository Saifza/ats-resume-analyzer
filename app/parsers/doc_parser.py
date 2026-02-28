from docx import Document


class DOCXParser:
    """
    Extracts raw text from DOCX resumes.
    """

    @staticmethod
    def extract_text(file) -> str:
        """
        Extract text from a DOCX file object.

        Args:
            file: Uploaded file-like object

        Returns:
            str: Extracted raw text
        """
        try:
            document = Document(file)
            paragraphs = [para.text for para in document.paragraphs if para.text.strip()]
            return "\n".join(paragraphs)

        except Exception as e:
            raise ValueError(f"Error reading DOCX file: {e}")
