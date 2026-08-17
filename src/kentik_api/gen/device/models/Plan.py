from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Plan(BaseModel):
    """
    Plan model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    active: Optional[bool] = Field(validation_alias="active", default=None)

    bgp: Optional[bool] = Field(validation_alias="bgp", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    deviceTypes: Optional[List[str]] = Field(
        validation_alias="deviceTypes", default=None
    )

    devices: Optional[List[str]] = Field(validation_alias="devices", default=None)

    fastRetention: Optional[int] = Field(validation_alias="fastRetention", default=None)

    fullRetention: Optional[int] = Field(validation_alias="fullRetention", default=None)

    maxBigdataFps: Optional[int] = Field(validation_alias="maxBigdataFps", default=None)

    maxDevices: Optional[int] = Field(validation_alias="maxDevices", default=None)

    maxFps: Optional[int] = Field(validation_alias="maxFps", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    metadata: Optional[Dict[str, Any]] = Field(
        validation_alias="metadata", default=None
    )
