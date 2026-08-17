from typing import Optional

from pydantic import BaseModel, Field

from .AlertAutoAckFilters import AlertAutoAckFilters
from .typesv202506PaginationConfig import typesv202506PaginationConfig
from .typesv202506SortingConfig import typesv202506SortingConfig


class AlertAutoAckServiceListRequest(BaseModel):
    """
    AlertAutoAckServiceListRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    pagination: Optional[typesv202506PaginationConfig] = Field(
        validation_alias="pagination", default=None
    )

    sorting: Optional[typesv202506SortingConfig] = Field(
        validation_alias="sorting", default=None
    )

    filters: Optional[AlertAutoAckFilters] = Field(
        validation_alias="filters", default=None
    )
