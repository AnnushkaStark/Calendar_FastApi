from datetime import datetime

from pydantic import BaseModel, Field
from calendar_app.constants.comment_constants import (
    MAX_LENGTH_TEXT, MIN_LENGTH_TEXT  
)  


class CommentBase(BaseModel):   
    id: int
    author_id: int
    text: str = Field(
        min_length=MIN_LENGTH_TEXT,
        max_length=MAX_LENGTH_TEXT
    )
    created_at:datetime = Field(default_factory=datetime.now)
    event_id: int

    class Config:
        from_attributes = True