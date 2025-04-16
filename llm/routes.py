from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.models import UserInDB
from auth.security import get_current_user
from db import get_db
from .crud import create_statement, get_statements
from .inference import get_predictor
from .models import StatementListResponse, PatientStatement, Statement

router = APIRouter(prefix="/llm", tags=["LLM"])


@router.post("/predict")
def predict_disorder(
        data: PatientStatement,
        user: UserInDB = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    predicted_disorder = get_predictor().predict(data.statement)
    created_statement = create_statement(db, user.id, data.statement, predicted_disorder)
    return created_statement


@router.get("/statements", response_model=StatementListResponse)
def get_user_statements(
        user: UserInDB = Depends(get_current_user),
        db: Session = Depends(get_db),
        skip: Optional[int] = 0,
        limit: Optional[int] = 10
):
    statements = get_statements(db, user.id, skip, limit)

    total_statements = db.query(Statement).filter(Statement.user_id == user.id).count()

    return {"total": total_statements, "statements": statements}
