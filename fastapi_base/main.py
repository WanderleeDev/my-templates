from fastapi import FastAPI
from src.core import settings
from src.modules.health_check import health_check_router

app = FastAPI(
    version=settings.APP_VERSION,
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    root_path=f"/api/{settings.APP_VERSION}",
)

app.include_router(health_check_router, prefix="/health_check", tags=["Health Check"])
