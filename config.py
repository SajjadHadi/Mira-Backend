from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_PORT = int(os.getenv("CONTAINER_PORT", 8000))
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
    HF_TOKEN = os.getenv("HF_TOKEN")
    MODEL_NAME = os.getenv("MODEL_NAME")
    JWT_SECRET = os.getenv("JWT_SECRET")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    ALGORITHM = "HS256"
    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )

settings = Settings()