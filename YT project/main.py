from fastapi import FastAPI


app  = FastAPI()



@app.get("/")
async def index():
    # return {'data': {"name":"Umair"}}
    return {'data': 'blog list'}
    # a = input("Enter a number ")
    # return {"a"}
    # return {"sum": 2+4}

@app.get("/blog")
async def index(limit = 10,published:bool= True):
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
async def comments(id):
    # fetch comments og blog with id = id 
    return {'data': {'1','2','3'}}


