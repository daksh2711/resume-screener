import json
from pathlib import Path


SKILLS_FILE = Path("data/skills_master_list.json")


def load_skills() -> list[str]:
    with open(SKILLS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_skills_from_text(text: str) -> list[str]:
    """
    Extracts skills from text using exact keyword matching.
    """
    text_lower = text.lower()
    skills = load_skills()

    found_skills = []

    for skill in skills:
        if skill in text_lower:
            found_skills.append(skill)

    return sorted(set(found_skills))


def compare_skills(resume_skills: list[str], jd_skills: list[str]) -> dict:
    """
    Compares resume skills with job description skills.
    """
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched_skills = sorted(resume_set & jd_set)
    missing_skills = sorted(jd_set - resume_set)

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }