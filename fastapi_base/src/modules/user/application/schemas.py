from pydantic import BaseModel, EmailStr, ConfigDict, model_validator, Field
from typing import Optional
from src.core import model_config_base, PydanticBaseModel


class UserBase(BaseModel):
    username: str = Field(description="User username", min_length=3, max_length=16)
    email: EmailStr = Field(description="User email")


class UserUpdate(UserBase):
    model_config = model_config_base | ConfigDict(
        json_schema_extra={
            "example": {
                "username": "john_doe",
                "email": "john.doe@example.com",
            }
        },
    )


class UserPatch(BaseModel):
    username: Optional[str] = Field(
        description="User username", min_length=3, max_length=16
    )
    email: Optional[EmailStr] = Field(description="User email")

    model_config = model_config_base | ConfigDict(
        json_schema_extra={
            "example": {
                "username": "john_doe",
                "email": "john.doe@example.com",
            }
        },
    )


class UserCreate(UserBase):
    password: str = Field(
        description="User password (min 8 chars, 1 uppercase, 1 lowercase, 1 number, 1 special char)",
        min_length=8,
        max_length=16,
        example="SecurePass123!",
    )
    confirm_password: str

    @model_validator(mode="after")
    def password_check(self):
        if self.password != self.confirm_password:
            raise ValueError("passwords do not match")
        return self

    model_config = model_config_base | ConfigDict(
        json_schema_extra={
            "example": {
                "username": "john_doe",
                "email": "john.doe@example.com",
                "password": "password123",
                "confirm_password": "password123",
            }
        },
    )


class UserToDB(UserBase):
    hashed_password: str

    model_config = model_config_base | ConfigDict(
        json_schema_extra={
            "example": {
                "username": "john_doe",
                "email": "john.doe@example.com",
                "hashed_password": "password123",
            }
        },
    )


class UserResponse(PydanticBaseModel, UserBase):
    model_config = model_config_base | ConfigDict(
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "username": "john_doe",
                "email": "john.doe@example.com",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
            }
        }
    )
