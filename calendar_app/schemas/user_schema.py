from email_validator import validate_email
from typing import List
from pydantic import BaseModel, EmailStr, Field, validator

from calendar_app.schemas.event_schema import EventBase
from calendar_app.constants.user_constants import (
    MIN_NICKNAME_LENGTH,
    MAX_NICKNAME_LENGTH,
    MIN_PASSWORD_LENGTH,
)


class UserBase(BaseModel):
    nickname: str = Field(
        min_length=MIN_NICKNAME_LENGTH,
        max_length=MAX_NICKNAME_LENGTH
    )
    email: EmailStr
    password: str =Field(min_length=MIN_PASSWORD_LENGTH)
    events: List[EventBase] = []

    @validator("email")
    def email_check(cls, v: EmailStr) -> EmailStr:
        email_info = validate_email(v, check_deliverability=True)
        email = email_info.normalized
        return email

    class Config:
        from_attributes = True


