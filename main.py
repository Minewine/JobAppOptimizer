import os
import sys
import subprocess
import logging
from scripts.keyword_extractor import process_keywords
from scripts.interactive_cv_optimizer import generate_ats_cv
from scripts.cover_letter_generator import generate_cover_letter
import config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def validate_file(file_path, description):
    """Validate that a file exists."""
    if not os.path.exists(file_path):
        logger.error(f"{description} not found at {file_path}")
        sys.exit(1)

def run_streamlit_app(app_path):
    """Run the Streamlit app."""
    try:
        logger.info(f"Launching Streamlit app: {app_path}")
        subprocess.run(["streamlit", "run", app_path], check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to launch Streamlit app: {e}")
        sys.exit(1)
    except FileNotFoundError:
        logger.error("Streamlit not installed or not found in PATH. Install it with 'pip install streamlit'.")
        sys.exit(1)

def main():
    # Validate input files using config values
    validate_file(config.CV_LOCATION, "CV file")
    validate_file(config.JOB_DESC_LOCATION, "Job description file")
    streamlit_app_path = f"{config.BASE_DIR}/app.py"  # Assuming app.py is in BASE_DIR
    validate_file(streamlit_app_path, "Streamlit app file")
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR)
        logger.info(f"Created output directory: {config.OUTPUT_DIR}")

    # Step 1: Generate ATS Report
    logger.info("Starting ATS keyword extraction...")
    try:
        process_keywords()
        logger.info("ATS report generation completed.")
        validate_file(config.ATS_REPORT_PATH, "ATS report")
    except Exception as e:
        logger.error(f"ATS report generation failed: {e}")
        sys.exit(1)

    # Step 2: Generate Optimized CV
    logger.info("Starting CV optimization...")
    try:
        generate_ats_cv()
        logger.info("CV optimization completed.")
        validate_file(config.OPTIMIZED_CV_PATH, "Optimized CV")
    except Exception as e:
        logger.error(f"CV optimization failed: {e}")
        sys.exit(1)

    # Step 3: Generate Cover Letter
    logger.info("Starting cover letter generation...")
    try:
        generate_cover_letter()
        logger.info("Cover letter generation completed.")
        validate_file(config.COVER_LETTER_PATH, "Cover letter")
    except Exception as e:
        logger.error(f"Cover letter generation failed: {e}")
        sys.exit(1)

    # Step 4: Launch Streamlit App
    logger.info("All document generation steps completed successfully.")
    run_streamlit_app(streamlit_app_path)

if __name__ == "__main__":
    main()