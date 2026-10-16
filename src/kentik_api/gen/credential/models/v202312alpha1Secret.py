# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .v202312alpha1SecretType import v202312alpha1SecretType


class v202312alpha1Secret(BaseModel):
    """
    Secret
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: str = Field(validation_alias="name", description="The secret's name")

    value: str = Field(
        validation_alias="value", description="The secret's actual value"
    )

    version: int = Field(validation_alias="version", description="The secret's version")

    description: Optional[str] = Field(
        validation_alias="description",
        default=None,
        description="Purpose of this secret",
    )

    type: Optional[v202312alpha1SecretType] = Field(
        validation_alias="type", default=None
    )

    id: str = Field(validation_alias="id", description="The secret's identifier")
