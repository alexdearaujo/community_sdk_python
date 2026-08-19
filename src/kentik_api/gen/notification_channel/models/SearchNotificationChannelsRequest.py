# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .ChannelType import ChannelType


class SearchNotificationChannelsRequest(BaseModel):
    """
    SearchNotificationChannelsRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    namePattern: Optional[str] = Field(validation_alias="namePattern", default=None)

    types: Optional[List[Optional[ChannelType]]] = Field(
        validation_alias="types", default=None
    )

    includeDisabled: Optional[bool] = Field(
        validation_alias="includeDisabled", default=None
    )
