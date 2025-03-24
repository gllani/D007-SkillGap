# Placeholder for models.py - Simulated in-memory data models

# Simulated database tables (as lists)
CANDIDATES = []
JOBS = []
SKILL_GAP_RESULTS = []

# Sample structure
class Candidate:
    def __init__(self, id, name, skills):
        self.id = id
        self.name = name
        self.skills = skills

    def __repr__(self):
        return f"<Candidate {self.name}>"

class Job:
    def __init__(self, id, title, required_skills):
        self.id = id
        self.title = title
        self.required_skills = required_skills

    def __repr__(self):
        return f"<Job {self.title}>"

class SkillGapAnalysis:
    def __init__(self, candidate_id, job_id, missing_skills):
        self.candidate_id = candidate_id
        self.job_id = job_id
        self.missing_skills = missing_skills

    def __repr__(self):
        return f"<SkillGapAnalysis Candidate {self.candidate_id} - Job {self.job_id}>"

# Sample usage (for testing)
if __name__ == "__main__":
    # Add fake data
    CANDIDATES.append(Candidate(1, "Alice", "python, sql"))
    JOBS.append(Job(1, "Data Scientist", "python, sql, machine learning"))

    # Print data
    print(CANDIDATES[0])
    print(JOBS[0])
