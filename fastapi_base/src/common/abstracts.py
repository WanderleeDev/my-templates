from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, List
from uuid import UUID

from db.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class AbstractRepository(ABC, Generic[T]):
    """
    Abstract base class for all repositories
    """

    @abstractmethod
    def create(self, entity: T) -> T:
        """Create an entity"""
        pass

    @abstractmethod
    def read(self, entity_id: UUID) -> Optional[T]:
        """Read an entity by its ID"""
        pass

    @abstractmethod
    def update(self, entity: T) -> bool:
        """Update an entity"""
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        """Delete an entity by its ID"""
        pass

    @abstractmethod
    def read_list(self, skip: int = 0, limit: int = 10) -> List[T]:
        """Get a list of entities"""
        pass
