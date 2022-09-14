import asyncio

from tortoise import Tortoise

from config import config


async def init():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url=config().db_url,
        modules={'models': ['dal.attach', 'dal.platforms']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


asyncio.ensure_future(init())
