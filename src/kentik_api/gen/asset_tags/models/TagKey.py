from typing import Optional

from pydantic import BaseModel, Field


class TagKey(BaseModel):
    """
    TagKey model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    displayName: Optional[str] = Field(validation_alias="displayName", default=None)

    color: Optional[str] = Field(validation_alias="color", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)
