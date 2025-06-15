from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, List, Union
from uuid import UUID
from db.base_model import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchema = TypeVar("CreateSchema")
UpdateSchema = TypeVar("UpdateSchema")
PatchSchema = TypeVar("PatchSchema")


class AbstractRepository(
    ABC, Generic[ModelType, CreateSchema, UpdateSchema, PatchSchema]
):
    """
    This class defines the contract that all repository implementations
    must follow for CRUD operations.
    """

    @abstractmethod
    def create(self, entity: CreateSchema) -> ModelType:
        """Create an entity"""
        pass

    @abstractmethod
    def read(self, entity_id: Union[UUID, str]) -> Optional[ModelType]:
        """Read an entity by its ID"""
        pass

    @abstractmethod
    def update(
        self, entity_id: Union[UUID, str], values: Union[UpdateSchema, PatchSchema]
    ) -> bool:
        """Update an entity by its ID"""
        pass

    @abstractmethod
    def delete(self, entity_id: Union[UUID, str]) -> bool:
        """Delete an entity by its ID"""
        pass

    @abstractmethod
    def read_list(self, skip: int = 0, limit: int = 10) -> List[ModelType]:
        """Get a list of entities"""
        pass
