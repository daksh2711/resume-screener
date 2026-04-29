from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.pdf_parser import extract_text_from_pdf_bytes
from app.services.skills_extractor import extract_skills_from_text, compare_skills
from app.services.scorer import (
    calculate_skill_score,
    calculate_section_score,
    calculate_overall_score,
)

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

        skill_score = calculate_skill_score(
            skill_comparison["matched_skills"],
            jd_skills
        )
        section_score = calculate_section_score(resume_text)
        overall_score = calculate_overall_score(skill_score, section_score)

        return {
            "filename": file.filename,
            "resume_text_length": len(resume_text),
            "resume_text_preview": resume_text[:1000],
            "job_description_preview": job_description[:300],
            "resume_skills": resume_skills,
            "job_description_skills": jd_skills,
            "matched_skills": skill_comparison["matched_skills"],
            "missing_skills": skill_comparison["missing_skills"],
            "skill_score": round(skill_score, 2),
            "section_score": round(section_score, 2),
            "overall_score": overall_score
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))