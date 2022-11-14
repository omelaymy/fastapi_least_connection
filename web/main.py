from fastapi import FastAPI
from time import sleep

app = FastAPI()


@app.get("/health/", status_code=200)
async def i_am_alive():
    return 'I am alive'


@app.get("/")
async def hello():
    sleep(2)
    return {"Hello": "World"}
