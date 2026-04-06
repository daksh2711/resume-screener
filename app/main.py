from fastapi import FastAPI

app = FastAPI(title="AI Resume Screener")

@app.get("/")
def root():
    return {"message": "Resume Screener API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}