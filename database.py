from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("NEON_CONNECTION_STRING")

if not DATABASE_URL:
    raise ValueError("NEON_CONNECTION_STRING not found in .env")

# Create SQLAlchemy Engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300
)

# Create Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()