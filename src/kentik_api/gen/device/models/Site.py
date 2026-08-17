from typing import Optional

from pydantic import BaseModel, Field


class Site(BaseModel):
    """
    Site model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    siteName: Optional[str] = Field(validation_alias="siteName", default=None)

    lat: Optional[float] = Field(validation_alias="lat", default=None)

    lon: Optional[float] = Field(validation_alias="lon", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)
