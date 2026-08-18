from typing import Optional

from pydantic import BaseModel, Field


class FlowspecActionIPNextHopCopy(BaseModel):
    """
    FlowspecActionIPNextHopCopy model
    FlowspecActionIPNextHopCopy allows the traffic to be copied
    to a specific Next Hop IP address.

    Extended Community type and sub-type: 0x0800 with least-significant bit &#39;C&#39; set to 1

    The target next-hop address refers to the &#39;Network Address of Next-Hop&#39; field
    of the associated NLRI.
    https://datatracker.ietf.org/doc/html/draft-simpson-idr-flowspec-redirect
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    nextHop: Optional[str] = Field(validation_alias="nextHop", default=None)
