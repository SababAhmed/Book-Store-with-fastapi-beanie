from fastapi import APIRouter, HTTPException
from models import Authors, Books
from typing import List
from beanie import PydanticObjectId
from bson import ObjectId

interaction_router = APIRouter()
### 3. Interaction
# - GET /authors/{id}/books: Retrieve all books from a specific author
# - GET /books/{id}/author: Retrieve the author of a specific book

# @interaction_router.get("/{author_id}", status_code=200)
# async def Get_All_Book() -> List[Books]:
#     books = await Books.find_all(Books.author_id).to_list()

#     return books

@interaction_router.get("/{author_id}", status_code=200)
async def Retrieve_a_Book_of_Author(author_id: object) -> Books:


    book_to_get = await Books.find_one(Books.author_id == author_id)

    return book_to_get

# @interaction_router.get("/{book_id}", status_code=200)
# async def Retrieve_Author_of_book(book_id: object) -> Books:

#     z =[]
#     x = await Books.find_one(Books.id == book_id)

#     return x

# @interaction_router.get("/{book_id}", status_code=200)
# async def Retrieve_Book_Author(book_id: object) -> Books:

#     book_to_get = await Books.find(Books.id == book_id)
#     # book_to_get = []
#     # for x in Books.find(Books.id == book_id):
#     #     await book_to_get.append(x)
#     return book_to_get

