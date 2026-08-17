from typing import List, Optional

from pydantic import BaseModel, Field

from .DeviceDetailed import DeviceDetailed


class ListDevicesResponse(BaseModel):
    """
    ListDevicesResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    devices: Optional[List[Optional[DeviceDetailed]]] = Field(
        validation_alias="devices", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
