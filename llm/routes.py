from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.models import UserInDB
from auth.security import get_current_user
from db import get_db
from .crud import create_statement
from .inference import get_predictor
from .models import PatientStatement

router = APIRouter(prefix="/llm", tags=["LLM"])


@router.post("/predict")
def predict_disorder(
        data: PatientStatement,
        user: UserInDB = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    predicted_disorder = get_predictor().predict(data.statement)
    created_statement = create_statement(db, user.id, data.statement, predicted_disorder)
    return {"data": created_statement}
