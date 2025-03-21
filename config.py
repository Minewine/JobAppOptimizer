import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_BASE = "https://openrouter.ai/api/v1/chat/completions"


# File Paths
BASE_DIR = "/home/mick/Projects/JobAppOptimizer"
ROLEFILES_DIR = f"{BASE_DIR}/rolefiles"
OUTPUT_DIR = f"{BASE_DIR}/output"

CV_LOCATION = f"{ROLEFILES_DIR}/COUGHLAN_CV_2024_EN.pdf"
JOB_DESC_LOCATION = f"{ROLEFILES_DIR}/job_desc.pdf"
ATS_REPORT_PATH = f"{OUTPUT_DIR}/ats_report.md"
OPTIMIZED_CV_PATH = f"{OUTPUT_DIR}/optimized_cv.md"
COVER_LETTER_PATH = f"{OUTPUT_DIR}/cover_letter.md"
API_BASE = "https://openrouter.ai/api/v1/chat/completions"
SYSTEM_MESSAGE = "You are an AI-powered Job Application Wizard specializing in analyzing CVs and optimizing them for ATS. Your goal is to provide structured, actionable feedback in Markdown format to improve the applicant's chances of being shortlisted."


def get_analysis_prompt(job_description, cv_content):
    return f"""<system>
    <instructions>
        <instruction>Generate a report analyzing the provided CV against the given job description.</instruction>
        <instruction>Format the output as Markdown with headings, tables, and plain text, suitable for display in Streamlit.</instruction>
        <instruction>Save the final output to a file named 'ats_report.md'.</instruction>
    </instructions>

    <tasks>
        <task>
            <name>ATS Compatibility Score</name>
            <description>Evaluate how well the CV aligns with the job description based on keywords, skills, and qualifications. Assign a score from 0 to 100%.</description>
            <output>
                A Markdown section with a heading 'ATS Compatibility Score' and a paragraph containing the score (e.g., 'Score: 85%') followed by a brief explanation.
            </output>
        </task>

        <task>
            <name>Extract & Summarize</name>
            <description>Extract key elements from the job description, including required skills, qualifications, experience, and company values. Rank them by importance based on emphasis or frequency in the text.</description>
            <output>
                A Markdown section with a heading 'Job Description Summary' and a table listing elements, descriptions, and importance (e.g., | Element | Description | Importance |).
            </output>
        </task>

        <task>
            <name>Detailed Comparison</name>
            <description>Compare the CV to the job description, focusing on skills, qualifications, and experience. Order the comparison by the importance of each element as identified in the job description.</description>
            <output>
                A Markdown section with a heading 'Detailed Comparison' and a table comparing job requirements to CV content (e.g., | Job Requirement | CV Match | Notes |).
            </output>
        </task>

        <task>
            <name>Gaps & Recommendations</name>
            <description>Identify elements from the job description missing in the CV and provide specific, actionable suggestions to address these gaps.</description>
            <output>
                A Markdown section with a heading 'Gaps & Recommendations', a subheading 'Gaps' with a bulleted list, and a subheading 'Recommendations' with a bulleted list.
            </output>
        </task>
    </tasks>

    <formatting_rules>
        <rule>Use Markdown syntax: '#' for headings, '|' for tables, '-' for bullets, and plain text for content.</rule>
        <rule>Ensure tables are properly aligned and readable in Markdown (e.g., use '|---|' for column separators).</rule>
        <rule>Avoid XML tags, LaTeX, or other non-Markdown formatting.</rule>
    </formatting_rules>

    <job_details>
        <job_description>{job_description}</job_description>
    </job_details>

    <cv_content>{cv_content}</cv_content>

    <notes>If the CV or job description is incomplete or unclear, include a note in the output (e.g., 'Note: Limited data provided') and proceed with the available information.</notes>
</system>"""


def get_cv_customization_prompt(cv_content, ats_report, style="detailed"):
    style_instruction = "Format the CV in a concise style, focusing on brevity and key points." if style == "concise" else "Format the CV in a detailed style, elaborating on experience and skills."
    return f"""<system>

    <instructions>
        <instruction>Revise the provided CV by incorporating recommendations from the ATS report.</instruction>
        <instruction>Enhance the CV by addressing gaps identified in the ATS report, adding relevant skills, qualifications, and details where applicable.</instruction>
        <instruction>Preserve the original structure and content of the CV, only modifying or adding sections as needed to align with the ATS report.</instruction>
        <instruction>Use exact keywords and phrases from the ATS report (e.g., 'Spring Framework' instead of 'Spring') to ensure ATS compatibility, unless the CV provides a valid alternative term.</instruction>
        <instruction>{style_instruction}</instruction>
        <instruction>Format the output as Markdown, suitable for display in Streamlit, with clear headings and sections.</instruction>
        <instruction>Save the final output to a file named 'customized_cv.md'.</instruction>
    </instructions>

    <tasks>
        <task>
            <name>Analyze ATS Report</name>
            <description>Review the 'Gaps & Recommendations' section of the ATS report to identify missing elements (e.g., skills, qualifications, soft skills) and actionable suggestions.</description>
            <output>No separate output; use this analysis to inform the CV revision.</output>
        </task>

        <task>
            <name>Revise CV</name>
            <description>Update the CV by adding or enhancing sections based on the ATS report recommendations. Prioritize high-importance elements (e.g., skills marked 'High' in the ATS report) and integrate them prominently in the 'Skills' or 'Experience' sections. For missing skills, infer reasonable proficiency from related experience if possible (e.g., Python experience might imply familiarity with frameworks), and add them with qualifiers (e.g., 'Exposure to AWS via team projects'). Avoid generic placeholders; ensure additions are specific and job-relevant.</description>
            <output>
                A complete, revised CV in Markdown format with sections such as:
                - '# Profile' (summary with soft skills, e.g., '## Summary')
                - '# Skills' (technical and other skills, e.g., '## Technical Skills', '## Soft Skills')
                - '# Experience' (job-specific experience, e.g., '## Job Title - Company (Dates)')
                - '# Education' (qualifications, e.g., '## Degree - Institution')
                - '# Languages' (language proficiency, e.g., '## Languages Spoken')
            </output>
        </task>

        <task>
            <name>Validation</name>
            <description>Ensure all gaps identified in the ATS report are addressed in the revised CV. If certain recommendations cannot be implemented due to lack of information, note this. Additionally, estimate an updated ATS compatibility score (0-100%) based on how well the revised CV now aligns with the ATS report’s 'Job Description Summary' and 'Detailed Comparison' sections.</description>
            <output>
                A Markdown section with a heading '## Notes' at the end of the CV, including:
                - Explanations of unresolved gaps (e.g., 'Note: No Italian proficiency added as no data was provided').
                - An estimated ATS compatibility score (e.g., 'Estimated ATS Score: 75% - Improved by addressing most technical skills').
            </output>
        </task>
    </tasks>

    <formatting_rules>
        <rule>Use Markdown syntax: '# ' for main headings, '## ' for subheadings within sections (e.g., '## Technical Skills' under '# Skills'), '-' for bullets, and plain text for content.</rule>
        <rule>Organize the CV into clear sections with appropriate headings and subheadings for readability.</rule>
        <rule>Avoid XML tags, LaTeX, or other non-Markdown formatting.</rule>
    </formatting_rules>

    <cv_content>{cv_content}</cv_content>

    <ats_report>{ats_report}</ats_report>

    <notes>If specific skills or experiences recommended in the ATS report cannot be confirmed from the original CV, flag them in the 'Notes' section as requiring user clarification (e.g., 'Note: AWS experience recommended - please confirm if applicable'). Avoid guessing unless reasonable inference is possible.</notes>
</system>"""