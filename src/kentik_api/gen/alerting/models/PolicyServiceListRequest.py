# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .PolicyListFilters import PolicyListFilters
from .typesv202506PaginationConfig import typesv202506PaginationConfig
from .typesv202506SortingConfig import typesv202506SortingConfig


class PolicyServiceListRequest(BaseModel):
    """
    PolicyServiceListRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    pagination: Optional[typesv202506PaginationConfig] = Field(
        validation_alias="pagination", default=None
    )

    sorting: Optional[typesv202506SortingConfig] = Field(
        validation_alias="sorting", default=None
    )

    filters: Optional[PolicyListFilters] = Field(
        validation_alias="filters", default=None
    )
