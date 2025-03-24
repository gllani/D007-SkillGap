class Config:
    """
    Placeholder configuration for local development and testing.
    """

    # Secret key for session and form security (replace in production)
    SECRET_KEY = "dev_secret_key"

    # Use local SQLite file as the database
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Debugging mode ON for local testing
    DEBUG = True

    # Fake AWS credentials (non-functional in this mode)
    AWS_ACCESS_KEY = "FAKE_AWS_ACCESS_KEY"
    AWS_SECRET_KEY = "FAKE_AWS_SECRET_KEY"
    S3_BUCKET_NAME = "FAKE_BUCKET"

    # Dummy API key
    API_KEY = "test-api-key"
