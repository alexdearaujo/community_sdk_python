# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .EventPolicyLevelSettings import EventPolicyLevelSettings
from .FlowPolicyLevelSettings import FlowPolicyLevelSettings
from .NmsPolicyLevelSettings import NmsPolicyLevelSettings
from .NotificationChannelAssociation import NotificationChannelAssociation
from .v202303Severity import v202303Severity


class PolicyPolicyLevel(BaseModel):
    """
    PolicyPolicyLevel model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    severity: Optional[v202303Severity] = Field(
        validation_alias="severity", default=None
    )

    description: Optional[str] = Field(validation_alias="description", default=None)

    ackRequired: Optional[bool] = Field(validation_alias="ackRequired", default=None)

    nms: Optional[NmsPolicyLevelSettings] = Field(validation_alias="nms", default=None)

    flow: Optional[FlowPolicyLevelSettings] = Field(
        validation_alias="flow", default=None
    )

    event: Optional[EventPolicyLevelSettings] = Field(
        validation_alias="event", default=None
    )

    notifications: Optional[List[Optional[NotificationChannelAssociation]]] = Field(
        validation_alias="notifications", default=None
    )
