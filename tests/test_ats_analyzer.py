from app.services.ats_analyzer import ATSAnalyzer


def test_ats_analysis():

    resume = """
    John Doe

    SUMMARY
    Python developer with Django experience.

    SKILLS
    Python, AWS, Docker

    EXPERIENCE
    Built REST APIs.
    """

    jd = """
    Looking for Python developer with AWS and Docker experience.
    Experience with Kubernetes is a plus.
    """

    analyzer = ATSAnalyzer(top_n_keywords=10)
    result = analyzer.analyze(resume, jd)

    assert "python" in result["matched_keywords"]
    assert "kubernetes" in result["missing_keywords"]
    assert result["match_percentage"] > 0
    assert "skills" in result["sections_found"]
