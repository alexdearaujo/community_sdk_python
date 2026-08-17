from typing import Optional

from pydantic import BaseModel, Field


class KmiServiceGetRankingsBody(BaseModel):
    """
    GetRankingsRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    limit: Optional[int] = Field(validation_alias="limit", default=None)
