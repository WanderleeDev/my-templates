from pydantic import BaseModel, ConfigDict, Field


class ResponseMessage(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=100,
        description="Descriptive message about the operation result",
    )

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        json_schema_extra={"example": {"message": "Created successfully"}},
    )
