from tortoise import Tortoise

from ..config import _DB_URL_


async def init():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models"
    await Tortoise.init(
        db_url=_DB_URL_,
        modules={'models': ['app.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
