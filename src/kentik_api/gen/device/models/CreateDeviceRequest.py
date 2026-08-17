from pydantic import BaseModel, Field

from .DeviceConcise import DeviceConcise


class CreateDeviceRequest(BaseModel):
    """
    CreateDeviceRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    device: DeviceConcise = Field(validation_alias="device")
