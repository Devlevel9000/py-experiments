from typing import Annotated, Any

from fastapi import Depends
from kink import di

from tdd_api.core.ioc import setup_container

if "log" not in di:
    setup_container()


def get_logger() -> Any:
    return di["log"]


Logger = Annotated[Any, Depends(get_logger)]
