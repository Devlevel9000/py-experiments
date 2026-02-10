from sqlalchemy import DATETIME, Boolean, Integer, String, Text
from sqlalchemy.orm import MappedColumn, mapped_column

from ..core.base_model import Base


class Book(Base):
    __tablename__ = "books"

    id: MappedColumn[Integer] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False
    )
    name: MappedColumn[String] = mapped_column(nullable=False)
    description: MappedColumn[Text] = mapped_column(nullable=False)
    sku: MappedColumn[String] = mapped_column(nullable=False)
    published: MappedColumn[Boolean] = mapped_column(nullable=False, default=True)
    published_at: MappedColumn[DATETIME] = mapped_column(nullable=True)
