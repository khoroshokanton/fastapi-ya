from app.core.base import Base

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column


class Major(Base):
    major_name: Mapped[str] = mapped_column(unique=True)
    major_description: Mapped[str] = mapped_column(nullable=True)
    count_students: Mapped[int] = mapped_column(server_default=text("0"))
