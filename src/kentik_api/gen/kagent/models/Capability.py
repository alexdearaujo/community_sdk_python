# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class Capability(BaseModel):
    """
    Capability model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: Optional[str] = Field(validation_alias="name", default=None)

    displayName: Optional[str] = Field(validation_alias="displayName", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    seedBundleId: Optional[str] = Field(validation_alias="seedBundleId", default=None)

    seedConfig: Optional[str] = Field(validation_alias="seedConfig", default=None)
