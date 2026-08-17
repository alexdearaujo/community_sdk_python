from pydantic import BaseModel, Field

from .BgpMonitor import BgpMonitor


class CreateMonitorRequest(BaseModel):
    """
    CreateMonitorRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    monitor: BgpMonitor = Field(validation_alias="monitor")
