from typing import List, Optional

from pydantic import BaseModel, Field

from .UpdateResult import UpdateResult


class RouteServiceAnnounceResponse(BaseModel):
    """
    RouteServiceAnnounceResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    results: Optional[List[Optional[UpdateResult]]] = Field(
        validation_alias="results", default=None
    )
