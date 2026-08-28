# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .ScopeDimensions import ScopeDimensions
from .v202501alpha1SavedFilterFilters import v202501alpha1SavedFilterFilters


class ScopeConfig(BaseModel):
    """
    ScopeConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    dimensions: Optional[ScopeDimensions] = Field(
        validation_alias="dimensions", default=None
    )

    filters: Optional[v202501alpha1SavedFilterFilters] = Field(
        validation_alias="filters", default=None
    )
