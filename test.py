import requests


def get_all_students(course: int):
    url = "http://127.0.0.1:8000/students/{course}"
    response = requests.get(url)
    return response.json()


def get_students_with_param_max(
    course: int, major: str | None, enrollment_year: int | None
):
    url = f"http://127.0.0.1:8000/students/{course}"

    params = {}
    if major:
        params["major"] = major
    if enrollment_year:
        params["enrollment_year"] = enrollment_year

    print(params)

    response = requests.get(url, params=params)
    return response.json()


# students = get_all_students()
# for i in students:
#     print(i)

students = get_students_with_param_max(4, major="Биология", enrollment_year=2016)
print(students)
