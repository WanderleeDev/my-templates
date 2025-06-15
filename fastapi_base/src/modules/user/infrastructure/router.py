from fastapi import APIRouter, Query
from typing import List
from uuid import UUID
from src.core import ResponseMessage
from src.modules.user.application.schemas import (
    UserCreate,
    UserResponse,
    UserUpdate,
    UserPatch,
)
from src.modules.user.infrastructure.di import UserSvcDep

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get(
    "/{id}",
    status_code=200,
    response_model=UserResponse,
    summary="Get user by ID",
    description="Retrieves a single user by their unique identifier.",
)
async def read_user_by_id(id: UUID, user_service: UserSvcDep):
    return await user_service.read_user_by_id(id)


@user_router.get(
    "",
    status_code=200,
    response_model=List[UserResponse],
    summary="List users",
    description="Retrieves a paginated list of users.",
)
async def list_user(
    user_service: UserSvcDep,
    offset: int = Query(0, ge=0, description="Pagination offset"),
    limit: int = Query(10, ge=1, le=100, description="Items per page (max 100)"),
):
    return await user_service.list_users(offset, limit)


@user_router.post(
    "",
    status_code=201,
    response_model=UserResponse,
    summary="Create a new user",
    description="Creates a new user with the provided information.",
)
async def create_user(user: UserCreate, user_service: UserSvcDep):
    return await user_service.create_user(user)


@user_router.patch(
    "/{id}",
    status_code=200,
    response_model=UserResponse,
    summary="Partially update a user",
    description="Updates specific fields of an existing user.",
)
async def patch_user(id: UUID, user: UserPatch, user_service: UserSvcDep):
    return await user_service.update_user(id, user)


@user_router.put(
    "/{id}",
    status_code=200,
    response_model=UserResponse,
    summary="Update a user",
    description="Replaces all user information with the provided data.",
)
async def update_user(id: UUID, user: UserUpdate, user_service: UserSvcDep):
    return await user_service.update_user(id, user)


@user_router.delete(
    "/{id}",
    status_code=200,
    response_model=ResponseMessage,
    summary="Delete a user",
    description="Deletes a user by their ID.",
)
async def delete_user(id: UUID, user_service: UserSvcDep):
    await user_service.delete_user(id)

    return ResponseMessage(message="User deleted successfully")
