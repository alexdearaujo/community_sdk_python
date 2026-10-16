# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501alpha1SavedFilterFilterGroup import v202501alpha1SavedFilterFilterGroup


class v202501alpha1SavedFilterFilters(BaseModel):
    """
    v202501alpha1SavedFilterFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    any: Optional[bool] = Field(validation_alias="any", default=None)

    filterGroups: List[v202501alpha1SavedFilterFilterGroup] = Field(
        validation_alias="filterGroups"
    )
