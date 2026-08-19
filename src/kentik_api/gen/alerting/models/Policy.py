# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .EventPolicySettings import EventPolicySettings
from .FlowPolicySettings import FlowPolicySettings
from .NmsPolicySettings import NmsPolicySettings
from .PolicyPolicyErrorInfo import PolicyPolicyErrorInfo
from .PolicyPolicyLevel import PolicyPolicyLevel
from .Source import Source


class Policy(BaseModel):
    """
    Policy model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    source: Optional[Source] = Field(validation_alias="source", default=None)

    createdAt: Optional[str] = Field(validation_alias="createdAt", default=None)

    modifiedAt: Optional[str] = Field(validation_alias="modifiedAt", default=None)

    createdBy: Optional[str] = Field(validation_alias="createdBy", default=None)

    modifiedBy: Optional[str] = Field(validation_alias="modifiedBy", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    enabled: Optional[bool] = Field(validation_alias="enabled", default=None)

    levels: Optional[List[Optional[PolicyPolicyLevel]]] = Field(
        validation_alias="levels", default=None
    )

    flow: Optional[FlowPolicySettings] = Field(validation_alias="flow", default=None)

    nms: Optional[NmsPolicySettings] = Field(validation_alias="nms", default=None)

    event: Optional[EventPolicySettings] = Field(validation_alias="event", default=None)

    hasErrors: Optional[bool] = Field(validation_alias="hasErrors", default=None)

    lastError: Optional[PolicyPolicyErrorInfo] = Field(
        validation_alias="lastError", default=None
    )

    expireDate: Optional[str] = Field(validation_alias="expireDate", default=None)
