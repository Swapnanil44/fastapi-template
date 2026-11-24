from fastapi import FastAPI
from fastapi.routing import APIRoute

from backend.app.core.config import Settings
from backend.app.routes import utils


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=Settings.PROJECT_NAME,
    openapi_url=f"{Settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)


app.include_router(utils.router)
