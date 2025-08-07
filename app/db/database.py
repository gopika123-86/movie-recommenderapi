from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session

# Load environment variables from .env
load_dotenv()

# Get DB URL from .env
DB_URL = os.getenv("DATABASE_URL")

# SQLAlchemy setup
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# ✅ Add this function to use DB sessions via dependency injection in FastAPI
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
