# 📌 Job Application Optimizer

🚀 **AI-powered tool for optimizing CVs & cover letters for ATS & recruiters**

## 📖 Overview
Job Application Optimizer helps job seekers refine their CVs and cover letters to increase their chances of passing Applicant Tracking Systems (ATS) and catching recruiters' attention. 

This tool provides AI-powered step-by-step guidance, ATS analysis, and content improvements to craft stronger job applications.

## ✨ Features
✅ **ATS Optimization** – Improve CVs to pass ATS filters.  
✅ **AI-Powered Enhancements** – Generate ATS-friendly keyword suggestions.  
✅ **Step-by-Step AI Guidance** – Guide users through the application process.  
✅ **Cover Letter Personalization** – Create tailored, impactful cover letters.  
✅ **Gap Analysis** – Identify missing skills, weak phrasing, and formatting issues.  
✅ **Bilingual Support** – English & French versions available.  
✅ **CLI & API Integration (Upcoming)** – Automate with a command-line tool and API.  

## 📂 Project Structure
```
JobAppOptimizer/
├── README.md                # Documentation
├── LICENSE                  # MIT License (recommended)
├── requirements.txt         # Dependencies
├── prompts/                 # AI prompts (English & French)
│   ├── en/                  # English prompts
│   ├── fr/                  # French prompts
├── scripts/                 # Core functionalities
│   ├── interactive_cv_optimizer.py  # CLI tool
│   ├── ats_scoring.py              # ATS score calculation
│   ├── cv_parser.py                # CV & job description parser
│   ├── keyword_extractor.py        # AI keyword detection
│   ├── cover_letter_generator.py   # AI cover letter tool
├── api/                     # API backend (FastAPI)
│   ├── app.py                # Main API entry point
│   ├── endpoints/            # API endpoints
│   │   ├── process_cv.py
│   │   ├── score_ats.py
│   │   ├── generate_cover_letter.py
│   │   ├── process_cv_fr.py   # French support
├── docs/                    # Documentation
│   ├── en/                   # English docs
│   ├── fr/                   # French docs
```

## 🚀 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/JobAppOptimizer.git
cd JobAppOptimizer
```
### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 3️⃣ Run the CLI Tool
```sh
python scripts/interactive_cv_optimizer.py
```

## 📌 How It Works
The **Job Application Optimizer** follows a structured 6-step process:

1️⃣ **Extract Key Information** – Analyze the CV & job description.  
2️⃣ **Analyze ATS Compatibility** – Identify strengths & gaps.  
3️⃣ **Refine the CV** – Improve content, keywords, and structure.  
4️⃣ **Personalize** – Highlight hidden strengths & motivations.  
5️⃣ **Generate a Cover Letter** – Tailored to the job & company.  
6️⃣ **Final Review & Interview Prep** – Last-minute improvements & sample questions.  

---

## 🔜 Roadmap
| Phase      | Feature                                      | Status     |
|------------|----------------------------------------------|------------|
| ✅ Phase 1 | Structured Prompts (English & French)       | ✅ Done     |
| 🔜 Phase 2 | Interactive CLI Tool                        | In Progress |
| 🔜 Phase 3 | AI-Powered ATS Optimization (Ollama & LangChain) | Upcoming  |
| 🔜 Phase 4 | Web App (FastAPI + Frontend)                | Upcoming  |

---

## 🤝 Contributions
💡 Want to contribute? Follow these steps:
1. **Fork the repo** on GitHub.
2. **Clone your fork** and create a new branch.
3. **Make your improvements** and commit changes.
4. **Submit a pull request** for review!

---

## 📜 License
This project is licensed under the **MIT License** – free to use & modify.

---

🚀 **Ready to optimize your CV & land more interviews? Try it now!**  
📩 **Questions?** Open an issue or submit a pull request!