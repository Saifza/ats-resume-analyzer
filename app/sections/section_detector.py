import re
from typing import Dict


class SectionDetector:
    """
    Detects major resume sections using regex-based header matching.
    """

    SECTION_HEADERS = {
        "summary": [
            "summary",
            "professional summary",
            "profile",
            "career summary",
        ],
        "skills": [
            "skills",
            "technical skills",
            "core competencies",
            "key skills",
        ],
        "experience": [
            "experience",
            "work experience",
            "professional experience",
            "employment history",
        ],
        "education": [
            "education",
            "academic background",
            "educational qualifications",
        ],
        "projects": [
            "projects",
            "personal projects",
            "academic projects",
        ],
        "certifications": [
            "certifications",
            "licenses",
            "certificates",
        ],
    }

    @classmethod
    def detect_sections(cls, text: str) -> Dict[str, str]:
        """
        Detect sections from resume text.

        Args:
            text (str): Cleaned resume text

        Returns:
            Dict[str, str]: Section name -> section content
        """

        if not text:
            return {}

        text_lower = text.lower()

        # Find all header matches with positions
        matches = []

        for section, headers in cls.SECTION_HEADERS.items():
            for header in headers:
                pattern = rf"\n?\b{re.escape(header)}\b\s*\n"
                for match in re.finditer(pattern, text_lower):
                    matches.append(
                        {
                            "section": section,
                            "start": match.start(),
                            "end": match.end(),
                        }
                    )

        # Sort headers by position
        matches = sorted(matches, key=lambda x: x["start"])

        sections = {}

        # Extract content between headers
        for i in range(len(matches)):
            current = matches[i]
            start = current["end"]

            if i + 1 < len(matches):
                end = matches[i + 1]["start"]
            else:
                end = len(text)

            content = text[start:end].strip()
            sections[current["section"]] = content

        return sections
