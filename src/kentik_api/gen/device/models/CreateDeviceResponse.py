from typing import Optional

from pydantic import BaseModel, Field

from .DeviceDetailed import DeviceDetailed


class CreateDeviceResponse(BaseModel):
    """
    CreateDeviceResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    device: Optional[DeviceDetailed] = Field(validation_alias="device", default=None)
