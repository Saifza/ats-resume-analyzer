import re


class TextCleaner:
    """
    Cleans and normalizes extracted resume text.
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean resume text.

        Steps:
        - Normalize whitespace
        - Remove excessive line breaks
        - Remove non-standard characters
        - Standardize spacing
        """

        if not text:
            return ""

        # Normalize unicode quotes/dashes
        text = text.replace("–", "-").replace("—", "-")

        # Remove non-printable characters
        text = re.sub(r"[^\x00-\x7F]+", " ", text)

        # Normalize multiple newlines
        text = re.sub(r"\n\s*\n+", "\n\n", text)

        # Normalize multiple spaces
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()
