from typing import List, Optional

from pydantic import BaseModel, Field

from .SiteMarket import SiteMarket


class ListSiteMarketsResponse(BaseModel):
    """
    ListSiteMarketsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    siteMarkets: Optional[List[Optional[SiteMarket]]] = Field(
        validation_alias="siteMarkets", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
