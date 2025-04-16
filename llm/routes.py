from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.models import UserInDB
from auth.security import get_current_user
from db import get_db
from .inference import get_predictor
from .models import PatientStatement

router = APIRouter(prefix="/llm", tags=["LLM"])


@router.post("/predict")
def predict_disorder(
        data: PatientStatement,
        user: UserInDB = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    predictor = get_predictor()
    predicted_disorder = predictor.multi_predict(data.statement)

    return {"predicted_disorder": predicted_disorder}
