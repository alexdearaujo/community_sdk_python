from typing import Optional

from pydantic import BaseModel, Field


class CapacityPlanInterfaceDetail(BaseModel):
    """
    InterfaceDetail model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    deviceName: Optional[str] = Field(validation_alias="deviceName", default=None)

    intfName: Optional[str] = Field(validation_alias="intfName", default=None)

    intfDescription: Optional[str] = Field(
        validation_alias="intfDescription", default=None
    )

    intfCapacity: Optional[str] = Field(validation_alias="intfCapacity", default=None)

    networkBoundary: Optional[str] = Field(
        validation_alias="networkBoundary", default=None
    )

    connType: Optional[str] = Field(validation_alias="connType", default=None)

    provider: Optional[str] = Field(validation_alias="provider", default=None)

    utilStatus: Optional[str] = Field(validation_alias="utilStatus", default=None)

    utilOutMbps: Optional[str] = Field(validation_alias="utilOutMbps", default=None)

    utilOutPct: Optional[str] = Field(validation_alias="utilOutPct", default=None)

    utilInMbps: Optional[str] = Field(validation_alias="utilInMbps", default=None)

    utilInPct: Optional[str] = Field(validation_alias="utilInPct", default=None)

    runoutStatus: Optional[str] = Field(validation_alias="runoutStatus", default=None)

    runoutInDate: Optional[str] = Field(validation_alias="runoutInDate", default=None)

    runoutInVariation: Optional[str] = Field(
        validation_alias="runoutInVariation", default=None
    )

    runoutOutDate: Optional[str] = Field(validation_alias="runoutOutDate", default=None)

    runoutOutVariation: Optional[str] = Field(
        validation_alias="runoutOutVariation", default=None
    )
