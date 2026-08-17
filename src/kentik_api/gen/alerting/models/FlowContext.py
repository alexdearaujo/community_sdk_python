from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .FlowContextActivationStatus import FlowContextActivationStatus
from .FlowContextMetricValue import FlowContextMetricValue


class FlowContext(BaseModel):
    """
    FlowContext model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    metricValues: Optional[List[Optional[FlowContextMetricValue]]] = Field(
        validation_alias="metricValues", default=None
    )

    activationStatus: Optional[FlowContextActivationStatus] = Field(
        validation_alias="activationStatus", default=None
    )

    baselineValue: Optional[float] = Field(
        validation_alias="baselineValue", default=None
    )

    alertKeyDetails: Optional[Dict[str, Any]] = Field(
        validation_alias="alertKeyDetails", default=None
    )
