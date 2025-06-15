from pydantic import EmailStr, Field, ConfigDict
from src.core import BaseEntity, model_config_base


class User(BaseEntity):
    username: str = (Field(description="User name", min_length=3, max_length=50),)

    hashed_password: str = (
        Field(description="User hashed password", min_length=128, max_length=128),
    )

    email: EmailStr = Field(description="User email")

    model_config = model_config_base | ConfigDict(
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "username": "john_doe",
                "hashed_password": "password123",
                "email": "john.doe@example.com",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }
    )
