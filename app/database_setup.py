from app import create_app, db
from app.database import Candidate, Job

def init_db():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        preload_sample_data()
        db.session.commit()
        print("✅ Database initialized with sample data.")

def preload_sample_data():
    candidates = [
        Candidate(name="Alice Johnson", skills="Python, SQL, Machine Learning"),
        Candidate(name="Bob Smith", skills="Java, JavaScript, AWS, Docker"),
        Candidate(name="Charlie Brown", skills="C++, Data Analysis, Flask, Pandas"),
    ]

    jobs = [
        Job(title="Data Scientist", required_skills="Python, SQL, Machine Learning, TensorFlow"),
        Job(title="Software Engineer", required_skills="Java, JavaScript, AWS"),
        Job(title="Data Analyst", required_skills="SQL, Data Analysis, Pandas, Excel"),
    ]

    db.session.add_all(candidates + jobs)

if __name__ == "__main__":
    init_db()
