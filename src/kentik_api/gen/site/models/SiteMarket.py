from typing import Optional

from pydantic import BaseModel, Field


class SiteMarket(BaseModel):
    """
    SiteMarket model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: str = Field(validation_alias="name")

    description: Optional[str] = Field(validation_alias="description", default=None)

    numberOfSites: Optional[int] = Field(validation_alias="numberOfSites", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)
