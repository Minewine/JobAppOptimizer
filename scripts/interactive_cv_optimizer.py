import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from scripts import file_parser

import config
from config import get_cv_customization_prompt  # Import the new prompt function
from llm_api import call_llm  # Import the reusable function

def customize_cv_with_llm(cv_text, ats_report_text):
    """Customizes the CV based on the ATS report using LLM."""
    if not config.OPENROUTER_API_KEY:
        raise ValueError("❌ OpenRouter API key is missing. Set it in config.py.")

    user_prompt = get_cv_customization_prompt(cv_text, ats_report_text)
    system_message = config.SYSTEM_MESSAGE
    return call_llm(user_prompt, system_message, max_tokens=8000)

def process_cv_customization():
    """Processes CV & ATS report to generate a customized CV."""
    
    # Extract text from the original CV and ATS report
    cv_text = file_parser.extract_text(config.CV_LOCATION)
    ats_report_text = file_parser.extract_text(config.ATS_REPORT_PATH)

    # Generate the customized CV
    customized_cv = customize_cv_with_llm(cv_text, ats_report_text)

    # Save customized CV to markdown
    customized_cv_path = config.OPTIMIZED_CV_PATH
    with open(customized_cv_path, "w", encoding="utf-8") as file:
        file.write(customized_cv)
    print(f"✅ Customized CV saved to {customized_cv_path}")

if __name__ == "__main__":
    process_cv_customization()