from typing import Any, Dict

from pydantic import BaseModel, Field


class DeviceServiceUpdateDeviceBody(BaseModel):
    """
    UpdateDeviceRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    device: Dict[str, Any] = Field(validation_alias="device")
