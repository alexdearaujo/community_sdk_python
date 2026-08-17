from pydantic import BaseModel, Field

from .AlertSilenceNotificationsDefinition import AlertSilenceNotificationsDefinition


class AlertSilenceNotificationsServiceCreateRequest(BaseModel):
    """
    AlertSilenceNotificationsServiceCreateRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    silence: AlertSilenceNotificationsDefinition = Field(validation_alias="silence")
