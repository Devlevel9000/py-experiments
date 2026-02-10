import os

from dotenv import load_dotenv

load_dotenv()

PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_DB = os.getenv("PG_DB")
PG_HOST = os.getenv("PG_HOST")
ENV = os.getenv("ENV", "dev")
SQLITE_DB = f"sqlite:///./{os.getenv('SQLITE_DB')}"
PG_LINK = f"postgresql+asyncpg://{PG_USER}:{PG_PASS}@{PG_HOST}/{PG_DB}"
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_DEV = os.getenv("REDIS_DEV")
