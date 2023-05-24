from beanie import Document
from datetime import datetime
from pydantic import Field
#from typing import Annotated

class Authors(Document):
    id: object
    name: str = Field(max_length=350)
    dob: datetime = datetime.now() 
    nationality: str

    class Setting:
        name = "authors_database"

    class config:
        schema_extra = {
            "id": "182nhag24",
            "name": "John Doe",
            "dob": datetime.now(),
            "nationality": "British"
        }

class Books(Document):
    id: object
    title: str = Field(max_length=350)
    author_id:object
    publication_year:int
    isbn: str
    stock: int

    class Setting:
        name = "books_database"

    class config:
        schema_extra = {
            "id": "dh123hi",
            "title": "Value of Copper",
            "author_id": "182nhag24",
            "publication_year": "2018",
            "isbn":"978-3-16-148410-0",
            "stock": "3"
        }