from flask import Flask
from flask_cors import CORS  
from app import create_app
from app.database import init_db

app = create_app()

CORS(app) 

@app.route("/")
def home():
    return "✅ Flask API is running: Skill Gap Analysis"

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
