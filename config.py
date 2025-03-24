import os

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "skill_gap_db"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
}

AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET", "skill-gap-analysis-bucket")

API_SETTINGS = {
    "host": os.getenv("API_HOST", "0.0.0.0"),
    "port": int(os.getenv("API_PORT", 8000)),
}

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")