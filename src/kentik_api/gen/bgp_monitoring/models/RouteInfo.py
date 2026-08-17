from typing import List, Optional

from pydantic import BaseModel, Field

from .Nlri import Nlri
from .v202303RpkiStatus import v202303RpkiStatus
from .v202303VantagePoint import v202303VantagePoint


class RouteInfo(BaseModel):
    """
    RouteInfo model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    nlri: Optional[Nlri] = Field(validation_alias="nlri", default=None)

    originAsn: Optional[int] = Field(validation_alias="originAsn", default=None)

    asPath: Optional[List[str]] = Field(validation_alias="asPath", default=None)

    vantagePoint: Optional[v202303VantagePoint] = Field(
        validation_alias="vantagePoint", default=None
    )

    rpkiStatus: Optional[v202303RpkiStatus] = Field(
        validation_alias="rpkiStatus", default=None
    )

    nexthop: Optional[str] = Field(validation_alias="nexthop", default=None)
