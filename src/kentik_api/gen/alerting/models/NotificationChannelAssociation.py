# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field


class NotificationChannelAssociation(BaseModel):
    """
    NotificationChannelAssociation model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    channelId: str = Field(validation_alias="channelId")
