from typing import Optional

from pydantic import BaseModel, Field

from .SiteMarket import SiteMarket


class UpdateSiteMarketResponse(BaseModel):
    """
    UpdateSiteMarketResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    siteMarket: Optional[SiteMarket] = Field(
        validation_alias="siteMarket", default=None
    )
