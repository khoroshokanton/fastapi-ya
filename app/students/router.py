from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from .schemes import Student as StudentSchema
import app.students.service as service

router = APIRouter(prefix='/students', tags=['Студенты'])


@router.get('/')
async def get_all_students(
    session: AsyncSession = Depends(get_session),
) -> list[StudentSchema]:
    return await service.get_all_students(session=session)


@router.get('/{id}')
async def get_student_by_id(
    id: int, session: AsyncSession = Depends(get_session)
) -> StudentSchema | None:
    return await service.get_student_by_id(id=id, session=session)


# # @app.get("/students/{course}")
# # async def get_all_students_course(
# #     course: int, major: str | None = None, enrollment_year: int | None = 2018
# # ):
# #     students = json_to_dict_list(path_to_json)
# #     filtered_students = []
# #     for student in students:
# #         if student["course"] == course:
# #             filtered_students.append(student)

# #     if major:
# #         filtered_students = [
# #             student for student in filtered_students if student["major"] == major
# #         ]

# #     print(filtered_students)

# #     if major:
# #         filtered_students = [
# #             student
# #             for student in filtered_students
# #             if student["enrollment_year"] == enrollment_year
# #         ]

# #     return filtered_students
