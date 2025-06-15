"""
This class implements the AbstractUserService interface using the UserRepository
and PasswordHasher.

The class provides methods for creating, reading, updating and deleting users.
The methods are implemented using the repository and the password hasher.
"""

from typing import override, List
from uuid import UUID
from src.core import (
    DeleteResourceException,
    NotFoundResourceException,
    ResourceAlreadyExistsException,
    UpdateResourceException,
    CreateResourceException,
)
from src.modules.user.application.schemas import (
    UserCreate,
    UserToDB,
    UserUpdate,
    UserPatch,
)
from src.modules.user.domain.user import User
from src.modules.user.domain.user_service import AbstractUserService
from src.modules.user.infrastructure.user_repository import UserRepository
from src.core import PasswordHasher


class UserService(AbstractUserService):
    """
    This class implements the AbstractUserService interface using the UserRepository
    and PasswordHasher.
    """

    def __init__(self, repository: UserRepository, password_hasher: PasswordHasher):
        """
        Initialize the UserService.

        Args:
        repository (UserRepository): The user repository.
        password_hasher (PasswordHasher): The password hasher.
        """
        self.repository = repository
        self.password_hasher = password_hasher

    @override
    async def create_user(self, user: UserCreate) -> User:
        """
        Create a new user.

        Args:
        user (UserCreate): The user to create.

        Returns:
        User: The created user.

        """
        exist_user = await self.repository.find_by_email(user.email)

        if exist_user is not None:
            raise ResourceAlreadyExistsException(
                f"User with email {user.email} already exists"
            )

        try:
            user_to_db = UserToDB(
                username=user.username,
                email=user.email,
                hashed_password=self.password_hasher.hash(user.password),
            )
            return await self.repository.create(user_to_db)
        except Exception as e:
            raise CreateResourceException(f"User couldn't be created: {e}")

    @override
    async def read_user_by_id(self, id: UUID) -> User:
        """
                Read a user by id.

                Args:
                id (UUID): The id of the user to read.
        j
                Returns:
                User: The read user.

                Raises:
                NotFoundResourceException: If the user is not found.
        """
        user = await self.repository.read(id)

        if user is None:
            raise NotFoundResourceException()

        return user

    @override
    async def update_user(self, id: UUID, user: UserUpdate | UserPatch) -> User:
        """
        Update a user by id.

        Args:
        id (UUID): The id of the user to update.
        user (UserUpdate | UserPatch): The user to update.

        Returns:
        User: The updated user.

        Raises:
        UpdateResourceException: If the user is not updated.
        """
        is_updated = await self.repository.update(
            id, user.model_dump(exclude_unset=True, exclude_none=True)
        )

        if not is_updated:
            raise UpdateResourceException()

        return await self.read_user_by_id(id)

    @override
    async def delete_user(self, id: UUID) -> bool:
        """
        Delete a user by id.

        Args:
        id (UUID): The id of the user to delete.

        Returns:
        bool: True if the user is deleted, False otherwise.

        Raises:
        DeleteResourceException: If the user is not deleted.
        """
        result = await self.repository.delete(id)

        if not result:
            raise DeleteResourceException()

        return result

    @override
    async def list_users(self, offset: int = 0, limit: int = 10) -> List[User]:
        """
        List users with pagination.

        Args:
        offset (int): The offset of the pagination. Defaults to 0.
        limit (int): The limit of the pagination. Defaults to 10.

        Returns:
        List[User]: The list of users.
        """
        return await self.repository.read_list(offset, limit)

    @override
    async def find_user_by_email(self, email: str) -> User:
        """
        Find a user by email.

        Args:
        email (str): The email of the user to find.

        Returns:
        User: The found user.

        Raises:
        NotFoundResourceException: If the user is not found.
        """
        user = await self.repository.find_by_email(email)

        if user is None:
            raise NotFoundResourceException()

        return user
