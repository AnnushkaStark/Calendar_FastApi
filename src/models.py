from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    CheckConstraint,
    Enum,
    DateTime,
    Table,
    ForeignKey,
    func,
) 
from sqlalchemy.orm import relationship

from src.constants import EventPriority, EventType


Base =declarative_base()


class User(Base):
    """
    Временная таблица
    пользователей
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, Index=True)
    username =Column(
        String(50), CheckConstraint(
            "length(username)>=3",
            name="username_length_check"
        )
    )
    email = Column(
        String(50), CheckConstraint(
        "length(email) >= 5",
        name='email_length_check'
        ), 
        CheckConstraint(
            "email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z]{2,}$'",
            name='email_format_check'
        )
    )
    password = Column(
        String(50), CheckConstraint(
        "length(pasword) >= 5",
        name='password_format_check'
        )
    )

# Ассоциативная таблица для связи между Event и User
event_user_association = Table(
    'event_user',
    Base.metadata,
    Column('event_id', Integer, ForeignKey('event.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
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
    - описание
    - Владелец 
    - Участники
    """
    __tablename__ = "event" 

    id = Column(Integer, primary_key=True, Index=True)
    name = Column(
        String(100), CheckConstraint(
        "length(name) >= 5",
        name='name_format_check'
        )
    )
    category = Column(
        Enum(EventType),
        nullable=False,
        default=EventType.no_category
    ) 
    priority= Column(
        Enum(EventPriority),
        nullable=False,
        default=EventPriority.without_priority
    )  

    event_location =Column(
        String(100), CheckConstraint(
        "length(event_location) >= 5",
        name='location_format_check'
        )
    )
    organizer = Column(String(100), nullable=True)

    start_time = Column(
        DateTime,
        nullable=False,
        default=func.now()
    )
    end_time = Column(
        DateTime,
        nullable=False,
        default=func.now()
    )
    description = Column(String(3000), nullable=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship("User", back_populates="owned_events") 
    participants = relationship(
        "User",
        secondary=event_user_association,
        back_populates="participated_events"
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
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    text = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)

    author = relationship('User', back_populates='comments')
    event = relationship('Event', back_populates='comments')