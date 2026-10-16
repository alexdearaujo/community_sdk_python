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

    any: Optional[bool] = Field(validation_alias="any", default=None)

    filters: Optional[List[Optional[v202501alpha1SavedFilterFilter]]] = Field(
        validation_alias="filters", default=None
    )

    not_: Optional[bool] = Field(validation_alias="not", default=None)

    savedFilterIds: Optional[List[Optional[v202501alpha1SavedFilterFilterId]]] = Field(
        validation_alias="savedFilterIds", default=None
    )

    nestedFilterGroups: Optional[
        List[Optional["v202501alpha1SavedFilterFilterGroup"]]
    ] = Field(validation_alias="nestedFilterGroups", default=None)
