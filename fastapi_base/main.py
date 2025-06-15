from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.core import settings, init_sentry, PydanticErrorExtended
from src.modules.health_check import health_check_router
from src.modules.user import user_router
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)


# init_sentry()

app = FastAPI(
    version=settings.APP_VERSION,
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    root_path=f"/api/{settings.APP_VERSION}",
    # responses={422: {"model": PydanticErrorExtended}},
)


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(
    _request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder(
            PydanticErrorExtended(detail=exc.errors(), body=exc.body)
        ),
    )


app.include_router(health_check_router)
app.include_router(user_router)
