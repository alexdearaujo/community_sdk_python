from pydantic import BaseModel, Field

from .SiteMarket import SiteMarket


class CreateSiteMarketRequest(BaseModel):
    """
    CreateSiteMarketRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    siteMarket: SiteMarket = Field(validation_alias="siteMarket")
