from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# by the same way declare optional perameter Query

@app.get("/items/{item_id}")
async def read_item(item_id: str , q: str | None=None):
    if q :
        return {"item_id" :  item_id, "q":q}
    return {"item_id" : item_id}


from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# multiple path and Query errors
@app.get("users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id:int, item_id:str, q:str |None=None,short: bool = False
):
    item = {"item_id": item_id, "owner_id":user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}

        )
    return item