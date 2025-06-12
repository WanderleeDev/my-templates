from typing import Optional, Type, TypeVar, List, override, Dict, Any
from sqlalchemy import select, update, delete
from db.base_model import BaseModel
from db.session import SessionDep
from src.common.abstracts import AbstractRepository
from uuid import UUID


T = TypeVar("T", bound=BaseModel)


class BaseRepository(AbstractRepository[T]):
    """
    Base class for all repositories
    """

    def __init__(self, session: SessionDep, model_class: Type[T]):
        """
        Initialize the repository with a session and a model

        Args:
            session (SessionDep): The session to use for database operations
            model (Type[T]): The model to use for database operations
        """

        self.session = session
        self.model_class = model_class

    @override
    async def create(self, entity: T) -> T:
        """
        Create a new entity

        Args:
            entity (T): The entity to create

        Returns:
            T: The created entity
        """

        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)

        return entity

    @override
    async def read(self, entity_id: UUID) -> Optional[T]:
        """
        Read an entity by its ID

        Args:
            entity_id (UUID): The ID of the entity to read

        Returns:
            Optional[T]: The entity if found, otherwise None
        """
        return await self.session.get(self.model_class, entity_id)

    @override
    async def update(self, id: UUID, values: Dict[str, Any]) -> bool:
        """
        Update an entity by its ID

        Args:
            id (UUID): The ID of the entity to update
            values (Dict[str, Any]): The values to update

        Returns:
            bool: True if the entity was updated, otherwise False
        """

        statement = update(self.model_class).where(self.model_class.id == id).values(**values)
        result = await self.session.execute(statement)
        await self.session.commit()

        return result.rowcount > 0


    @override
    async def delete(self, entity_id: UUID) -> bool:
        """
        Delete an entity by its ID

        Args:
            entity_id (int): The ID of the entity to delete

        Returns:
            bool: True if the entity was deleted, otherwise False
        """
        statement = delete(self.model_class).where(self.model_class.id == entity_id)
        result = await self.session.execute(statement)
        await self.session.commit()

        return result.rowcount > 0

    @override
    async def read_list(self, skip: int = 0, limit: int = 10) -> List[T]:
        """
        Get all entities

        Args:
            skip (int): The number of entities to skip
            limit (int): The number of entities to return

        Returns:
            List[T]: The list of entities
        """

        statement = select(self.model_class).offset(skip).limit(limit)
        results = await self.session.scalars(statement)

        return results.all()
