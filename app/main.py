from fastapi import FastAPI
import uvicorn

from students.router import router

app = FastAPI()
app.include_router(router)


@app.get('/')
async def home():
    return {'message': 'Home page'}


if __name__ == '__main__':
    uvicorn.run('app.main:app', host='127.0.0.1', port=8000, reload=True)
