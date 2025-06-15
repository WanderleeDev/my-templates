from typing import Any, List, Dict
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from datetime import datetime
from typing import Optional


class PydanticBaseModel(BaseModel):
    id: UUID = Field(description="Unique identifier")
    created_at: datetime = Field(description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Update date")


class PydanticError(BaseModel):
    type: str = Field(description="Type of error")
    loc: List[str] = Field(description="Location of error")
    msg: str = Field(description="Error message")
    input: str = Field(description="Invalid input")
    ctx: Dict[str, Any] = Field(description="Context of error")

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        json_schema_extra={
            "example": {
                "detail": [
                    {
                        "type": "value",
                        "loc": ["loc"],
                        "msg": "msg",
                        "input": "input",
                        "ctx": {"ctx": "ctx", "ctx2": "ctx2", "ctx3": "ctx3"},
                    }
                ],
                "body": {"value": "value", "value2": "value2", "value3": "value3"},
            }
        },
    )


class PydanticErrorExtended(BaseModel):
    detail: List[PydanticError] = Field(description="List of validation errors")
    body: Dict[str, Any] = Field(description="Request body")

    model_config = ConfigDict(
        from_attributes=True,
        extra="ignore",
        json_schema_extra={
            "example": {
                "detail": [
                    {
                        "type": "value",
                        "loc": ["loc"],
                        "msg": "msg",
                        "input": "input",
                        "ctx": {"ctx": "ctx", "ctx2": "ctx2", "ctx3": "ctx3"},
                    }
                ],
                "body": {"value": "value", "value2": "value2", "value3": "value3"},
            }
        },
    )


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
