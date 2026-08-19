# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .AlertAcknowledgement import AlertAcknowledgement
from .AlertState import AlertState
from .ExternalContext import ExternalContext
from .FlowContext import FlowContext
from .NmsContext import NmsContext
from .Source import Source
from .v202303Severity import v202303Severity


class Alert(BaseModel):
    """
    Alert model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    source: Optional[Source] = Field(validation_alias="source", default=None)

    startTimeAt: Optional[str] = Field(validation_alias="startTimeAt", default=None)

    endTimeAt: Optional[str] = Field(validation_alias="endTimeAt", default=None)

    state: Optional[AlertState] = Field(validation_alias="state", default=None)

    severity: Optional[v202303Severity] = Field(
        validation_alias="severity", default=None
    )

    highestSeverity: Optional[v202303Severity] = Field(
        validation_alias="highestSeverity", default=None
    )

    acknowledgement: Optional[AlertAcknowledgement] = Field(
        validation_alias="acknowledgement", default=None
    )

    eventStartTimeAt: Optional[str] = Field(
        validation_alias="eventStartTimeAt", default=None
    )

    flow: Optional[FlowContext] = Field(validation_alias="flow", default=None)

    nms: Optional[NmsContext] = Field(validation_alias="nms", default=None)

    mitigationId: Optional[str] = Field(validation_alias="mitigationId", default=None)

    externalContexts: Optional[List[Optional[ExternalContext]]] = Field(
        validation_alias="externalContexts", default=None
    )
