from fastapi import FastAPI
 

app = FastAPI()



items = {
    1: {"name": "Apple", "price": 50},
    2: {"name": "Banana", "price": 20}
}

@app.get("/")
def root():
    return "Hey welcome to items list"

# get the item id 
@app.get("/item{item_id}/")
def get_item(item_id:int):
    if item_id in items:
        return items[item_id]
    return "item not found"

# adding new item by post method
@app.post("/items/")
def add_item(name: str, price: int):
    new_id = max(items.keys())+1
    items[new_id] = {"name": name, "price": price}
    return {"message": "Item updated", "item": items[new_id]}
# modified patch
@app.patch("/items/{item_id}")
def patch_item(item_id: int, name: str = None, price: int = None):
    if item_id in items:
        if name:
            items[item_id]["name"] = name
        if price:
            items[item_id]["price"] = price
        return {"message": "Item partially updated", "item": items[item_id]}
    return {"error": "Item not found"}

# delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        deleted = items.pop(item_id)
        return {"message": "Item deleted", "item": deleted}
    return {"error": "Item not found"}

@app.put("/item{item_id}")
def update_item(item_id:int, name:str, price:int):
    if item_id in items:
        items[item_id] = {"name": name, "price": price}
        return "items are updated"
    











# get all items 
@app.get("/all_items/")
def all_items():
    return items