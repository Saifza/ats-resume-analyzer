from app.keywords.keyword_matcher import KeywordMatcher


def test_keyword_matching():

    resume = """
    Experienced Python developer with Django and AWS experience.
    Built REST APIs and deployed using Docker.
    """

    jd_keywords = ["python", "django", "aws", "docker", "kubernetes"]

    matcher = KeywordMatcher()
    result = matcher.match(resume, jd_keywords)

    assert "python" in result["matched_keywords"]
    assert "kubernetes" in result["missing_keywords"]
    assert result["match_percentage"] > 0
