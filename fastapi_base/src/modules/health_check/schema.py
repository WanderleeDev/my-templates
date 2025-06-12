from pydantic import BaseModel, ConfigDict


class HealthCheckResponse(BaseModel):
    status: str
    message: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {"status": "ok", "message": "Application is fully functional"}
        },
    )
