from typing import List, Optional

from pydantic import BaseModel, Field

from .Source import Source
from .v202303KeyValue import v202303KeyValue
from .v202303TimeRange import v202303TimeRange


class AlertSilenceNotificationFilters(BaseModel):
    """
    AlertSilenceNotificationFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    silenceIds: Optional[List[str]] = Field(validation_alias="silenceIds", default=None)

    sources: Optional[List[Optional[Source]]] = Field(
        validation_alias="sources", default=None
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

    keys: Optional[List[Optional[v202303KeyValue]]] = Field(
        validation_alias="keys", default=None
    )
