import os

from fastapi import FastAPI
import uvicorn

from utils.utils import json_to_dict_list
from app.students.schemes import Student as StudentModel

script_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, "students.json")

app = FastAPI()
app.add_route


@app.get("/")
async def home():
    return {"message": "Home page"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
