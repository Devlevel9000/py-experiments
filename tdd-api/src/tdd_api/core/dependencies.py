from collections.abc import AsyncGenerator, Generator
from typing import Annotated, Any

from fastapi import Depends
from kink import di
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from tdd_api.core.ioc import setup_container

if "env" not in di:
    setup_container()


def get_logger() -> Any:
    return di["log"]


def get_sqlite_session() -> Generator[Session, None, None]:
    session_factory = di["sqlite_session"]
    session = session_factory()
    try:
        yield session
    finally:
        session.close()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = di["async_session"]
    async with session_factory() as session:
        yield session


async def get_redis() -> Any:
    return di["redis"]


Logger = Annotated[Any, Depends(get_logger)]
SqliteSession = Annotated[Any, Depends(get_sqlite_session)]
AsyncDB = Annotated[Any, Depends(get_async_session)]
RedisClient = Annotated[Any, Depends(get_redis)]
