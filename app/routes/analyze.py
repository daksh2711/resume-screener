from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.pdf_parser import extract_text_from_pdf_bytes
from app.services.skills_extractor import extract_skills_from_text, compare_skills

router = APIRouter()


@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

        file_bytes = await file.read()
        resume_text = extract_text_from_pdf_bytes(file_bytes)

        resume_skills = extract_skills_from_text(resume_text)
        jd_skills = extract_skills_from_text(job_description)

        skill_comparison = compare_skills(resume_skills, jd_skills)

        return {
            "filename": file.filename,
            "job_description_preview": job_description[:300],
            "resume_text_preview": resume_text[:1000],
            "resume_text_length": len(resume_text),
            "resume_skills": resume_skills,
            "job_description_skills": jd_skills,
            "matched_skills": skill_comparison["matched_skills"],
            "missing_skills": skill_comparison["missing_skills"]
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))