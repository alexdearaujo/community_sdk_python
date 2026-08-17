from typing import List, Optional

from pydantic import BaseModel, Field

from .BgpMonitorSettings import BgpMonitorSettings
from .BgpMonitorStatus import BgpMonitorStatus
from .v202303UserInfo import v202303UserInfo


class BgpMonitor(BaseModel):
    """
    BgpMonitor model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: str = Field(validation_alias="name")

    status: Optional[BgpMonitorStatus] = Field(validation_alias="status", default=None)

    settings: Optional[BgpMonitorSettings] = Field(
        validation_alias="settings", default=None
    )

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    createdBy: Optional[v202303UserInfo] = Field(
        validation_alias="createdBy", default=None
    )

    lastUpdatedBy: Optional[v202303UserInfo] = Field(
        validation_alias="lastUpdatedBy", default=None
    )

    labels: Optional[List[str]] = Field(validation_alias="labels", default=None)
