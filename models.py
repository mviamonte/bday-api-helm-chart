from sqlmodel import SQLModel, Field
from pydantic import BaseModel, field_validator
from datetime import date

class User(SQLModel, table=True):
    username: str = Field(primary_key=True)
    date_of_birth: date

class UserInput(BaseModel):
    dateOfBirth: date

    @field_validator("dateOfBirth")
    @classmethod
    def validate_date(cls, v: date) -> date:
        if v >= date.today():
            raise ValueError("The date should be older than today's date")
        return v