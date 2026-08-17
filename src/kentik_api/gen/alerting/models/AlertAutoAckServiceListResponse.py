from typing import List, Optional

from pydantic import BaseModel, Field

from .AlertAutoAck import AlertAutoAck
from .typesv202506PaginationInfo import typesv202506PaginationInfo


class AlertAutoAckServiceListResponse(BaseModel):
    """
    AlertAutoAckServiceListResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    pagination: Optional[typesv202506PaginationInfo] = Field(
        validation_alias="pagination", default=None
    )

    autoAcks: Optional[List[Optional[AlertAutoAck]]] = Field(
        validation_alias="autoAcks", default=None
    )
