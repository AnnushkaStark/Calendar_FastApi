from datetime import datetime

from pydantic import BaseModel,  Field, validator
from typing import Optional, List

from calendar_app.schemas.user_schema import UserBase
from calendar_app.constants.event_constants import (
    MAX_LENGTH_DESRIPTION,
    MIN_LENGTH_TITLE,
    MAX_LENGTH_TITLE,
    EventType,
    EventLocation,
    EventPriority,
    EventRepitabilyty
)


class EventBase(BaseModel):
    id: int
    title: str = Field(
        min_length=MIN_LENGTH_TITLE,
        max_length=MAX_LENGTH_TITLE,  
    )
    event_type: EventType = Field(default=EventType.no_category)
    priority: EventPriority = Field(default=EventPriority.without_priority)
    repeatability: EventRepitabilyty = Field(default=EventRepitabilyty.no_repeats)
    event_location: EventLocation = Field(default=EventLocation.other)
    organizer: str
    start_time: datetime = Field(default_factory=datetime.now)
    end_time: datetime = Field(default_factory=datetime.now)
    duration: int
    description: str = Field(min_length=MAX_LENGTH_DESRIPTION, default="")
    owner_id: int
    is_active: Optional[bool] = False
    participants: List[UserBase] = []
   
    @validator('duration', pre=True, always=True)
    def calculate_duration(cls, v, values, **kwargs):
        if 'start_time' in values and 'end_time' in values:
            start_time = values['start_time']
            end_time = values['end_time']
            duration = int((end_time - start_time).total_seconds())
            return duration
        return None
    
    class Config:
        from_attributes = True
    