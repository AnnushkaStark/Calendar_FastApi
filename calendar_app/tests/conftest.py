from typing import Generator

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from calendar_app.database import Base, engine
from calendar_app.main import app

from .fixtures import *

@pytest_asyncio.fixture
async def async_session() -> AsyncSession:
    session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with session() as s:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield s

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()



@pytest_asyncio.fixture
async def http_client(
    async_session: AsyncSession,
) -> Generator[AsyncClient, None, None]:
    await startup()
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8000") as ac:
        yield ac
