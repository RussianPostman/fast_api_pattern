from datetime import datetime

from sqlalchemy import DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from . import BaseModel


class Rate(BaseModel):
    __tablename__ = "rates"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    date_to: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    rate: Mapped[float]

    __table_args__ = (
        UniqueConstraint('name', 'date_to'),
    )
