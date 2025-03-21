import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from scripts import file_parser
import config
from llm_api import call_llm

def generate_cover_letter():
    """Generates a tailored cover letter based on the ATS report & optimized CV."""
    ats_report = file_parser.extract_text(config.ATS_REPORT_PATH)
    optimized_cv = file_parser.extract_text(config.OPTIMIZED_CV_PATH)

    user_prompt = config.CREATE_COVERLETTER_PROMPT.format(
        ats_report = ats_report,
        optimized_cv = optimized_cv
    )

    cover_letter = call_llm(config.CREATE_COVERLETTER_SYSTEM_PROMPT, user_prompt, max_tokens=1500)

    with open(config.COVER_LETTER_PATH, "w", encoding="utf-8") as file:
        file.write(cover_letter)
    print(f"✅ Cover Letter saved at: {config.COVER_LETTER_PATH}")

if __name__ == "__main__":
    generate_cover_letter()
