import re
from typing import List, Dict


class KeywordMatcher:
    """
    Matches extracted job description keywords against resume text
    and calculates keyword coverage score.
    """

    def _normalize(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"\s+", " ", text)
        return text

    def _keyword_in_text(self, keyword: str, text: str) -> bool:
        """
        Match whole words only to avoid false positives.
        Example:
        'java' should not match 'javascript'
        """
        pattern = r"\b" + re.escape(keyword.lower()) + r"\b"
        return re.search(pattern, text) is not None

    def match(self, resume_text: str, jd_keywords: List[str]) -> Dict:

        if not resume_text or not jd_keywords:
            return {
                "matched_keywords": [],
                "missing_keywords": [],
                "match_percentage": 0.0
            }

        resume_text = self._normalize(resume_text)

        matched = []
        missing = []

        for keyword in jd_keywords:
            if self._keyword_in_text(keyword, resume_text):
                matched.append(keyword)
            else:
                missing.append(keyword)

        total = len(jd_keywords)
        score = (len(matched) / total) * 100 if total > 0 else 0.0

        return {
            "matched_keywords": matched,
            "missing_keywords": missing,
            "match_percentage": round(score, 2)
        }
