from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
from fastapi import FastAPI

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_timeout=30
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_database():
    inspector = inspect(engine)
    required_tables = ["users"]
    for table in required_tables:
        if not inspector.has_table(table):
            raise RuntimeError(f"Table {table} missing. Run Alembic migrations.")