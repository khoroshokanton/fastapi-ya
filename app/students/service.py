from sqlalchemy.ext.asyncio import AsyncSession

from .schemes import Student


async def get_all_students(session: AsyncSession) -> list[Student]:
    return []


async def get_student_by_id(id: int, session: AsyncSession) -> Student | None:
    return None
