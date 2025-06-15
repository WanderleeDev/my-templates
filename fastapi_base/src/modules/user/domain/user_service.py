from abc import ABC, abstractmethod
from typing import List
from src.modules.user.application.schemas import UserCreate, UserUpdate, UserPatch
from src.modules.user.domain.user import User
from uuid import UUID


class AbstractUserService(ABC):
    @abstractmethod
    async def create_user(self, user: UserCreate) -> User:
        """Create a new user"""
        pass

    @abstractmethod
    async def read_user_by_id(self, id: UUID) -> User:
        """Read a user by id"""
        pass

    @abstractmethod
    async def update_user(self, id: UUID, user: UserUpdate | UserPatch) -> User:
        """Update a user by id"""
        pass

    @abstractmethod
    async def delete_user(self, id: UUID) -> bool:
        """Delete a user by id"""
        pass

    @abstractmethod
    async def list_users(self, offset: int = 0, limit: int = 10) -> List[User]:
        """List users with pagination"""
        pass

    @abstractmethod
    async def find_user_by_email(self, email: str) -> User:
        """Find a user by email"""
        pass
