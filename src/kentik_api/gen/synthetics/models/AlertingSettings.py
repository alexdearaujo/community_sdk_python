# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .AlertingType import AlertingType
from .GroupedAlertSettings import GroupedAlertSettings


class AlertingSettings(BaseModel):
    """
    AlertingSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    disableWarningNotifications: Optional[bool] = Field(
        validation_alias="disableWarningNotifications", default=None
    )

    alertingType: Optional[AlertingType] = Field(
        validation_alias="alertingType", default=None
    )

    groupedAlertSettings: Optional[GroupedAlertSettings] = Field(
        validation_alias="groupedAlertSettings", default=None
    )
