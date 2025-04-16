from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)


class UserCreate(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class UserInDB(BaseModel):
    id: int
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str
