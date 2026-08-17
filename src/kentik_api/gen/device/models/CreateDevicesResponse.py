from typing import List, Optional

from pydantic import BaseModel, Field

from .DeviceDetailed import DeviceDetailed


class CreateDevicesResponse(BaseModel):
    """
    CreateDevicesResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    devices: Optional[List[Optional[DeviceDetailed]]] = Field(
        validation_alias="devices", default=None
    )

    failedDevices: Optional[List[str]] = Field(
        validation_alias="failedDevices", default=None
    )
