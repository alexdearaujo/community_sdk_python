from typing import Optional

from pydantic import BaseModel, Field


class v202303VantagePoint(BaseModel):
    """
    VantagePoint model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    dataset: Optional[str] = Field(validation_alias="dataset", default=None)

    collector: Optional[str] = Field(validation_alias="collector", default=None)

    peerAsn: Optional[int] = Field(validation_alias="peerAsn", default=None)

    peerIp: Optional[str] = Field(validation_alias="peerIp", default=None)
