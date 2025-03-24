from skill_extraction import extract_skills_from_text
from job_matching import match_skills_with_jobs


def process_resume(content: str):
    return extract_skills_from_text(content)


def recommend_skills(skills: list):
    return match_skills_with_jobs(skills)