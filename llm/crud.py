from datetime import datetime, timezone

from sqlalchemy.orm import Session

from .models import Statement


def create_statement(db: Session, user_id: int, statement: str, disorders: dict) -> Statement:
    db_statement = Statement(
        user_id=user_id,
        statement=statement,
        disorders=disorders,
        created_at=datetime.now(timezone.utc)
    )
    db.add(db_statement)
    db.commit()
    db.refresh(db_statement)
    return db_statement
