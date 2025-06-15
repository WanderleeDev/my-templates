from typing import Optional, Type, TypeVar, List, override, Union
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio.session import AsyncSession
from db.base_model import BaseModel
from src.core.domain.abstract_repository import AbstractRepository
from uuid import UUID
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchema = TypeVar("CreateSchema")
UpdateSchema = TypeVar("UpdateSchema")
PatchSchema = TypeVar("PatchSchema")


class BaseRepository(
    AbstractRepository[ModelType, CreateSchema, UpdateSchema, PatchSchema]
):
    """
    Base class for all repositories.

    This class provides methods for creating, reading, updating and deleting entities.
    """

    def __init__(self, session: AsyncSession, model_class: Type[ModelType]):
        """
        Initialize the repository with a session and a model.

        Args:
            session (AsyncSession): The session to use for database operations.
            model_class (Type[ModelType]): The model to use for database operations.
        """

        self.session = session
        self.model_class = model_class

    @override
    async def create(self, entity: CreateSchema) -> ModelType:
        """
        Create a new entity.

        Args:
            entity (CreateSchema): The entity to create.

        Returns:
            ModelType: The created entity.
        """
        user_to_db = self.__create_model(entity)
        self.session.add(user_to_db)
        await self.session.commit()
        await self.session.refresh(user_to_db)

        return user_to_db

    @override
    async def read(self, entity_id: Union[UUID, str]) -> Optional[ModelType]:
        """
        Read an entity by its ID.

        Args:
            entity_id (UUID | str): The ID of the entity to read.

        Returns:
            Optional[ModelType]: The entity if found, otherwise None.
        """

        return await self.session.get(self.model_class, self.__to_str_id(entity_id))

    @override
    async def update(
        self, entity_id: Union[UUID, str], values: Union[UpdateSchema, PatchSchema]
    ) -> bool:
        """
        Update an entity by its ID.

        Args:
            entity_id (UUID | str): The ID of the entity to update.
            values (Union[UpdateSchema, PatchSchema]): The values to update.

        Returns:
            bool: True if the entity was updated, otherwise False.
        """

        statement = (
            update(self.model_class)
            .where(self.model_class.id == self.__to_str_id(entity_id))
            .values(**values)
        )
        result = await self.session.execute(statement)
        await self.session.commit()

        return result.rowcount > 0

    @override
    async def delete(self, entity_id: Union[UUID, str]) -> bool:
        """
        Delete an entity by its ID.

        Args:
            entity_id (UUID | str): The ID of the entity to delete.

        Returns:
            bool: True if the entity was deleted, otherwise False.
        """

        statement = delete(self.model_class).where(
            self.model_class.id == self.__to_str_id(entity_id)
        )
        result = await self.session.execute(statement)
        await self.session.commit()

        return result.rowcount > 0

    @override
    async def read_list(self, offset: int = 0, limit: int = 10) -> List[ModelType]:
        """
        Get a list of entities.

        Args:
            offset (int): The number of entities to offset.
            limit (int): The number of entities to return.

        Returns:
            List[ModelType]: The list of entities.
        """

        statement = select(self.model_class).offset(offset).limit(limit)
        results = await self.session.scalars(statement)

        return results.all()

    def __to_str_id(self, id: Union[UUID, str]) -> str:
        """
        Convert an ID to a string.

        Args:
            id (UUID | str): The ID to convert.

        Returns:
            str: The ID as a string.
        """

        return str(id)

    def __create_model(self, schema: BaseModel) -> ModelType:
        """
        Create a model from a create schema.

        Args:
            schema (CreateSchema): The schema to create.

        Returns:
            ModelType: The created model.
        """

        return self.model_class(**schema.model_dump(exclude_unset=True))
