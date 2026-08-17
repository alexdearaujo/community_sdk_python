from typing import Optional

from pydantic import BaseModel, Field

from .MitigationEvent import MitigationEvent
from .MitigationState import MitigationState


class MitigationStateEntry(BaseModel):
    """
    MitigationStateEntry model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    timestamp: Optional[str] = Field(validation_alias="timestamp", default=None)

    state: Optional[MitigationState] = Field(validation_alias="state", default=None)

    event: Optional[MitigationEvent] = Field(validation_alias="event", default=None)
