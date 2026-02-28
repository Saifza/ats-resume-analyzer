import re
from typing import List
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


class KeywordExtractor:
    """
    Extracts top keywords from a job description using
    frequency-based ranking (more stable for single documents).
    """

    def __init__(self, top_n: int = 20):
        self.top_n = top_n
        self.stop_words = set(ENGLISH_STOP_WORDS)

    def _preprocess(self, text: str) -> List[str]:
        text = text.lower()

        # Keep letters, numbers, +, # (important for C++, C#, etc.)
        text = re.sub(r"[^a-z0-9+#\s]", " ", text)
        text = re.sub(r"\s+", " ", text)

        tokens = text.split()

        # Remove stopwords and short tokens
        tokens = [
            word for word in tokens
            if word not in self.stop_words and len(word) > 2
        ]

        return tokens

    def extract(self, job_description: str) -> List[str]:

        if not job_description:
            return []

        tokens = self._preprocess(job_description)

        freq = Counter(tokens)

        most_common = freq.most_common(self.top_n)

        return [word for word, count in most_common]
