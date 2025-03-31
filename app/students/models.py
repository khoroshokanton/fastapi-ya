from datetime import date
from typing import TYPE_CHECKING

from app.core.base import Base

from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from ..majors.models import Major


class Student(Base):
    phone_number: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    date_of_birth: Mapped[date]
    email: Mapped[str] = mapped_column(unique=True)
    address: Mapped[str] = mapped_column(Text, nullable=False)
    enrollment_year: Mapped[int]
    course: Mapped[int]
    special_notes: Mapped[str] = mapped_column(nullable=True)
    major_id: Mapped[int] = mapped_column(ForeignKey('majors.id'), nullable=False)

    major: Mapped['Major'] = relationship('Major', back_populates='students')
