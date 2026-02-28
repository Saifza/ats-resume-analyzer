from app.keywords.keyword_extractor import KeywordExtractor


def test_keyword_extraction():
    jd = """
    We are looking for a Python developer with experience in Django,
    REST APIs, Docker, AWS, and CI/CD pipelines.
    """

    extractor = KeywordExtractor(top_n=10)
    keywords = extractor.extract(jd)

    assert any("python" in kw for kw in keywords)
    assert any("django" in kw for kw in keywords)
   
