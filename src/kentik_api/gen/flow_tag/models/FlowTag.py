from typing import List, Optional

from pydantic import BaseModel, Field

from .AddressInfo import AddressInfo


class FlowTag(BaseModel):
    """
    FlowTag model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    editedBy: Optional[str] = Field(validation_alias="editedBy", default=None)

    createdBy: Optional[str] = Field(validation_alias="createdBy", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    ip: Optional[AddressInfo] = Field(validation_alias="ip", default=None)

    port: Optional[List[str]] = Field(validation_alias="port", default=None)

    tcpFlags: Optional[int] = Field(validation_alias="tcpFlags", default=None)

    protocol: Optional[List[int]] = Field(validation_alias="protocol", default=None)

    deviceName: Optional[List[str]] = Field(validation_alias="deviceName", default=None)

    deviceType: Optional[List[str]] = Field(validation_alias="deviceType", default=None)

    site: Optional[List[str]] = Field(validation_alias="site", default=None)

    interfaceName: Optional[List[str]] = Field(
        validation_alias="interfaceName", default=None
    )

    asn: Optional[List[str]] = Field(validation_alias="asn", default=None)

    lasthopAsName: Optional[List[str]] = Field(
        validation_alias="lasthopAsName", default=None
    )

    nexthopAsn: Optional[List[str]] = Field(validation_alias="nexthopAsn", default=None)

    nexthopAsName: Optional[List[str]] = Field(
        validation_alias="nexthopAsName", default=None
    )

    nexthop: Optional[List[str]] = Field(validation_alias="nexthop", default=None)

    bgpAspath: Optional[List[str]] = Field(validation_alias="bgpAspath", default=None)

    bgpCommunity: Optional[List[str]] = Field(
        validation_alias="bgpCommunity", default=None
    )

    mac: Optional[AddressInfo] = Field(validation_alias="mac", default=None)

    country: Optional[List[str]] = Field(validation_alias="country", default=None)

    vlans: Optional[List[str]] = Field(validation_alias="vlans", default=None)
