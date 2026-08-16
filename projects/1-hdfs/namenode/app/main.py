from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import json

app = FastAPI()

settings_path = Path(__file__).parent.parent / "settings.json"
checkpoint_path = Path(__file__).parent.parent / "checkpoint.json"

class FileRequest(BaseModel):
    file_name: str


@app.get("/healthcheck")
def healthcheck():
    return {"status": "up"}

@app.get("/datanodes")
def get_datanodes():
    with open(settings_path) as json_file:
        settings = json.load(json_file)
        return {"datanodes": settings["datanodes"]}

@app.post("/files")
def create_file(request: FileRequest):
    if not request.file_name:
        raise HTTPException(status_code=400, detail="File name is required")

    with open(settings_path) as json_file:
        settings = json.load(json_file)
    
    with open(checkpoint_path) as json_file:
        checkpoint = json.load(json_file)

    if request.file_name in checkpoint:
        raise HTTPException(status_code=409, detail="File already exists")

    file_metadata = {
        "file_name": request.file_name,
        "block_size_bytes": settings["block_size_bytes"],
        "blocks": []
    }

    checkpoint[request.file_name] = file_metadata

    with open(checkpoint_path, "w") as json_file:
        json.dump(checkpoint, json_file)

    return file_metadata

