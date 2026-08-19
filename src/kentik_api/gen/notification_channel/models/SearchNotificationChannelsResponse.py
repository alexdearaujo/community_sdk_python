# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .NotificationChannel import NotificationChannel


class SearchNotificationChannelsResponse(BaseModel):
    """
    SearchNotificationChannelsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    notificationChannels: Optional[List[Optional[NotificationChannel]]] = Field(
        validation_alias="notificationChannels", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
