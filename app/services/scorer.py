def calculate_skill_score(matched_skills: list[str], jd_skills: list[str]) -> float:
    if not jd_skills:
        return 0.0

    return (len(matched_skills) / len(jd_skills)) * 100


def calculate_section_score(resume_text: str) -> float:
    text = resume_text.lower()

    score = 0
    sections = ["skills", "experience", "education", "projects"]

    for section in sections:
        if section in text:
            score += 1

    return (score / len(sections)) * 100


def calculate_overall_score(skill_score: float, section_score: float) -> float:
    return round((0.6 * skill_score) + (0.4 * section_score), 2)