from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
