from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class SumRequest(BaseModel):
    x: int
    y: int

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/info")
def read_info():
    return {"studentId": 555, "universityName": "upf"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/sum")
def sum_numbers(request: SumRequest):
    result = request.x + request.y
    return {"result": result}