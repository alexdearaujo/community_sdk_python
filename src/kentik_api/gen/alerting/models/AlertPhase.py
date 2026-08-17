from typing import Optional

from pydantic import BaseModel, Field

from .FlowContext import FlowContext
from .NmsContext import NmsContext
from .v202303Severity import v202303Severity


class AlertPhase(BaseModel):
    """
    AlertPhase model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    severity: Optional[v202303Severity] = Field(
        validation_alias="severity", default=None
    )

    startTimeAt: Optional[str] = Field(validation_alias="startTimeAt", default=None)

    endTimeAt: Optional[str] = Field(validation_alias="endTimeAt", default=None)

    flow: Optional[FlowContext] = Field(validation_alias="flow", default=None)

    nms: Optional[NmsContext] = Field(validation_alias="nms", default=None)
