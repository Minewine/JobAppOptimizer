import os

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
        input(f"\nPress Enter to start {step.replace('_', ' ').title()}...")
        print("\n" + load_prompt(step, lang))
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
