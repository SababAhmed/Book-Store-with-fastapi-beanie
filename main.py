from fastapi import FastAPI
from author_tasks import author_router
from book_tasks import book_router
from interaction import interaction_router
from database import init_db

tags_metadata = [
    {
        "name": "Authors",
        "description": "Edit Authors Database.",
    },
    {
        "name": "Books",
        "description": "Edit Books Database.",
    },
    {
       "name": "Interactions",
    }
]

app = FastAPI(
    title="Books & Author",
    description = "This is a simple API for Books and Author registration.",
    openapi_tags=tags_metadata
)


@app.on_event('startup')
async def connect():
    await init_db()

app.include_router(author_router,prefix='/authors',tags=["Authors"])

app.include_router(book_router,prefix='/books',tags=["Books"])

app.include_router(interaction_router,prefix='/interactions',tags=["Interactions"])