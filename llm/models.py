from pydantic import BaseModel

class PatientStatement(BaseModel):
    statement: str
