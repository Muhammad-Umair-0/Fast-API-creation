from importlib.resources import files
from fastapi import FastAPI, File, UploadFile
import uuid
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os
from random import randint

IMAGE_DIR = "./Results"

# Ensure the image directory exists
os.makedirs(IMAGE_DIR, exist_ok=True)

# creating app instant 
app  = FastAPI()

# Mount the static files directory
app.mount("/Results", StaticFiles(directory=IMAGE_DIR), name="Results")

@app.get("/")
def root():
    return {"Hello": "world"}


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):

    filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()


    # save the file 
    file_path = os.path.join(IMAGE_DIR, filename)
    with open(file_path, "wb") as f:
        f.write(contents)

    # Return the image URL
    image_url = f"/Results/{filename}"
    return {"filename": filename, "url": image_url}

@app.get("/show")
async def read_file():
    # get file from image directory
    files = os.listdir(IMAGE_DIR)
    if not files:
        return {"error": "No images found."}
    random_index = randint(1, len(files)-1)
    
    path = f"{IMAGE_DIR}/{files[random_index]}"
    return FileResponse(path)
    # return FileResponse(path, media_type='image/jpeg', filename=files[random_index])

