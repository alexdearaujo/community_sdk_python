from typing import Optional

from pydantic import BaseModel, Field


class PacketLossData(BaseModel):
    """
    PacketLossData model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    current: Optional[float] = Field(validation_alias="current", default=None)

    health: Optional[str] = Field(validation_alias="health", default=None)
