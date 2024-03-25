from datetime import datetime
from typing import  Optional, TYPE_CHECKING

from sqlalchemy.orm import Mapped ,mapped_column
from sqlalchemy import (
    Integer,
    DateTime,
    ForeignKey,
    func,
) 

from calendar_app.database import Base

MIN_COMMENT_LENGTH = 2
MAX_COMMENT_LENGTH = 1000


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
    
    def __repr__(self) -> str:
        return f"{self.id} {self.author_id}"