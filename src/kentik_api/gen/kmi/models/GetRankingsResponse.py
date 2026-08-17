from typing import List, Optional

from pydantic import BaseModel, Field

from .Ranking import Ranking


class GetRankingsResponse(BaseModel):
    """
    GetRankingsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    rankings: Optional[List[Optional[Ranking]]] = Field(
        validation_alias="rankings", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
