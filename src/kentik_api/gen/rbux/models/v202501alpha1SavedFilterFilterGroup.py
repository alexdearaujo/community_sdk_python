# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501alpha1SavedFilterFilter import v202501alpha1SavedFilterFilter
from .v202501alpha1SavedFilterFilterId import v202501alpha1SavedFilterFilterId


class v202501alpha1SavedFilterFilterGroup(BaseModel):
    """
    v202501alpha1SavedFilterFilterGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    any: Optional[bool] = Field(
        validation_alias="any",
        default=None,
        description="Whether to require matches against ALL or ANY filter. Defaults to requiring a match for all.",
    )

    filters: Optional[List[Optional[v202501alpha1SavedFilterFilter]]] = Field(
        validation_alias="filters",
        default=None,
        description="Filters to operate against.",
    )

    not_: Optional[bool] = Field(
        validation_alias="not",
        serialization_alias="not",
        default=None,
        description="Whether or not to NOT() the filter group. Defaults to false.",
    )

    savedFilterIds: Optional[List[Optional[v202501alpha1SavedFilterFilterId]]] = Field(
        validation_alias="savedFilterIds",
        default=None,
        description="Include reference of other saved filters in this filter group.",
    )

    nestedFilterGroups: Optional[
        List[Optional["v202501alpha1SavedFilterFilterGroup"]]
    ] = Field(
        validation_alias="nestedFilterGroups",
        default=None,
        description="Include nested filter group.",
    )
