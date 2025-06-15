from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.core import BaseRepository
from src.modules.user.infrastructure.models import User
from src.modules.user.application.schemas import UserUpdate, UserPatch, UserToDB


class UserRepository(BaseRepository[User, UserToDB, UserUpdate, UserPatch]):
    """
    This class implements the repository pattern for the User model.
    It provides methods for creating, reading, updating and deleting users.
    """

    def __init__(self, session: AsyncSession):
        """
        Initialize the UserRepository.

        Args:
        session (AsyncSession): The session to use for database operations.
        """
        super().__init__(session, User)

    async def find_by_email(self, email: str) -> Optional[User]:
        """
        Find a user by email.

        Args:
        email (str): The email of the user to find.

        Returns:
        User: The found user, or None if the user is not found.
        """
        statement = select(self.model_class).where(self.model_class.email == email)
        return await self.session.scalar(statement)
