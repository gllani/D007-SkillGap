
def match_skills_with_jobs(skills: list):
    job_requirements = ["Python", "Machine Learning", "Data Engineering"]
    missing_skills = set(job_requirements) - set(skills)
    return list(missing_skills)
