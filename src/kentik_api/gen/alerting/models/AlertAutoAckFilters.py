# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .Source import Source
from .v202303KeyValue import v202303KeyValue
from .v202303TimeRange import v202303TimeRange


class AlertAutoAckFilters(BaseModel):
    """
    AlertAutoAckFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    autoAckIds: Optional[List[str]] = Field(validation_alias="autoAckIds", default=None)

    sources: Optional[List[Optional[Source]]] = Field(
        validation_alias="sources", default=None
    )

    keys: Optional[List[Optional[v202303KeyValue]]] = Field(
        validation_alias="keys", default=None
    )

    userIds: Optional[List[str]] = Field(validation_alias="userIds", default=None)

    createdAt: Optional[v202303TimeRange] = Field(
        validation_alias="createdAt", default=None
    )

    modifiedAt: Optional[v202303TimeRange] = Field(
        validation_alias="modifiedAt", default=None
    )

    startTimeAt: Optional[v202303TimeRange] = Field(
        validation_alias="startTimeAt", default=None
    )

    endTimeAt: Optional[v202303TimeRange] = Field(
        validation_alias="endTimeAt", default=None
    )
