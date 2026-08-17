from typing import Any, Dict

from pydantic import BaseModel, Field


class BgpMonitoringAdminServiceUpdateMonitorBody(BaseModel):
    """
    UpdateMonitorRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    monitor: Dict[str, Any] = Field(validation_alias="monitor")
