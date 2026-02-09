from kink import di

from .logging_config import configure_logging


def setup_container() -> None:
    di["log"] = configure_logging()
