from typing import Optional

from pydantic import BaseModel, Field

from .DeviceSubtype import DeviceSubtype


class PlanDevice(BaseModel):
    """
    PlanDevice model
        Represents a device that is associated with a plan.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    deviceName: str = Field(validation_alias="deviceName")

    deviceSubtype: DeviceSubtype = Field(validation_alias="deviceSubtype")

    deviceType: DeviceSubtype = Field(validation_alias="deviceType")
