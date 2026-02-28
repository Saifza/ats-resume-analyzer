from app.sections.section_detector import SectionDetector
from app.parsers.text_cleaner import TextCleaner


def test_section_detection():
    sample_text = """
    John Doe
    Email: john@example.com

    SUMMARY
    Software engineer with 5 years experience...

    SKILLS
    Python
    Java
    Docker

    EXPERIENCE
    Worked at XYZ Company...

    EDUCATION
    BSc Computer Science
    """

    cleaned = TextCleaner.clean(sample_text)
    sections = SectionDetector.detect_sections(cleaned)

    assert "summary" in sections
    assert "skills" in sections
    assert "experience" in sections
    assert "education" in sections
