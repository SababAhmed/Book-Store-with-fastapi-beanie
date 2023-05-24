from fastapi import APIRouter, HTTPException
from models import Authors,Books
from typing import List
from beanie import PydanticObjectId
from bson import ObjectId

book_router = APIRouter()

@book_router.get("/",status_code=200)
async def Get_All_Books() -> List[Books]:
    books = await Books.find_all().to_list()

    return books

@book_router.post("/", status_code=201)
async def Create_Book(book: Books):
    
    book_to_check = await Books.get(book.id)
    if book_to_check:
        return {"message": "ID already registered."}
    
    author_to_check = await Authors.get(book.author_id)
    if author_to_check:
        return {"message": "Author already registered."}

    await book.create()

    return {"message": "New Book registered."}

@book_router.get("/{book_id}", status_code=200)
async def Retrieve_Book(book_id: object) -> Books:

    task_to_get = await Books.get(book_id)

    print(task_to_get)

    return task_to_get

@book_router.put("/{book_id}", status_code=200)
async def Update_Book(book: Books, book_id: object) -> Books:

    book_to_update = await Books.get(book_id)

    if not book_to_update:
        raise HTTPException(status_code=404, detail="Resource not found")

    book_to_update.title = book.title
    book_to_update.author_id = book.author_id
    book_to_update.publication_year = book.publication_year
    book_to_update.isbn = book.isbn
    book_to_update.stock = book.stock

    await book_to_update.save()

    return book_to_update

@book_router.delete("/{book_id}", status_code=204)
async def Delete_Book(book_id: object):
    book_to_delete = await Books.get(book_id)
    await book_to_delete.delete()

    return {"message": "Book deleted"}

