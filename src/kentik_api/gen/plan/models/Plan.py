from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .DeviceSubtype import DeviceSubtype
from .PlanDevice import PlanDevice


class Plan(BaseModel):
    """
    Plan model
        Represents a plan object.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)

    name: str = Field(validation_alias="name")

    description: Optional[str] = Field(validation_alias="description", default=None)

    active: Optional[bool] = Field(validation_alias="active", default=None)

    maxDevices: Optional[int] = Field(validation_alias="maxDevices", default=None)

    maxFps: Optional[int] = Field(validation_alias="maxFps", default=None)

    bgpEnabled: Optional[bool] = Field(validation_alias="bgpEnabled", default=None)

    fastRetention: Optional[int] = Field(validation_alias="fastRetention", default=None)

    fullRetention: Optional[int] = Field(validation_alias="fullRetention", default=None)

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)

    maxBigdataFps: Optional[int] = Field(validation_alias="maxBigdataFps", default=None)

    deviceTypes: Optional[List[Optional[DeviceSubtype]]] = Field(
        validation_alias="deviceTypes", default=None
    )

    devices: Optional[List[Optional[PlanDevice]]] = Field(
        validation_alias="devices", default=None
    )

    metadata: Optional[Dict[str, Any]] = Field(
        validation_alias="metadata", default=None
    )
