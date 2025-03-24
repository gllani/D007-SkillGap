from app import db

# -------------------------------
# Models
# -------------------------------

class Candidate(db.Model):
    """Model for storing candidate information."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.Text, nullable=False)  # Comma-separated skills

    def __repr__(self):
        return f"<Candidate {self.name}>"

class Job(db.Model):
    """Model for storing job details and required skills."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    required_skills = db.Column(db.Text, nullable=False)  # Comma-separated skills

    def __repr__(self):
        return f"<Job {self.title}>"

class SkillGapAnalysis(db.Model):
    """Model for storing results of candidate vs job skill gap analysis."""
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.id"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("job.id"), nullable=False)
    missing_skills = db.Column(db.Text, nullable=False)  # Comma-separated list of skills

    candidate = db.relationship("Candidate", backref="skill_analyses", lazy=True)
    job = db.relationship("Job", backref="skill_analyses", lazy=True)

    def __repr__(self):
        return f"<SkillGapAnalysis Candidate={self.candidate_id} Job={self.job_id}>"

# -------------------------------
# Database Initialization
# -------------------------------

def init_db():
    """Initialize database and create tables."""
    db.create_all()
    print("✅ Database tables created.")

# -------------------------------
# Script usage
# -------------------------------

if __name__ == "__main__":
    from app import create_app
    app = create_app()

    with app.app_context():
        init_db()
