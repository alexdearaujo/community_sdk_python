# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class CreateTagKeyRequest(BaseModel):
    """
    CreateTagKeyRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: str = Field(validation_alias="name")

    displayName: Optional[str] = Field(validation_alias="displayName", default=None)

    color: Optional[str] = Field(validation_alias="color", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)
