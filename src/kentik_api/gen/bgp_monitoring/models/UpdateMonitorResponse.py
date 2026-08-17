from typing import Optional

from pydantic import BaseModel, Field

from .BgpMonitor import BgpMonitor


class UpdateMonitorResponse(BaseModel):
    """
    UpdateMonitorResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    monitor: Optional[BgpMonitor] = Field(validation_alias="monitor", default=None)
