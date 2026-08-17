from typing import Optional

from pydantic import BaseModel, Field


class syntheticsv202309Location(BaseModel):
    """
    Location model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    latitude: Optional[float] = Field(validation_alias="latitude", default=None)

    longitude: Optional[float] = Field(validation_alias="longitude", default=None)

    country: Optional[str] = Field(validation_alias="country", default=None)

    region: Optional[str] = Field(validation_alias="region", default=None)

    city: Optional[str] = Field(validation_alias="city", default=None)
