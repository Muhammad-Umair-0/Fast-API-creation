from fastapi import FastAPI

app = FastAPI()

food_items = {
    'indian' : ["samosa", "Dosa"],
    'american': ["hot Dog", "apple pie"],
    'italian' : ["Ravioli", "Pizza"]
}

@app.get("/")
async def root():
    return {"message: Hello Word"}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return food_items.get(cuisine)


@app.get("/hello/{name}")
async def hello(name): 
    return f"welcome {name}"








@app.get("/age")
async def hello():
    return ("i am 24 year old")



