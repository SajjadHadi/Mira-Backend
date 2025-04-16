from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship

from db import Base


class PatientStatement(BaseModel):
    statement: str


class Statement(Base):
    __tablename__ = "statements"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    statement = Column(String(length=1000), nullable=False)
    disorders = Column(JSON, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="statements")
