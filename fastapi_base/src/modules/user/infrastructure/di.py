from functools import lru_cache
from fastapi import Depends
from typing import Annotated
from src.core import PasswordHasher
from db import get_session
from src.modules.user.infrastructure.user_repository import UserRepository
from src.modules.user.application.services import UserService
from src.modules.user.domain.user_service import AbstractUserService
from sqlalchemy.ext.asyncio import AsyncSession


def get_user_repository(session: AsyncSession = Depends(get_session)) -> UserRepository:
    """Resolve the concrete UserRepository with the provided DB session."""
    return UserRepository(session)


@lru_cache
def get_password_hasher() -> PasswordHasher:
    """Return a singleton PasswordHasher instance."""
    return PasswordHasher()


def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
    password_hasher: PasswordHasher = Depends(get_password_hasher),
) -> AbstractUserService:
    """Assemble and return the concrete UserService implementation."""
    return UserService(repository, password_hasher)


UserSvcDep = Annotated[AbstractUserService, Depends(get_user_service)]
