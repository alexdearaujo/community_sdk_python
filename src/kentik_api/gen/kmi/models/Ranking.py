from typing import Optional

from pydantic import BaseModel, Field


class Ranking(BaseModel):
    """
    Ranking model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asn: Optional[int] = Field(validation_alias="asn", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    rank: Optional[int] = Field(validation_alias="rank", default=None)

    rankChange: Optional[int] = Field(validation_alias="rankChange", default=None)

    score: Optional[int] = Field(validation_alias="score", default=None)

    scoreChange: Optional[int] = Field(validation_alias="scoreChange", default=None)
