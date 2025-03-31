# @app.get("/students")
# async def get_all_students(course: int | None = None) -> list[StudentModel]:
#     students = json_to_dict_list(path_to_json)
#     if course is None:
#         return students
#     else:
#         result = []
#         for student in students:
#             if student["course"] == course:
#                 result.append(student)

#         return result


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

# @app.get('/students/{id}')
# async def get_student_by_id(id: int) -> StudentModel | None:
#     students: list[StudentModel] = json_to_dict_list(path_to_json)
#     for student in students:
#         if student['student_id'] == id:
#             return student
#     return None
