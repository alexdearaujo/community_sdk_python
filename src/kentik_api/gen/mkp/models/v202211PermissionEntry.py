# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field


class v202211PermissionEntry(BaseModel):
    """
    PermissionEntry model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    capability: str = Field(validation_alias="capability")

    allowed: bool = Field(validation_alias="allowed")
