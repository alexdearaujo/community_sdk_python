from typing import List

from pydantic import BaseModel, Field

from .DeviceConcise import DeviceConcise


class UpdateDevicesRequest(BaseModel):
    """
    UpdateDevicesRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    devices: List[DeviceConcise] = Field(validation_alias="devices")
