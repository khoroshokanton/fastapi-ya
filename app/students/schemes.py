from enum import StrEnum
from datetime import date, datetime
import re

from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError


class Major(StrEnum):
    informatics = "Информатика"
    economics = "Экономика"
    law = "Право"
    medicine = "Медицина"
    engineering = "Инженерия"
    languages = "Языки"


class Student(BaseModel):
    student_id: int
    first_name: str = Field(default=..., min_length=1, max_length=50)
    last_name: str = Field(default=..., min_length=1, max_length=50)
    date_of_birth: date
    email: EmailStr
    phone_number: str = Field(
        default=..., description="Номер телефона в международном формате"
    )
    address: str = Field(default=..., min_length=10, max_length=200)
    enrollment_year: int = Field(ge=2002)
    major: Major
    course: int = Field(default=..., ge=1, le=5)
    special_notes: str | None = Field(default=None, max_length=500)

    # @field_validator('phone_number')
    # @classmethod
    # def validate_phone_number(cls, value: str) -> str:
    #         if not re.match(r'^\+\d{1,15}$', value):
    #             raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
    #         return value

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value: date) -> date:
        if value and value >= datetime.now().date():
            raise ValueError("Дата рождения должна быть в прошлом")
        return value
