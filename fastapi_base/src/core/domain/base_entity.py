from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional
from uuid import UUID


class BaseEntity(BaseModel):
    """
    Base entity model.
    """
    id: UUID = Field(description="Unique identifier", min_length=36, max_length=36)
    created_at: datetime = Field(description="Creation date")
    updated_at: Optional[datetime] = Field(default=None, description="Update date")


model_config_base = ConfigDict(
    from_attributes=True,
    extra="ignore",
    str_strip_whitespace=True,
)
