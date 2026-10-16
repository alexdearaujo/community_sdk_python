# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .ScopeConfig import ScopeConfig


class ScopeServiceUpdateScopeBody(BaseModel):
    """
    ScopeServiceUpdateScopeBody model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: str = Field(validation_alias="name")

    description: Optional[str] = Field(validation_alias="description", default=None)

    scope: ScopeConfig = Field(validation_alias="scope")

    createdBy: Optional[str] = Field(validation_alias="createdBy", default=None)

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)
