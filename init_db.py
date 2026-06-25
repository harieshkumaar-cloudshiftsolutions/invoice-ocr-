import os
from sqlalchemy import create_engine
from models import Base
from dotenv import load_dotenv


load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("NEON_CONNECTION_STRING")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("Missing NEON_CONNECTION_STRING.")

# Neon requires connection pooling adjustments for serverless environments
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    pool_pre_ping=True, 
    pool_recycle=300
)

def create_tables():
    print("Connecting to database and verifying schemas...")
    try:
        Base.metadata.create_all(bind=engine)
        print("Success: All tables successfully built in Neon!")
    except Exception as e:
        print(f"Failed to create tables: {e}")

if __name__ == "__main__":
    create_tables()