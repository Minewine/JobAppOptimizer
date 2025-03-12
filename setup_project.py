import os

# Define project structure
project_structure = {
    "JobAppOptimizer": [
        "README.md",
        "README_FR.md",
        "LICENSE",
        "requirements.txt",
        ".gitignore",
        "config/settings.yaml",
        "config/logging_config.json",
        "data/en/sample_cv.pdf",
        "data/en/sample_job_desc.txt",
        "data/en/industry_keywords.json",
        "data/fr/exemple_cv.pdf",
        "data/fr/exemple_description_poste.txt",
        "data/fr/mots_cles_secteur.json",
        "docs/en/setup_guide.md",
        "docs/en/usage_guide.md",
        "docs/en/contributing.md",
        "docs/en/roadmap.md",
        "docs/fr/guide_installation.md",
        "docs/fr/guide_utilisation.md",
        "docs/fr/contribution.md",
        "docs/fr/feuille_route.md",
        "prompts/en/step_1_extraction.md",
        "prompts/en/step_2_gap_analysis.md",
        "prompts/en/step_3_cv_refinement.md",
        "prompts/en/step_4_personalization.md",
        "prompts/en/step_5_cover_letter.md",
        "prompts/en/step_6_review_prep.md",
        "prompts/fr/etape_1_extraction.md",
        "prompts/fr/etape_2_analyse_ecart.md",
        "prompts/fr/etape_3_amelioration_cv.md",
        "prompts/fr/etape_4_personnalisation.md",
        "prompts/fr/etape_5_lettre_motivation.md",
        "prompts/fr/etape_6_revue_prep_entretien.md",
        "scripts/interactive_cv_optimizer.py",
        "scripts/ats_scoring.py",
        "scripts/cv_parser.py",
        "scripts/keyword_extractor.py",
        "scripts/cover_letter_generator.py",
        "scripts/resume_formatter.py",
        "models/ollama_integration.py",
        "models/langchain_prompting.py",
        "models/embeddings/.keep",  # Placeholder for future embeddings
        "api/app.py",
        "api/endpoints/process_cv.py",
        "api/endpoints/score_ats.py",
        "api/endpoints/generate_cover_letter.py",
        "api/endpoints/process_cv_fr.py",
        "api/endpoints/generate_cover_letter_fr.py",
        "web/frontend/.keep",
        "web/backend/.keep",
        "tests/test_ats_scoring.py",
        "tests/test_cv_parser.py",
        "tests/test_cover_letter_generator.py",
        "tests/test_fr_ats_scoring.py",
        "tests/test_fr_cover_letter.py",
    ]
}

# Sample content templates
file_contents = {
    "README.md": "# JobAppOptimizer\n\n🚀 AI-powered tool for optimizing CVs & cover letters.",
    "README_FR.md": "# JobAppOptimizer\n\n🚀 Outil IA pour optimiser CV et lettres de motivation.",
    "LICENSE": "MIT License",
    "requirements.txt": "langchain\nollama\nfastapi\nspacy\nnltk\npandas",
    ".gitignore": "__pycache__/\n*.pyc\nvenv/",
    "config/settings.yaml": "language: en\nats_scoring: enabled",
    "config/logging_config.json": '{ "level": "INFO", "format": "%(asctime)s - %(message)s" }',
    "docs/en/setup_guide.md": "# Setup Guide\n\nSteps to install and use JobAppOptimizer.",
    "docs/fr/guide_installation.md": "# Guide d'installation\n\nÉtapes pour installer et utiliser JobAppOptimizer.",
    "prompts/en/step_1_extraction.md": "# Step 1: Extraction & Insights",
    "prompts/fr/etape_1_extraction.md": "# Étape 1 : Extraction et Analyse",
    "scripts/interactive_cv_optimizer.py": """import os

def load_prompt(step, lang="en"):
    filename = f"prompts/{lang}/{step}.md"
    with open(filename, "r") as file:
        return file.read()

def main():
    print("Welcome to Job Application Optimizer!")
    lang = input("Choose Language / Choisissez la langue (en/fr): ").strip().lower()
    if lang not in ["en", "fr"]:
        print("Invalid choice! Defaulting to English.")
        lang = "en"

    steps = {
        "en": ["step_1_extraction", "step_2_gap_analysis", "step_3_cv_refinement",
               "step_4_personalization", "step_5_cover_letter", "step_6_review_prep"],
        "fr": ["etape_1_extraction", "etape_2_analyse_ecart", "etape_3_amelioration_cv",
               "etape_4_personnalisation", "etape_5_lettre_motivation", "etape_6_revue_prep_entretien"]
    }
    
    for step in steps[lang]:
        input(f"\\nPress Enter to start {step.replace('_', ' ').title()}...")
        print("\\n" + load_prompt(step, lang))
        input("\\nPress Enter to continue...")

if __name__ == "__main__":
    main()
""",
    "api/app.py": """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Job Application Optimizer API"}

@app.get("/process_cv/")
def process_cv():
    return {"message": "Processing CV"}

@app.get("/process_cv_fr/")
def process_cv_fr():
    return {"message": "Traitement du CV"}
"""
}

# Function to create files and directories
def create_project_structure(structure, base_path=""):
    for folder, files in structure.items():
        base_folder = os.path.join(base_path, folder)
        os.makedirs(base_folder, exist_ok=True)
        
        for file in files:
            file_path = os.path.join(base_folder, file)
            if file.endswith("/.keep"):  # Empty folders
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
            else:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(file_contents.get(file, ""))

# Run script to generate the full project structure
if __name__ == "__main__":
    create_project_structure(project_structure)
    print("🚀 Job Application Optimizer project structure created successfully!")
