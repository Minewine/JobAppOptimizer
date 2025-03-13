# 📌 Optimiseur de Candidature

🚀 **Outil IA pour optimiser les CV et lettres de motivation pour les ATS & recruteurs**

## 📖 Aperçu
L'Optimiseur de Candidature aide les chercheurs d'emploi à améliorer leurs CV et lettres de motivation afin d'augmenter leurs chances de passer les systèmes de suivi des candidatures (ATS) et d'attirer l'attention des recruteurs.

Cet outil fournit une assistance guidée par IA étape par étape, une analyse ATS et des améliorations de contenu pour créer des candidatures plus efficaces.

## ✨ Fonctionnalités
✅ **Optimisation ATS** – Améliorez les CV pour passer les filtres ATS.  
✅ **Améliorations alimentées par l'IA** – Suggestions de mots-clés compatibles ATS.  
✅ **Guidage IA étape par étape** – Accompagne les utilisateurs dans le processus de candidature.  
✅ **Personnalisation de la lettre de motivation** – Créez des lettres adaptées et percutantes.  
✅ **Analyse des lacunes** – Identifie les compétences manquantes, les formulations faibles et les problèmes de mise en forme.  
✅ **Support bilingue** – Disponible en anglais et en français.  
✅ **Intégration CLI & API (prochainement)** – Automatisation via un outil en ligne de commande et une API.  

## 📂 Structure du Projet
```
JobAppOptimizer/
├── README.md                # Documentation
├── LICENSE                  # Licence MIT (recommandée)
├── requirements.txt         # Dépendances
├── prompts/                 # Prompts IA (Anglais & Français)
│   ├── en/                  # Prompts en anglais
│   ├── fr/                  # Prompts en français
├── scripts/                 # Fonctionnalités principales
│   ├── interactive_cv_optimizer.py  # Outil CLI
│   ├── ats_scoring.py              # Calcul du score ATS
│   ├── cv_parser.py                # Analyse du CV & de l’offre d’emploi
│   ├── keyword_extractor.py        # Détection de mots-clés par IA
│   ├── cover_letter_generator.py   # Générateur de lettres de motivation IA
├── api/                     # Backend API (FastAPI)
│   ├── app.py                # Point d'entrée principal
│   ├── endpoints/            # Endpoints API
│   │   ├── process_cv.py
│   │   ├── score_ats.py
│   │   ├── generate_cover_letter.py
│   │   ├── process_cv_fr.py   # Support français
├── docs/                    # Documentation
│   ├── en/                   # Docs en anglais
│   ├── fr/                   # Docs en français
```

## 🚀 Installation
### 1️⃣ Cloner le dépôt
```sh
git clone https://github.com/yourusername/JobAppOptimizer.git
cd JobAppOptimizer
```
### 2️⃣ Installer les dépendances
```sh
pip install -r requirements.txt
```
### 3️⃣ Exécuter l’outil CLI
```sh
python scripts/interactive_cv_optimizer.py
```

## 📌 Comment ça marche ?
L'**Optimiseur de Candidature** suit un processus structuré en 6 étapes :

1️⃣ **Extraction des informations clés** – Analyse du CV et de l'offre d'emploi.  
2️⃣ **Analyse de compatibilité ATS** – Identification des forces et faiblesses.  
3️⃣ **Amélioration du CV** – Optimisation du contenu, des mots-clés et de la structure.  
4️⃣ **Personnalisation** – Mise en avant des forces cachées et des motivations.  
5️⃣ **Génération de la lettre de motivation** – Adaptée au poste et à l'entreprise.  
6️⃣ **Relecture finale & préparation à l'entretien** – Dernières améliorations et questions d'entretien potentielles.  

---

## 🔜 Feuille de route
| Phase      | Fonctionnalité                                    | Statut      |
|------------|--------------------------------------------------|-------------|
| ✅ Phase 1 | Prompts structurés (Anglais & Français)         | ✅ Terminé   |
| 🔜 Phase 2 | Outil CLI interactif                            | En cours    |
| 🔜 Phase 3 | Optimisation ATS avec IA (Ollama & LangChain)   | À venir     |
| 🔜 Phase 4 | Application Web (FastAPI + Frontend)           | À venir     |

---

## 🤝 Contributions
💡 Vous souhaitez contribuer ? Suivez ces étapes :
1. **Forkez le dépôt** sur GitHub.
2. **Clonez votre fork** et créez une nouvelle branche.
3. **Apportez vos améliorations** et validez les modifications.
4. **Soumettez une pull request** pour révision !

---

## 📜 Licence
Ce projet est sous **licence MIT** – libre d'utilisation et de modification.

---

🚀 **Prêt à optimiser votre CV et décrocher plus d’entretiens ? Essayez-le maintenant !**  
📩 **Des questions ?** Ouvrez un ticket ou soumettez une pull request !