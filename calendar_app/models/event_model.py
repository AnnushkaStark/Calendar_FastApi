from datetime import datetime
from typing import  Optional, TYPE_CHECKING

from sqlalchemy.orm import Mapped ,mapped_column, relationship
from sqlalchemy import (
    Integer,
    Enum,
    DateTime,
    ForeignKey,
    Boolean,
    func,
) 
from sqlalchemy.orm import relationship

from calendar_app.constants.event_constants import (
    EventPriority,
    EventType,
    EventLocation,
    EventRepitabilyty
)
from calendar_app.database import Base

if TYPE_CHECKING:
    from models.user_model import User


class Event(Base):
    """
    Модель события
    - id
    - название
    - категория
    - приоретет
    - организатор
    - дата и время начала
    - дата и время окончания
    - периодичность 
    - описание
    - Владелец 
    - Участники
    """
    __tablename__ = "event" 

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str]
    event_type: Mapped[EventType] = mapped_column(
        Enum(EventType), default=EventType.no_category
    )
    priority: Mapped[EventPriority] = mapped_column(
        Enum(EventPriority),
        default=EventPriority.without_priority
    )
    repeatability: Mapped[EventRepitabilyty] = mapped_column(
        Enum(EventRepitabilyty),
        default=EventRepitabilyty.no_repeats
    )
    event_location: Mapped[EventLocation] = mapped_column(
        Enum(EventLocation),
        default=EventLocation.other
    )
    organizer: Mapped[Optional[str]]
    start_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
    end_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
    duration:  Mapped[datetime]
    description:  Mapped[Optional[str]]
    owner_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE")
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    participants: Mapped[list["User"]] = relationship(
        "User",
        back_populates="events",
        secondary= "event_user_association"
    )

    @property
    def duration(self):
        if self.end_time and self.start_time:
            return self.end_time - self.start_time
        return None

    def __repr__(self) -> str:
        return f"{self.id}"
    


  
