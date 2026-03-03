\# 📄 ATS Resume Analyzer

# ATS Resume Analyzer

[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-brightgreen?logo=streamlit)](https://ats-resume-analyzer-qgqhnptduzu4pvu7yfbk3p.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)]()

A Streamlit-based web app that analyzes how well a resume matches a job description using keyword extraction and ATS-style scoring.





\## 🚀 Features



\- Upload Resume (PDF or DOCX)

\- Paste Resume Text (fallback option)

\- Extract job description keywords

\- Match resume against JD keywords

\- Visual keyword tags (matched \& missing)

\- ATS Match Score with progress bar

\- Downloadable PDF analysis report



\## 🏗️ Architecture



\- Clean modular structure

\- Service layer orchestration

\- Resume parsing layer

\- Keyword extraction \& matching engine

\- Streamlit frontend



\## 🛠️ Tech Stack



\- Python

\- Streamlit

\- pdfplumber

\- python-docx

\- reportlab



\## ▶️ Run Locally



```bash

pip install -r requirements.txt

streamlit run app.py

