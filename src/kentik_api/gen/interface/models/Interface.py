from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .ConnectivityType import ConnectivityType
from .InterfaceVrf import InterfaceVrf
from .NetworkBoundary import NetworkBoundary


class Interface(BaseModel):
    """
    Interface model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    deviceId: Optional[str] = Field(validation_alias="deviceId", default=None)

    snmpId: Optional[str] = Field(validation_alias="snmpId", default=None)

    snmpSpeed: Optional[int] = Field(validation_alias="snmpSpeed", default=None)

    snmpType: Optional[int] = Field(validation_alias="snmpType", default=None)

    snmpAlias: Optional[str] = Field(validation_alias="snmpAlias", default=None)

    interfaceIp: Optional[str] = Field(validation_alias="interfaceIp", default=None)

    interfaceDescription: Optional[str] = Field(
        validation_alias="interfaceDescription", default=None
    )

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    interfaceIpNetmask: Optional[str] = Field(
        validation_alias="interfaceIpNetmask", default=None
    )

    connectivityType: Optional[ConnectivityType] = Field(
        validation_alias="connectivityType", default=None
    )

    networkBoundary: Optional[NetworkBoundary] = Field(
        validation_alias="networkBoundary", default=None
    )

    topNexthopAsns: Optional[List[int]] = Field(
        validation_alias="topNexthopAsns", default=None
    )

    provider: Optional[str] = Field(validation_alias="provider", default=None)

    interfaceKvs: Optional[Dict[str, Any]] = Field(
        validation_alias="interfaceKvs", default=None
    )

    interfaceTags: Optional[Dict[str, Any]] = Field(
        validation_alias="interfaceTags", default=None
    )

    interfaceStatus: Optional[str] = Field(
        validation_alias="interfaceStatus", default=None
    )

    extraInfo: Optional[Dict[str, Any]] = Field(
        validation_alias="extraInfo", default=None
    )

    initialSnmpId: Optional[str] = Field(validation_alias="initialSnmpId", default=None)

    initialSnmpAlias: Optional[str] = Field(
        validation_alias="initialSnmpAlias", default=None
    )

    initialInterfaceDescription: Optional[str] = Field(
        validation_alias="initialInterfaceDescription", default=None
    )

    initialSnmpSpeed: Optional[int] = Field(
        validation_alias="initialSnmpSpeed", default=None
    )

    secondaryIps: Optional[str] = Field(validation_alias="secondaryIps", default=None)

    initialConnectivityType: Optional[ConnectivityType] = Field(
        validation_alias="initialConnectivityType", default=None
    )

    initialNetworkBoundary: Optional[NetworkBoundary] = Field(
        validation_alias="initialNetworkBoundary", default=None
    )

    initialProvider: Optional[str] = Field(
        validation_alias="initialProvider", default=None
    )

    vrfId: Optional[str] = Field(validation_alias="vrfId", default=None)

    vrf: Optional[InterfaceVrf] = Field(validation_alias="vrf", default=None)
