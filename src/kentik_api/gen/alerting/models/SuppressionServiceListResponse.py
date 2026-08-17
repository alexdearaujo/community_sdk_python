from typing import List, Optional

from pydantic import BaseModel, Field

from .Suppression import Suppression
from .typesv202506PaginationInfo import typesv202506PaginationInfo


class SuppressionServiceListResponse(BaseModel):
    """
    SuppressionServiceListResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    pagination: Optional[typesv202506PaginationInfo] = Field(
        validation_alias="pagination", default=None
    )

    suppressions: Optional[List[Optional[Suppression]]] = Field(
        validation_alias="suppressions", default=None
    )
