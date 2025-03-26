import fitz
import re
import spacy
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.http.models import Distance, VectorParams
from collections import Counter
from keybert import KeyBERT

# === Configuration ===
CV_PATH = "JobAppOptimizer/rolefiles/CV.pdf"
JD_PATH = "JobAppOptimizer/rolefiles/job_desc.pdf"
QDRANT_PATH = "JobAppOptimizer/qdrant_storage"
COLLECTION_NAME = "cv_similarity_final"

# === Load NLP Models ===
nlp = spacy.load("en_core_web_sm")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
kw_model = KeyBERT(model=embedder) 

# === PDF Text Extraction ===
def extract_text_from_pdf(path):
    with fitz.open(path) as doc:
        return "\n".join(page.get_text() for page in doc)

# === Generalized Skill Extraction (Non-hardcoded) ===
def clean_phrase(phrase):
    # remove unwanted chars and excess whitespace
    phrase = re.sub(r'[^a-zA-Z\s/-]', '', phrase).strip()
    phrase = re.sub(r'\s+', ' ', phrase)
    return phrase.lower()

def extract_skills(text, top_n=25):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 3),
        stop_words='english',
        use_maxsum=True,
        nr_candidates=40,
        top_n=top_n
    )
    return set(kw for kw, _ in keywords)


# === Initialize Qdrant ===
def init_qdrant():
    client = QdrantClient(path=QDRANT_PATH)
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=embedder.get_sentence_embedding_dimension(),
            distance=Distance.COSINE
        ),
    )
    return client

# === Compute Similarity ===
def compute_ats_score(cv_path, jd_path):
    client = init_qdrant()
    cv_text = extract_text_from_pdf(cv_path)
    jd_text = extract_text_from_pdf(jd_path)

    # Embed CV
    cv_vector = embedder.encode(cv_text).tolist()
    client.upsert(
        COLLECTION_NAME,
        points=[PointStruct(id=1, vector=cv_vector, payload={"source": "cv"})]
    )

    # Embed Job Description and Query
    jd_vector = embedder.encode(jd_text).tolist()
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=jd_vector,
        limit=1,
        with_payload=True
    )

    # Extract Skills
    cv_skills = extract_skills(cv_text)
    jd_skills = extract_skills(jd_text)

    matched_skills = sorted(cv_skills & jd_skills)
    missing_skills = sorted(jd_skills - cv_skills)

    # Similarity Score
    score = round(results[0].score * 100, 2) if results else 0.0

    # === Output ===
    print("\n🚀 ATS Similarity Report\n" + "="*30)
    print(f"🧠 Similarity Score: {score}%")

    print("\n📑 Job Description Key Skills:")
    for skill in sorted(jd_skills):
        print(f" - {skill}")

    print(f"\n✅ Matched Skills ({len(matched_skills)}):")
    for skill in matched_skills:
        print(f" - {skill}")

    print(f"\n❌ Missing Skills ({len(missing_skills)}):")
    for skill in missing_skills:
        print(f" - {skill}")

# === Run ===
if __name__ == "__main__":
    compute_ats_score(CV_PATH, JD_PATH)
