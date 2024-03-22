from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./calendar.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)

async_session = async_sessionmaker(engine)


Base = declarative_base()

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
    