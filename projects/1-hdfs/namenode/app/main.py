from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import json

app = FastAPI()

settings_path = Path(__file__).parent.parent / "settings.json"

@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

@app.get("/datanodes")
def get_datanodes():
    with open(settings_path) as json_file:
        settings = json.load(json_file)
        return {"datanodes": settings["datanodes"]}

