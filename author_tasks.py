from fastapi import APIRouter, HTTPException
from models import Authors
from typing import List
from beanie import PydanticObjectId
from bson import ObjectId

author_router = APIRouter()

# 2. Author
#- GET /authors: Retrieve all authors
#- POST /authors: Create a new author
#- GET /authors/{id}: Retrieve an author by their ID
#- PUT /authors/{id}: Update an author by their ID
#- DELETE /authors/{id}: Delete an author by their ID

@author_router.get("/",status_code=200)
async def Get_All_Authors() -> List[Authors]:
    authors = await Authors.find_all().to_list()

    return authors

@author_router.post("/", status_code=201)
async def Create_Author(author: Authors):
    
    author_to_check = await Authors.get(author.id)
    if author_to_check:
        return {"message": "ID already registered."}
    
    await author.create()

    return {"message": "New author registered."}

@author_router.get("/{author_id}", status_code=200)
async def Retrieve_Book(author_id: object) -> Authors:
    print(author_id)
    task_to_get = await Authors.get(author_id)

    print(task_to_get)

    return task_to_get

@author_router.put("/{author_id}", status_code=200)
async def Update_Book(author: Authors, author_id: object) -> Authors:

    author_to_update = await Authors.get(author_id)

    if not author_to_update:
        raise HTTPException(status_code=404, detail="Resource not found")

    author_to_update.name = author.name
    author_to_update.nationality = author.nationality

    await author_to_update.save()

    return author_to_update

@author_router.delete("/{author_id}", status_code=204)
async def Delete_Book(author_id: object):
    author_to_delete = await Authors.get(author_id)

    await author_to_delete.delete()

    return {"message": "Author deleted"}