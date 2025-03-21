import sqlite3
from pathlib import Path
import sys
import os
import requests
import json


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from scripts import file_parser
import config
from llm_api import call_llm

# Database path
DB_PATH = Path(__file__).parent / "ats_experiences.db"

def get_user_experience(username):
    """Fetch job experiences for a given username from the database and return as a dictionary."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT company, years_worked, experience_text FROM job_experiences WHERE user_id = ?;
    """, (username,))
    
    experiences = cursor.fetchall()
    conn.close()

    # Format data into a dictionary
    user_data = {
        "name": username,
        "experiences": [
            {
                "company": exp[0],
                "years_worked": exp[1],
                "experience_text": exp[2]
            }
            for exp in experiences
        ]
    }

    return user_data

# Example calls
#get_user_experience("Nicholas")

#Get the job description
job_desc_text = file_parser.extract_text(config.JOB_DESC_LOCATION)



def craft_cv_prompt(user_data, job_desc_text):
    """Generates a structured prompt for the LLM to create a CV."""
    return f"""
You are an AI-powered career assistant specializing in crafting professional CVs. Your task is to create a well-structured, ATS-friendly CV tailored to the provided job description. 

## **Instructions**
1. Use the provided user experiences to highlight relevant skills and achievements.
2. Match the content to the job description, ensuring strong alignment.
3. Format the CV professionally with clear sections:
   - **Contact Information** (Use placeholders if missing)
   - **Professional Summary** (Concise introduction highlighting strengths)
   - **Work Experience** (Detailed descriptions based on past roles)
   - **Skills** (List of key skills extracted from experience)
   - **Education** (If available)
4. Ensure the CV sounds natural and professional while remaining truthful.
5. Output the CV in Markdown format.

## **User Experience Data**
{json.dumps(user_data, indent=4)}

## **Job Description**
{job_desc_text}

Generate a **professionally formatted CV** based on the information above.
"""


def generate_cv(username, job_desc_text):
    """Fetches user experience, crafts a CV prompt, calls LLM, and saves the CV."""
    user_data = get_user_experience(username)
    
    if not user_data["experiences"]:
        print(f"⚠️ No experience data found for user: {username}")
        return

    system_message = config.SYSTEM_MESSAGE
    user_prompt = craft_cv_prompt(user_data, job_desc_text)
    cv_text = call_llm(user_prompt, system_message, max_tokens=8000)
    

    if cv_text:
        cv_path = Path(__file__).parent / f"{username}_generated_cv.md"
        with open(cv_path, "w", encoding="utf-8") as f:
            f.write(cv_text)
        print(f"✅ CV generated and saved to {cv_path}")
    else:
        print("❌ Failed to generate CV.")


generate_cv("Ann", job_desc_text)