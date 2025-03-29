import os

from fastapi import FastAPI
import uvicorn

from utils import json_to_dict_list

script_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, "students.json")

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Home page"}


@app.get("/students")
async def get_all_students(course: int | None = None):
    students = json_to_dict_list(path_to_json)
    if course is None:
        return students
    else:
        result = []
        for student in students:
            if student["course"] == course:
                result.append(student)

        return result


@app.get("/students/{course}")
async def get_all_students_course(
    course: int, major: str | None = None, enrollment_year: int | None = 2018
):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [
            student for student in filtered_students if student["major"] == major
        ]

    print(filtered_students)

    if major:
        filtered_students = [
            student
            for student in filtered_students
            if student["enrollment_year"] == enrollment_year
        ]

    return filtered_students


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
