from typing import List, Optional

from pydantic import BaseModel, Field

from .BgpHealthSettings import BgpHealthSettings
from .Nlri import Nlri


class BgpMonitorSettings(BaseModel):
    """
    BgpMonitorSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    allowedAsns: Optional[List[int]] = Field(
        validation_alias="allowedAsns", default=None
    )

    targets: List[Nlri] = Field(validation_alias="targets")

    checkRpki: Optional[bool] = Field(validation_alias="checkRpki", default=None)

    includeCoveredPrefixes: Optional[bool] = Field(
        validation_alias="includeCoveredPrefixes", default=None
    )

    healthSettings: Optional[BgpHealthSettings] = Field(
        validation_alias="healthSettings", default=None
    )

    notificationChannels: Optional[List[str]] = Field(
        validation_alias="notificationChannels", default=None
    )

    notes: Optional[str] = Field(validation_alias="notes", default=None)

    allowedUpstreams: Optional[List[int]] = Field(
        validation_alias="allowedUpstreams", default=None
    )
