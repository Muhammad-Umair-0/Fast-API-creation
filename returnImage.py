from fastapi import FastAPI, File, UploadFile
import uuid
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os

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



