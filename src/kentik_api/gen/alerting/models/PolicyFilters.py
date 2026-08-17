from typing import List, Optional

from pydantic import BaseModel, Field

from .PolicyFiltersFieldFilter import PolicyFiltersFieldFilter
from .PolicyFiltersFilterConnector import PolicyFiltersFilterConnector
from .PolicyFiltersSavedFilter import PolicyFiltersSavedFilter


class PolicyFilters(BaseModel):
    """
    PolicyFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    not_: Optional[bool] = Field(validation_alias="not", default=None)

    connector: Optional[PolicyFiltersFilterConnector] = Field(
        validation_alias="connector", default=None
    )

    filters: Optional[List[Optional[PolicyFiltersFieldFilter]]] = Field(
        validation_alias="filters", default=None
    )

    groups: Optional[List[Optional["PolicyFilters"]]] = Field(
        validation_alias="groups", default=None
    )

    saved: Optional[List[Optional[PolicyFiltersSavedFilter]]] = Field(
        validation_alias="saved", default=None
    )
