from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped ,mapped_column, relationship
from sqlalchemy import (
    Integer,
    String,
) 
from sqlalchemy.orm import relationship

from calendar_app.database import Base

if TYPE_CHECKING:
    from models.event_model import Event


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
    events: Mapped[list["Event"]] =relationship(
        "Event",
        secondary="user_event_association",
        back_populates="participants",
    )

    def __repr__(self) -> str:
        return f"{self.id}: {self.nickname}"
