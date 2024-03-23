from datetime import datetime
from typing import  Optional, List

from sqlalchemy.orm import Mapped ,mapped_column, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    DateTime,
    Table,
    ForeignKey,
    func,
) 
from sqlalchemy.orm import relationship

from calendar_app.constants import (
    EventPriority,
    EventType,
    EventLocation,
    EventRepitabilyty
)
from calendar_app.database import Base


class User(Base):
    """
    Временная таблица
    пользователей
    """
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nickname: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)


# Ассоциативная таблица для связи между Event и User
event_user_association = Table(
    'event_user',
    Base.metadata,
    Column(
        "event_id", Integer, ForeignKey("event.id", ondelete="CASCADE")
    ),
    Column("user_id", Integer, ForeignKey("user.id", ondelete="CASCADE")),
)

    

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
    participants: Mapped[list[User]] = relationship(
        "User",
        back_populates="event",
        secondary=event_user_association
    )

  

class Comment(Base):
    """
    Модель
    комментария к событию
    - id
    - aвтор комментария (user)
    - текст комментария
    - дата и время комментария
    - прокомментированное событие (event)
    """
    __tablename__ = "comment" 
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    author_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
    event_id: Mapped[Optional[int]]  = mapped_column(Integer,ForeignKey("event.id", ondelete="CASCADE"))
