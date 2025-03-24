# Skill Gap Analysis Platform 🚀

## Overview
The **Skill Gap Analysis Platform** helps **match candidates to job listings** by analyzing their skills and identifying missing qualifications. This Flask-based application integrates **PostgreSQL, AWS S3, and Docker** to provide an efficient backend solution.

## Features
✅ **Candidate Skill Matching** - Matches candidates to jobs based on skills  
✅ **Skill Gap Analysis** - Identifies missing skills for a job  
✅ **Job Matching** - Finds the best job fit for a candidate  
✅ **ETL Pipeline** - Handles data extraction, transformation, and loading  
✅ **AWS S3 Integration** - Supports file uploads (resumes, datasets)  
✅ **Dockerized & Deployable** - Runs in **containers on AWS**  

---

## 📌 Installation Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/gllani/D007-SkillGap
cd D007-SkillGap

pip install -r requirements.txt

SECRET_KEY=supersecretkey
DATABASE_URL=postgresql://user:password@db/skill_db
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
S3_BUCKET_NAME=your-s3-bucket-name

python app/database_setup.py

python app/main.py

docker-compose up --build

docker-compose down

API Endpoints

🔹 Home
GET / → Check if the API is running.
🔹 Skill Analysis
POST /analyze
Request:
json

{
  "skills": "Python, SQL, Machine Learning"
}
Response:
json

{
  "candidate": "John Doe",
  "best_matches": [
    {"job": "Data Scientist", "match_score": 85}
  ]
}
🔹 Upload Resume (AWS S3)
POST /upload
Request: Upload a file to S3.
🚀 Deployment on AWS

1️⃣ Deploy with Docker on AWS EC2
sh

sudo docker-compose up --build -d
2️⃣ Check Running Containers
sh

docker ps
3️⃣ Stop & Restart
sh

docker-compose down
docker-compose up -d
👨‍💻 Technologies Used

Python (Flask)
PostgreSQL
Docker & Docker Compose
Gunicorn
AWS S3
HTML, CSS, JavaScript (Frontend)


This project is open-source and available under the MIT License.

---

### **Explanation:**
1. **Installation Guide** → Step-by-step instructions for **setup & running**.
2. **API Endpoints** → Explains the **Flask API structure**.
3. **Docker Instructions** → How to **deploy with Docker**.
4. **AWS Deployment** → **Run on AWS EC2** with Docker.
5. **Tech Stack** → Highlights **Flask, PostgreSQL, AWS, Docker**.
6. **Contact & License** → Provides **open-source info**.

