# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .Source import Source
from .v202303KeyValue import v202303KeyValue


class AlertSilenceNotificationsDefinition(BaseModel):
    """
    AlertSilenceNotificationsDefinition model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    userId: Optional[str] = Field(validation_alias="userId", default=None)

    source: Optional[Source] = Field(validation_alias="source", default=None)

    key: Optional[v202303KeyValue] = Field(validation_alias="key", default=None)

    startTimeAt: str = Field(validation_alias="startTimeAt")

    endTimeAt: Optional[str] = Field(validation_alias="endTimeAt", default=None)

    createdAt: Optional[str] = Field(validation_alias="createdAt", default=None)

    modifiedAt: Optional[str] = Field(validation_alias="modifiedAt", default=None)
