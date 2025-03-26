import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from scripts import file_parser

import config 
from config import get_analysis_prompt
from llm_api import call_llm  # Import the reusable function

def extract_keywords_with_llm(cv_text, job_desc_text):
    """Extracts job-related insights from a CV and Job Description."""
    
    if not config.OPENROUTER_API_KEY:
        raise ValueError("❌ OpenRouter API key is missing. Set it in config.py.")

    user_prompt = get_analysis_prompt(job_desc_text, cv_text)
    system_message = config.SYSTEM_MESSAGE
    return call_llm(user_prompt, system_message, max_tokens=8000)

def process_keywords():
    """Processes CV & job description using LLM-powered extraction."""
    
    cv_text = file_parser.extract_text(config.CV_LOCATION)
    job_desc_text = file_parser.extract_text(config.JOB_DESC_LOCATION)

    structured_insights = extract_keywords_with_llm(cv_text, job_desc_text)

    # Save ATS insights to markdown
    with open(config.ATS_REPORT_PATH, "w", encoding="utf-8") as file:
        file.write(structured_insights)
    print(f"✅ ATS insights saved to {config.ATS_REPORT_PATH}")

if __name__ == "__main__":
    process_keywords()
