import motor
import motor.motor_asyncio
from beanie import init_beanie
from models import Authors, Books


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/"
    )

    await init_beanie(
        database=client.db_name,
        document_models=[Authors, Books]      
    )