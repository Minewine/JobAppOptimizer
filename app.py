import os
import streamlit as st
import config

def load_markdown_file(file_path):
    """Loads a markdown file if it exists, otherwise returns a warning."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return None

st.title("📄 ATS Job Application Report")

# Load ATS Report
ats_report = load_markdown_file(config.ATS_REPORT_PATH)

if ats_report:
    st.markdown(ats_report)  # ✅ This will render Markdown properly
else:
    st.warning("⚠️ ATS report not found. Please generate it first.")

# Load Optimized CV
optimized_cv = load_markdown_file(config.OPTIMIZED_CV_PATH)

st.title("📑 Optimized CV")

if optimized_cv:
    st.markdown(optimized_cv)  # ✅ Renders Markdown properly
else:
    st.warning("⚠️ Optimized CV not found. Please generate it first.")