from typing import Optional

from pydantic import BaseModel, Field

from .SecretType import SecretType


class Secret(BaseModel):
    """
    Secret model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: str = Field(validation_alias="name")

    value: str = Field(validation_alias="value")

    version: int = Field(validation_alias="version")

    description: Optional[str] = Field(validation_alias="description", default=None)

    type: Optional[SecretType] = Field(validation_alias="type", default=None)

    id: str = Field(validation_alias="id")
