from typing import Any, Dict

from pydantic import BaseModel, Field


class SiteServiceUpdateSiteMarketBody(BaseModel):
    """
    UpdateSiteMarketRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    siteMarket: Dict[str, Any] = Field(validation_alias="siteMarket")
