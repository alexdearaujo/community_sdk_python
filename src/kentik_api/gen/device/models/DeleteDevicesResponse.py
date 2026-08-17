from typing import List, Optional

from pydantic import BaseModel, Field


class DeleteDevicesResponse(BaseModel):
    """
    DeleteDevicesResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    failedDevices: Optional[List[str]] = Field(
        validation_alias="failedDevices", default=None
    )
