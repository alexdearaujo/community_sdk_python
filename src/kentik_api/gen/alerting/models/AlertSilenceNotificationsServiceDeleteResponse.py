from pydantic import BaseModel


class AlertSilenceNotificationsServiceDeleteResponse(BaseModel):
    """
    AlertSilenceNotificationsServiceDeleteResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
