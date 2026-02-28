import streamlit as st
from app.services.ats_analyzer import ATSAnalyzer
from app.parsers.resume_parser import ResumeParser
from app.services.report_generator import ReportGenerator


st.set_page_config(
    page_title="ATS Resume Analyzer",
    layout="wide"
)

st.title("📄 ATS Resume Analyzer")
st.markdown("Analyze how well your resume matches a job description.")

# Layout
col1, col2 = st.columns(2)

# ===============================
# LEFT COLUMN — RESUME INPUT
# ===============================
with col1:
    st.subheader("Resume Input")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF or DOCX)",
        type=["pdf", "docx"]
    )

    resume_text = ""

    if uploaded_file is not None:
        try:
            resume_text = ResumeParser.parse(
                uploaded_file,
                uploaded_file.name
            )
            st.success("Resume successfully parsed from file.")
        except Exception as e:
            st.error(f"Error parsing file: {e}")

    st.markdown("**OR**")

    manual_resume = st.text_area(
        "Paste Resume Text",
        height=250
    )

    if manual_resume.strip():
        resume_text = manual_resume


# ===============================
# RIGHT COLUMN — JOB DESCRIPTION
# ===============================
with col2:
    st.subheader("Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=400
    )


# ===============================
# ANALYZE BUTTON
# ===============================
if st.button("Analyze Resume"):

    if not resume_text.strip() or not job_description.strip():
        st.warning("Please provide both resume and job description.")
    else:
        analyzer = ATSAnalyzer(top_n_keywords=20)
        result = analyzer.analyze(resume_text, job_description)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success("Analysis Complete!")

            score = result["match_percentage"]

            # ===============================
            # SCORE DISPLAY
            # ===============================
            st.subheader("ATS Match Score")
            st.progress(score / 100)
            st.metric("Match Percentage", f"{score}%")

            # ===============================
            # SECTIONS
            # ===============================
            st.subheader("Sections Detected in Resume")
            if result["sections_found"]:
                st.write(", ".join(result["sections_found"]))
            else:
                st.write("No standard sections detected.")

            # ===============================
            # MATCHED KEYWORDS
            # ===============================
            st.subheader("Matched Keywords")

            if result["matched_keywords"]:
                matched_html = ""
                for kw in result["matched_keywords"]:
                    matched_html += f"""
                    <span style="
                        background-color:#d4edda;
                        color:#155724;
                        padding:6px 10px;
                        margin:4px;
                        border-radius:20px;
                        display:inline-block;
                        font-size:14px;">
                        {kw}
                    </span>
                    """
                st.markdown(matched_html, unsafe_allow_html=True)
            else:
                st.write("No matching keywords found.")

            # ===============================
            # MISSING KEYWORDS
            # ===============================
            st.subheader("Missing Keywords")

            if result["missing_keywords"]:
                missing_html = ""
                for kw in result["missing_keywords"]:
                    missing_html += f"""
                    <span style="
                        background-color:#f8d7da;
                        color:#721c24;
                        padding:6px 10px;
                        margin:4px;
                        border-radius:20px;
                        display:inline-block;
                        font-size:14px;">
                        {kw}
                    </span>
                    """
                st.markdown(missing_html, unsafe_allow_html=True)
            else:
                st.write("No missing keywords — great match!")

            # ===============================
            # DOWNLOAD REPORT
            # ===============================
            st.subheader("Download Analysis Report")

            file_path = ReportGenerator.generate_report(result)

            with open(file_path, "rb") as f:
                st.download_button(
                    label="Download PDF Report",
                    data=f,
                    file_name="ats_report.pdf",
                    mime="application/pdf"
                )
