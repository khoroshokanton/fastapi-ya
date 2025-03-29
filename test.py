# import requests


# def get_all_students(course: int):
#     url = "http://127.0.0.1:8000/students/{course}"
#     response = requests.get(url)
#     return response.json()


# def get_students_with_param_max(
#     course: int, major: str | None, enrollment_year: int | None
# ):
#     url = f"http://127.0.0.1:8000/students/{course}"

#     params = {}
#     if major:
#         params["major"] = major
#     if enrollment_year:
#         params["enrollment_year"] = enrollment_year

#     print(params)

#     response = requests.get(url, params=params)
#     return response.json()


# # students = get_all_students()
# # for i in students:
# #     print(i)

# students = get_students_with_param_max(4, major="Биология", enrollment_year=2016)
# print(students)


from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel): 
    model_config = ConfigDict(extra='allow')
    name: str 
    age: int = Field(18)
    # skills: list = Field(default_factory=lambda data: data['age'] * 2)
    
# user1 = User(name='Anton', x='hello')

# print(user1)

from pydantic import ValidationError
from app.students.models import Student
from datetime import date

student_data = {
    "student_id": 1,
    "phone_number": "+1234567890",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_of_birth": date(2000, 1, 1),
    "email": "ivan.ivanov@example.com",
    "address": "Москва, ул. Пушкина, д. Колотушкина",
    "enrollment_year": 2022,
    "major": "Информатика1",
    "course": 3,
    "special_notes": "Увлекается программированием"
}

def test_valid_student(data: dict) -> None: 
    try: 
        student = Student(**data)
        print(student)
    except ValidationError as e: 
        print(f'Ошибка валидации {e}')


test_valid_student(student_data)

# from dataclasses import dataclass, field

# @dataclass()
# class Book: 
#     name: str = field(default_factory=[])
    
# @dataclass()
# class Book2: 
#     name: str = field(default_factory=[])    
    
# book1 = Book(name='Lord of Rings')
# print(book1.name)


    
# book2 = Book2(name='Lords')
# print(book2.name)

# @dataclass
# class BaseBook:
#     title: any = 'Test'
#     author: str = None

# @dataclass
# class Book(BaseBook):
#     desc: str = None
#     title: str = "Unknown"
    
# book = Book(desc='hello')
# print(book)

