from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path



# creating app instant 
app  = FastAPI()

@app.get("/get_image")
async def get_image():
    image_path = Path(".\\pic.jpg")
    

    if not image_path.is_file():
        return {"error" : "Image not found on the server"}
    
    return FileResponse


