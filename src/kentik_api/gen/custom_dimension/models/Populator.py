from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Populator(BaseModel):
    """
    Populator model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    value: Optional[str] = Field(validation_alias="value", default=None)

    direction: Optional[str] = Field(validation_alias="direction", default=None)

    deviceName: Optional[List[str]] = Field(validation_alias="deviceName", default=None)

    deviceType: Optional[List[str]] = Field(validation_alias="deviceType", default=None)

    site: Optional[List[str]] = Field(validation_alias="site", default=None)

    interfaceName: Optional[List[str]] = Field(
        validation_alias="interfaceName", default=None
    )

    addr: Optional[List[str]] = Field(validation_alias="addr", default=None)

    port: Optional[List[int]] = Field(validation_alias="port", default=None)

    tcpFlags: Optional[int] = Field(validation_alias="tcpFlags", default=None)

    protocol: Optional[List[int]] = Field(validation_alias="protocol", default=None)

    asn: Optional[List[int]] = Field(validation_alias="asn", default=None)

    lasthopAsName: Optional[List[str]] = Field(
        validation_alias="lasthopAsName", default=None
    )

    nexthopAsn: Optional[List[int]] = Field(validation_alias="nexthopAsn", default=None)

    nexthopAsName: Optional[List[str]] = Field(
        validation_alias="nexthopAsName", default=None
    )

    nexthop: Optional[List[str]] = Field(validation_alias="nexthop", default=None)

    bgpAspath: Optional[List[str]] = Field(validation_alias="bgpAspath", default=None)

    bgpCommunity: Optional[List[str]] = Field(
        validation_alias="bgpCommunity", default=None
    )

    mac: Optional[List[str]] = Field(validation_alias="mac", default=None)

    country: Optional[List[str]] = Field(validation_alias="country", default=None)

    vlans: Optional[List[str]] = Field(validation_alias="vlans", default=None)

    user: Optional[str] = Field(validation_alias="user", default=None)

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)

    addrCount: Optional[int] = Field(validation_alias="addrCount", default=None)

    macCount: Optional[int] = Field(validation_alias="macCount", default=None)

    extendedFields: Optional[Dict[str, Any]] = Field(
        validation_alias="extendedFields", default=None
    )
