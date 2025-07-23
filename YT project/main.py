from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app  = FastAPI()



@app.get("/")
async def index():
    # return {'data': {"name":"Umair"}}
    return {'data': 'blog list'}
    # a = input("Enter a number ")
    # return {"a"}
    # return {"sum": 2+4}

@app.get("/blog")
async def index(limit = 10,published:bool= True, sort:Optional[str]=None):
    return published
    if published:
        return {'data': f'{limit} published blog from DB'}
    else:
        return {'data': f'{limit} blog from DB'}


@app.get("/blog/unpublished")
def unpublished():
    return {'data': "all unpublished "}


@app.get("/blog/{id}")
async def show(id : int ):
    # fetch blod with id = id
    return {'data': id}




@app.get('/blog/{id}/comments')
async def comments(id, limit=10):
    # fetch comments og blog with id = id 
    return {'data': {'1','2','3'}}



class Blog(BaseModel):
    # id : float = 0.23
    title :str
    body : str
    published : Optional[bool]



@app.post('/blog')
def create_blog(blog:Blog):
    return {'data': f"Blog is created with title as {blog.title}"}


