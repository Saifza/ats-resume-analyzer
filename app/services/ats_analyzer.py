from typing import Dict

from app.parsers.text_cleaner import TextCleaner
from app.sections.section_detector import SectionDetector
from app.keywords.keyword_extractor import KeywordExtractor
from app.keywords.keyword_matcher import KeywordMatcher


class ATSAnalyzer:
    """
    High-level orchestration service for ATS resume analysis.
    """

    def __init__(self, top_n_keywords: int = 20):
        self.keyword_extractor = KeywordExtractor(top_n=top_n_keywords)
        self.keyword_matcher = KeywordMatcher()

    def analyze(self, resume_text: str, job_description: str) -> Dict:

        if not resume_text or not job_description:
            return {
                "error": "Resume text and Job Description are required."
            }

        # 1️⃣ Clean inputs
        cleaned_resume = TextCleaner.clean(resume_text)
        cleaned_jd = TextCleaner.clean(job_description)

        # 2️⃣ Extract JD keywords
        jd_keywords = self.keyword_extractor.extract(cleaned_jd)

        # 3️⃣ Detect Resume Sections
        sections = SectionDetector.detect_sections(cleaned_resume)

        # 4️⃣ Keyword Matching
        match_result = self.keyword_matcher.match(
            cleaned_resume,
            jd_keywords
        )

        # 5️⃣ Build Final Response
        result = {
            "jd_keywords": jd_keywords,
            "matched_keywords": match_result["matched_keywords"],
            "missing_keywords": match_result["missing_keywords"],
            "match_percentage": match_result["match_percentage"],
            "sections_found": list(sections.keys())
        }

        return result
