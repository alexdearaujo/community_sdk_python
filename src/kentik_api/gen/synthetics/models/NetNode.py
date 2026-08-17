from typing import Optional

from pydantic import BaseModel, Field

from .syntheticsv202309Location import syntheticsv202309Location


class NetNode(BaseModel):
    """
    NetNode model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    ip: Optional[str] = Field(validation_alias="ip", default=None)

    asn: Optional[int] = Field(validation_alias="asn", default=None)

    asName: Optional[str] = Field(validation_alias="asName", default=None)

    location: Optional[syntheticsv202309Location] = Field(
        validation_alias="location", default=None
    )

    dnsName: Optional[str] = Field(validation_alias="dnsName", default=None)

    deviceId: Optional[str] = Field(validation_alias="deviceId", default=None)

    siteId: Optional[str] = Field(validation_alias="siteId", default=None)
