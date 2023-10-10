from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(32), unique=True)
    description: Mapped[str]
    price: Mapped[int]