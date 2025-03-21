import os
import docx
import PyPDF2
import markdown
from bs4 import BeautifulSoup

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text() or ""
    return text.strip()


def extract_text_from_docx(docx_path):
    """Extract text from a Word (.docx) file."""
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()


def extract_text_from_md(md_path):
    """Extracts plain text from a Markdown (.md) file."""
    with open(md_path, "r", encoding="utf-8") as file:
        md_content = file.read()

    # Convert Markdown to HTML, then strip HTML tags
    html_content = markdown.markdown(md_content)
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text().strip()


def extract_text(file_path):
    """Detects file type and extracts text accordingly."""
    if not os.path.exists(file_path):
        return f"⚠️ File not found: {file_path}"

    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".md"):
        return extract_text_from_md(file_path)
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    else:
        return f"⚠️ Unsupported file format: {file_path}"
