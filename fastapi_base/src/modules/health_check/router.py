from fastapi import APIRouter, status
from src.modules.health_check.schema import HealthCheckResponse

health_check_router = APIRouter(prefix="/health_check", tags=["Health Check"])


@health_check_router.get(
    "", status_code=status.HTTP_200_OK, response_model=HealthCheckResponse
)
def health_check():
    return HealthCheckResponse(status="ok", message="Application is fully functional")
