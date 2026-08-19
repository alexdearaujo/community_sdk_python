# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .FlowspecAction import FlowspecAction
from .FlowspecActionAccept import FlowspecActionAccept
from .FlowspecActionDiscard import FlowspecActionDiscard
from .FlowspecActionExtendedCommunity import FlowspecActionExtendedCommunity
from .FlowspecActionIPNextHopCopy import FlowspecActionIPNextHopCopy
from .FlowspecActionIPNextHopRedirect import FlowspecActionIPNextHopRedirect
from .FlowspecActionLargeCommunity import FlowspecActionLargeCommunity
from .FlowspecActionMarkDSCP import FlowspecActionMarkDSCP
from .FlowspecActionRegularCommunity import FlowspecActionRegularCommunity
from .FlowspecActionRouteTargetRedirect import FlowspecActionRouteTargetRedirect
from .FlowspecActionTerminalSample import FlowspecActionTerminalSample
from .FlowspecActionTrafficRateBytes import FlowspecActionTrafficRateBytes
from .FlowspecMatch import FlowspecMatch
from .InetType import InetType


class FlowspecUpdate(BaseModel):
    """
    FlowspecUpdate model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    match: Optional[FlowspecMatch] = Field(validation_alias="match", default=None)

    creationTime: Optional[str] = Field(validation_alias="creationTime", default=None)

    inet: Optional[str] = Field(validation_alias="inet", default=None)

    inetType: Optional[InetType] = Field(validation_alias="inetType", default=None)

    key: Optional[str] = Field(validation_alias="key", default=None)

    rateBytes: Optional[FlowspecActionTrafficRateBytes] = Field(
        validation_alias="rateBytes", default=None
    )

    discard: Optional[FlowspecActionDiscard] = Field(
        validation_alias="discard", default=None
    )

    markDscp: Optional[FlowspecActionMarkDSCP] = Field(
        validation_alias="markDscp", default=None
    )

    rtRedirect: Optional[FlowspecActionRouteTargetRedirect] = Field(
        validation_alias="rtRedirect", default=None
    )

    ipRedirect: Optional[FlowspecActionIPNextHopRedirect] = Field(
        validation_alias="ipRedirect", default=None
    )

    accept: Optional[FlowspecActionAccept] = Field(
        validation_alias="accept", default=None
    )

    actionType: Optional[FlowspecActionTerminalSample] = Field(
        validation_alias="actionType", default=None
    )

    rtCopy: Optional[FlowspecActionIPNextHopCopy] = Field(
        validation_alias="rtCopy", default=None
    )

    regularCommunity: Optional[FlowspecActionRegularCommunity] = Field(
        validation_alias="regularCommunity", default=None
    )

    extendedCommunity: Optional[FlowspecActionExtendedCommunity] = Field(
        validation_alias="extendedCommunity", default=None
    )

    largeCommunity: Optional[FlowspecActionLargeCommunity] = Field(
        validation_alias="largeCommunity", default=None
    )

    actions: Optional[List[Optional[FlowspecAction]]] = Field(
        validation_alias="actions", default=None
    )

    terminal: Optional[bool] = Field(validation_alias="terminal", default=None)

    sample: Optional[bool] = Field(validation_alias="sample", default=None)
