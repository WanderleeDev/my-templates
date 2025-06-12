from typing import Optional, Type, TypeVar, List, override, Dict, Any
from sqlalchemy import delete
from sqlalchemy.sql import select
from db.base_model import BaseModel
from db.session import SessionDep
from src.common.abstracts import AbstractRepository
from uuid import UUID


T = TypeVar("T", bound=BaseModel)


class BaseRepository(AbstractRepository[T]):
    """
    Base class for all repositories
    """

    def __init__(self, session: SessionDep, model: Type[T]):
        """
        Initialize the repository with a session and a model

        Args:
            session (SessionDep): The session to use for database operations
            model (Type[T]): The model to use for database operations
        """

        self.session = session
        self.model = model

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
    async def read(self, entity_id: int) -> Optional[T]:
        """
        Read an entity by its ID

        Args:
            entity_id (int): The ID of the entity to read

        Returns:
            Optional[T]: The entity if found, otherwise None
        """
        return await self.session.get(self.model, entity_id)

    @override
    async def update(self, id: UUID, values: Dict[str, Any]) -> T:
        """
        Update an entity by its ID

        Args:
            id (UUID): The ID of the entity to update
            values (Dict[str, Any]): The values to update

        Returns:
            T: The updated entity
        """

        prev_entity = await self.read(id)

        if not prev_entity:
            raise HTTPException(status_code=404, detail="Entity not found")

        for key, value in values.items():
            if hasattr(prev_entity, key):
                setattr(prev_entity, key, value)

        await self.session.commit()
        await self.session.refresh(prev_entity)

        return prev_entity

    @override
    async def delete(self, entity_id: int) -> bool:
        """
        Delete an entity by its ID

        Args:
            entity_id (int): The ID of the entity to delete

        Returns:
            bool: True if the entity was deleted, otherwise False
        """

        statement = delete(self.model).where(self.model.id, entity_id)
        result = await self.session.execute(statement)
        await self.session.commit()

        return result.rowcount > 0

    @override
    async def read_list(self, skip: int = 0, limit: int = 10):
        """
        Get all entities

        Args:
            skip (int): The number of entities to skip
            limit (int): The number of entities to return

        Returns:
            List[T]: The list of entities
        """

        statement = select(self.model).offset(skip).limit(limit)
        results = await self.session.scalars(statement)

        return results.all()
