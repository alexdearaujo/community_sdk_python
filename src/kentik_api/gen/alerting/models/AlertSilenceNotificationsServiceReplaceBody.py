from typing import Any, Dict

from pydantic import BaseModel, Field


class AlertSilenceNotificationsServiceReplaceBody(BaseModel):
    """
    AlertSilenceNotificationsServiceReplaceBody model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    silence: Dict[str, Any] = Field(validation_alias="silence")
