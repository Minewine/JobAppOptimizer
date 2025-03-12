# 📌 Optimiseur de Candidature  
🚀 **Un outil IA pour optimiser les CV et lettres de motivation pour les ATS et les recruteurs**  

## 📖 Aperçu  
**Optimiseur de Candidature** aide les chercheurs d’emploi à **améliorer leurs CV et lettres de motivation** afin d’augmenter leurs chances de passer les **Systèmes de Suivi des Candidatures (ATS)** et d’attirer l’attention des recruteurs. Ce projet propose **des invites IA guidées étape par étape**, une analyse ATS et des **suggestions d’amélioration de contenu** pour renforcer les candidatures.  

## ✨ Fonctionnalités  
- ✅ **Optimisation ATS** – Améliorez les CV pour réussir les filtres ATS.  
- ✅ **Améliorations par l’IA** – Génère des suggestions de mots-clés adaptés aux ATS.  
- ✅ **Invites IA Guidées** – Guide les utilisateurs à travers le processus de candidature.  
- ✅ **Personnalisation des Lettres de Motivation** – Crée des lettres percutantes et sur mesure.  
- ✅ **Analyse des Lacunes** – Identifie les compétences manquantes, les formulations faibles et les problèmes de mise en forme.  
- ✅ **Support Bilingue** – Versions en anglais et en français disponibles.  
- ✅ **Intégration CLI & API (Futur)** – Automatise le processus via un outil en ligne de commande et une API.  

## 📂 Structure du Projet  
JobAppOptimizer/
├── README_FR.md
├── LICENSE # Licence MIT recommandée
├── requirements.txt
├── prompts/
│ ├── en/ # Invites en anglais
│ │ ├── step_1_extraction.md
│ │ ├── step_2_gap_analysis.md
│ │ ├── step_3_cv_refinement.md
│ │ ├── step_4_personalization.md
│ │ ├── step_5_cover_letter.md
│ │ ├── step_6_review_prep.md
│ ├── fr/ # Invites en français
│ │ ├── etape_1_extraction.md
│ │ ├── etape_2_analyse_ecart.md
│ │ ├── etape_3_amelioration_cv.md
│ │ ├── etape_4_personnalisation.md
│ │ ├── etape_5_lettre_motivation.md
│ │ ├── etape_6_revue_prep_entretien.md
├── scripts/
│ ├── interactive_cv_optimizer.py # Outil CLI
│ ├── ats_scoring.py # Calcul du score ATS
│ ├── cv_parser.py # Analyse du CV et de la description de poste
│ ├── keyword_extractor.py # Détection des mots-clés IA
│ ├── cover_letter_generator.py # Générateur de lettres de motivation IA
├── api/
│ ├── app.py # Backend FastAPI
│ ├── endpoints/
│ │ ├── process_cv.py
│ │ ├── score_ats.py
│ │ ├── generate_cover_letter.py
│ │ ├── process_cv_fr.py # Support français
├── docs/ # Documentation
│ ├── en/
│ │ ├── setup_guide.md
│ │ ├── usage_guide.md
│ │ ├── contributing.md
│ │ ├── roadmap.md
│ ├── fr/
│ │ ├── guide_installation.md
│ │ ├── guide_utilisation.md
│ │ ├── contribution.md
│ │ ├── feuille_route.md

yaml
Copy
Edit

---

## 🚀 Installation  
1. **Cloner le dépôt**  
   ```sh
   git clone https://github.com/yourusername/JobAppOptimizer.git
   cd JobAppOptimizer
Installer les dépendances

sh
Copy
Edit
pip install -r requirements.txt
Exécuter l’outil CLI

sh
Copy
Edit
python scripts/interactive_cv_optimizer.py
📌 Comment ça marche
L’Optimiseur de Candidature suit un processus en 6 étapes :

1️⃣ Extraction des informations clés à partir du CV et de la description du poste.
2️⃣ Analyse de la compatibilité ATS – Identification des forces et des lacunes.
3️⃣ Amélioration du CV – Optimisation du contenu, des mots-clés et de la structure.
4️⃣ Personnalisation – Mise en avant des compétences cachées et des motivations.
5️⃣ Génération d’une Lettre de Motivation – Sur mesure pour l’entreprise et le poste.
6️⃣ Relecture Finale et Préparation à l’Entretien – Dernières améliorations et questions types.

🔜 Feuille de Route
Phase	Fonctionnalité	Statut
✅ Phase 1	Invites IA structurées (anglais & français)	✅ Terminé
🔜 Phase 2	Outil CLI interactif	En cours
🔜 Phase 3	Optimisation ATS avec l’IA (Ollama & LangChain)	À venir
🔜 Phase 4	Application Web (FastAPI + Frontend)	À venir
🤝 Contributions
💡 Vous souhaitez contribuer ? Forkez le dépôt, proposez des Pull Requests et améliorez l’outil !

📜 Licence
Ce projet est sous licence MIT License – libre d’utilisation et de modification.

🚀 Prêt à optimiser votre CV et obtenir plus d’entretiens ? Essayez-le maintenant !
📩 Des questions ? Ouvrez une issue ou soumettez une pull request !