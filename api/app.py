from fastapi import FastAPI

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
