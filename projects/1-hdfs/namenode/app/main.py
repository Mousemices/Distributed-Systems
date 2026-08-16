from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

