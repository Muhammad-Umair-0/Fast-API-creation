from fastapi import FastAPI
from enum import Enum
from pathlib import Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: float):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return{"user_id": "The current user"}
    
@app.get("/users/{user_id}")
async def read_user_me(user_id: str):
    return{"user_id": "user_id"}


# creating a class Enum for predeifned perameters
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "deep learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images!"}
    
    return {"model_name": model_name, "message": "Have Some residuals!"}



# reading the files 
app.get("/files/{file_path:path}")
async def read_files(file_path: str):
    path = Path(file_path)
    if path.exists():
        return {"file_path": str(path), "exists": True}
    else:
        return {"file_path": str(path), "exists": False}
