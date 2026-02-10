from kink import di
from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from tdd_api.config import ENV, PG_LINK, REDIS_DEV, SQLITE_DB

from .logging_config import configure_logging


def setup_container(env: str = "production") -> None:
    env = ENV
    async_engine = create_async_engine(
        PG_LINK if env == "production" else "sqlite+aiosqlite:///:memory:"
    )

    di["log"] = configure_logging()

    sqlite_engine = create_engine(SQLITE_DB)
    di["sqlite_session"] = sessionmaker(bind=sqlite_engine)

    di["async_session"] = async_sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )

    if env == "production" or env == "development":
        di["redis"] = Redis(host="localhost", port=6379, decode_responses=True)
    elif env == "test":
        di["redis"] = None
    else:
        di["redis"] = None  # Defaultdi["env"] = env

    di["redis"] = (
        Redis(host="localhost", port=6379, decode_responses=True)
        if env == "production" or REDIS_DEV
        else None
    )

    di["env"] = env
