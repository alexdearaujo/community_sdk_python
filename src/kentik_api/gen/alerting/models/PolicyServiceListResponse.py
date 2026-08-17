from typing import List, Optional

from pydantic import BaseModel, Field

from .Policy import Policy
from .typesv202506PaginationInfo import typesv202506PaginationInfo


class PolicyServiceListResponse(BaseModel):
    """
    PolicyServiceListResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    pagination: Optional[typesv202506PaginationInfo] = Field(
        validation_alias="pagination", default=None
    )

    policies: Optional[List[Optional[Policy]]] = Field(
        validation_alias="policies", default=None
    )
