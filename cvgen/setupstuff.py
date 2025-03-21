import sqlite3
import json
from pathlib import Path

# Set database path in the current directory
DB_PATH = Path(__file__).parent / "ats_experiences.db"

def create_table():
    """Creates the job experiences table in SQLite (stored in the current directory)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_experiences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        company TEXT NOT NULL,
        years_worked TEXT NOT NULL,
        experience_text TEXT NOT NULL,
        vector_embedding TEXT  -- Store as JSON string
    );
    """)
    
    conn.commit()
    conn.close()

import sqlite3
import json
import random
from pathlib import Path
from langchain.embeddings import HuggingFaceEmbeddings

# Database path (stored in the current directory)
DB_PATH = Path(__file__).parent / "ats_experiences.db"

# Initialize embedding model (optional)
embedding_model = HuggingFaceEmbeddings()

def generate_experience_text(company, years, job_role):
    """Generates a natural, casual job experience text for someone with less expertise."""
    experiences = [
        f"I worked at {company} from {years}, mostly just helping out with whatever needed to be done. At first, I didn’t really know much, so I spent a lot of time asking questions and watching how others did things. I helped fix small bugs, but a lot of the time, I wasn’t even sure what I was fixing. Eventually, I got better at reading error messages, which made troubleshooting a little easier.",
        
        f"At {company}, I spent {years} doing basic tasks. I wasn’t the best at coding, so I mostly worked on testing things and making sure everything looked okay before we released updates. I remember once, I broke something important and had to wait for a senior dev to show me how to fix it. I learned a lot from mistakes like that, even though it was stressful at the time.",
        
        f"When I worked at {company} between {years}, my main job was to help with anything that needed extra hands. Some days, I was running test cases, other days, I was trying to update documentation. I wanted to do more programming, but honestly, I struggled with it. I did manage to write a small script once, but I mostly just copied and pasted from Google until it worked.",
        
        f"I was at {company} from {years}, working as a junior on the team. I didn’t really know what I was doing half the time, but I tried to keep up. My main job was checking logs and reporting issues. I asked a lot of questions and slowly started understanding how things worked. I also got to help set up some automated reports, though someone else had to double-check my work.",
        
        f"I worked at {company} during {years}, mostly doing small tasks. I spent a lot of time trying to fix things that I didn’t fully understand. Sometimes I got lucky and solved an issue quickly, but other times, I had to wait for someone more experienced to explain it to me. I learned that troubleshooting is mostly just trial and error—and a lot of Googling.",
        
        f"At {company}, I started out not really knowing what I was doing. During {years}, I worked on small projects, mostly just editing code other people wrote. I once tried to fix a bug but ended up making it worse. After that, I got better at testing changes before pushing them live. I also helped organize some files to make things easier to find, which wasn’t hard but made a difference.",
        
        f"I spent {years} at {company}, working in IT support. Most of my job was answering questions and trying to fix things that weren’t working. I wasn’t the best at explaining technical stuff, but I got better over time. I also had to reset a lot of passwords for people who kept forgetting them. I eventually helped create a small guide so we didn’t have to answer the same questions over and over.",
        
        f"At {company}, I was mostly handling small issues that popped up. During {years}, I did a lot of testing, making sure features worked before they were released. One time, I caught a pretty big mistake before it went live, and that felt good. I wasn’t very confident in my coding, but I tried to learn from the senior engineers whenever I could.",
        
        f"I worked at {company} for {years}, mostly doing basic troubleshooting. I spent a lot of time trying to figure out why things were broken, and sometimes I actually found the problem before anyone else. I also helped set up a few accounts and did some basic data entry. It wasn’t super exciting, but it helped me understand how things worked behind the scenes.",
        
        f"When I was at {company} from {years}, my job was mostly to assist wherever I was needed. I remember struggling with one task for hours, only to find out I had just missed a small setting. Stuff like that happened a lot, but I slowly got better. I also helped organize some documents, which wasn’t technical but was something that needed to be done."
    ]
    
    return random.choice(experiences)  # Pick a different experience each time

def populate_database():
    """Populates the database with two users, each having five job experiences."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    users = ["Ann", "Nicholas"]
    companies = ["Google", "Microsoft", "Amazon", "OpenAI", "Tesla"]
    years_list = ["2015-2018", "2018-2020", "2020-2022", "2016-2019", "2019-2021"]
    job_roles = ["Junior Developer", "IT Support", "QA Tester", "Help Desk Technician", "Technical Assistant"]

    for user in users:
        for i in range(5):
            company = companies[i]
            years = years_list[i]
            job_role = job_roles[i]
            experience_text = generate_experience_text(company, years, job_role)  # Natural explanation

            # Generate AI embedding (optional for semantic search)
            embedding = embedding_model.embed_query(experience_text)
            embedding_json = json.dumps(embedding)

            # Insert into SQLite
            cursor.execute("""
            INSERT INTO job_experiences (user_id, company, years_worked, experience_text, vector_embedding) 
            VALUES (?, ?, ?, ?, ?);
            """, (user, company, years, experience_text, embedding_json))

    conn.commit()
    conn.close()
    print("✅ Database populated with casual job descriptions.")



