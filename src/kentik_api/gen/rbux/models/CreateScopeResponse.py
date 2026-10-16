# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .Scope import Scope


class CreateScopeResponse(BaseModel):
    """
    CreateScopeResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    scope: Optional[Scope] = Field(validation_alias="scope", default=None)
