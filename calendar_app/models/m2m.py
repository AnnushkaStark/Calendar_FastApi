from typing import TYPE_CHECKING, Optional
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Table,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from calendar_app.database import Base

if TYPE_CHECKING:
    from calendar_app.models.user_model import User
    from calendar_app.models.event_model import Event


event_user_association = Table(
    'event_user',
    Base.metadata,
    Column(
        "event_id", Integer, ForeignKey("event.id", ondelete="CASCADE")
    ),
    Column("user_id", Integer, ForeignKey("user.id", ondelete="CASCADE")),
)