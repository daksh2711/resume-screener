from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI(title="AI Resume Screener")

app.include_router(analyze_router)


@app.get("/")
def root():
    return {"message": "Resume Screener API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}