from typing import List

from pydantic import BaseModel, Field

from .EventPolicySettingsEventType import EventPolicySettingsEventType
from .PolicyFilters import PolicyFilters


class EventPolicySettings(BaseModel):
    """
    EventPolicySettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    type: EventPolicySettingsEventType = Field(validation_alias="type")

    dimensions: List[str] = Field(validation_alias="dimensions")

    filters: PolicyFilters = Field(validation_alias="filters")
