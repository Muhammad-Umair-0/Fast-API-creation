from fastapi import FastAPI
from pydantic import BaseModel
import json


app = FastAPI()

books = {
    1: {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    2: {"title": "1984", "author": "George Orwell"},
    3: {"title": "Pride and Prejudice", "author": "Jane Austen"},
}


@app.get("/")
def welcome():
    return "Hi welcome to Meri_tech"


# Post Method 
class Book(BaseModel):
    title: str
    author: str

@app.post("/books/")
def create_book(book:Book):
    new_id = max(books.keys()) +1
    books[new_id] = book.dict()
    return {"message": "Book aded successfully"   ,  "book_id":new_id}


#get books with books id
@app.get("/books/{book_id}")
def get_books(book_id: int):
    if book_id in books:
        return books[book_id]
    return "book not found"


#books save to jason
def save_books_to_json():
    file_path = "books.json"
    with open(file_path, 'w') as json_file:
        json.dump(books, json_file, indent=4)
    print(f"Books data saved to {file_path}")

    
#get all books 
@app.get("/all_books/")
def get_all_books():
    return books



@app.get("/save-books/")
def save_all_books():
    save_books_to_json()
    return {"Message": "All books save to json"}