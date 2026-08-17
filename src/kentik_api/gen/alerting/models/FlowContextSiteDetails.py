from typing import Optional

from pydantic import BaseModel, Field


class FlowContextSiteDetails(BaseModel):
    """
    FlowContextSiteDetails model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    latitude: Optional[str] = Field(validation_alias="latitude", default=None)

    longitude: Optional[str] = Field(validation_alias="longitude", default=None)

    location: Optional[str] = Field(validation_alias="location", default=None)

    country: Optional[str] = Field(validation_alias="country", default=None)
