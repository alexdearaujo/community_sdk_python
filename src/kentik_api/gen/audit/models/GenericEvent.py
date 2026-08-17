from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class GenericEvent(BaseModel):
    """
    GenericEvent model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    eventSource: Optional[str] = Field(validation_alias="eventSource", default=None)

    action: Optional[str] = Field(validation_alias="action", default=None)

    eventType: Optional[str] = Field(validation_alias="eventType", default=None)

    owner: Optional[str] = Field(validation_alias="owner", default=None)

    metadata: Optional[Dict[str, Any]] = Field(
        validation_alias="metadata", default=None
    )
