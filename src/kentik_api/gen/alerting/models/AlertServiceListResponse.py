from typing import List, Optional

from pydantic import BaseModel, Field

from .Alert import Alert
from .typesv202506PaginationInfo import typesv202506PaginationInfo


class AlertServiceListResponse(BaseModel):
    """
    AlertServiceListResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    pagination: Optional[typesv202506PaginationInfo] = Field(
        validation_alias="pagination", default=None
    )

    alerts: Optional[List[Optional[Alert]]] = Field(
        validation_alias="alerts", default=None
    )
