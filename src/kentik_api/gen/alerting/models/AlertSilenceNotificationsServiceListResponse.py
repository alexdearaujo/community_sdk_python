# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .AlertSilenceNotificationsDefinition import AlertSilenceNotificationsDefinition
from .typesv202506PaginationInfo import typesv202506PaginationInfo


class AlertSilenceNotificationsServiceListResponse(BaseModel):
    """
    AlertSilenceNotificationsServiceListResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    pagination: Optional[typesv202506PaginationInfo] = Field(
        validation_alias="pagination", default=None
    )

    silences: Optional[List[Optional[AlertSilenceNotificationsDefinition]]] = Field(
        validation_alias="silences", default=None
    )
