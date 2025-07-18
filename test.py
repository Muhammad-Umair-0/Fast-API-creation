from fastapi import FastAPI


app  = FastAPI()

@app.get("/item")
async def basic():
    return "hello"