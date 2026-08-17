from typing import List, Optional

from pydantic import BaseModel, Field

from .CustomColumnData import CustomColumnData
from .DeviceNmsConfig import DeviceNmsConfig
from .DeviceSnmpV3Conf import DeviceSnmpV3Conf
from .devicev202504beta2Label import devicev202504beta2Label
from .GnmiV1Conf import GnmiV1Conf
from .Interface import Interface
from .Plan import Plan
from .Site import Site


class DeviceDetailed(BaseModel):
    """
    DeviceDetailed model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)

    deviceName: Optional[str] = Field(validation_alias="deviceName", default=None)

    deviceAlias: Optional[str] = Field(validation_alias="deviceAlias", default=None)

    deviceType: Optional[str] = Field(validation_alias="deviceType", default=None)

    deviceDescription: Optional[str] = Field(
        validation_alias="deviceDescription", default=None
    )

    site: Optional[Site] = Field(validation_alias="site", default=None)

    plan: Optional[Plan] = Field(validation_alias="plan", default=None)

    labels: Optional[List[Optional[devicev202504beta2Label]]] = Field(
        validation_alias="labels", default=None
    )

    allInterfaces: Optional[List[Optional[Interface]]] = Field(
        validation_alias="allInterfaces", default=None
    )

    deviceFlowType: Optional[str] = Field(
        validation_alias="deviceFlowType", default=None
    )

    deviceSampleRate: Optional[str] = Field(
        validation_alias="deviceSampleRate", default=None
    )

    sendingIps: Optional[List[str]] = Field(validation_alias="sendingIps", default=None)

    deviceSnmpIp: Optional[str] = Field(validation_alias="deviceSnmpIp", default=None)

    deviceSnmpCommunity: Optional[str] = Field(
        validation_alias="deviceSnmpCommunity", default=None
    )

    minimizeSnmp: Optional[bool] = Field(validation_alias="minimizeSnmp", default=None)

    deviceBgpType: Optional[str] = Field(validation_alias="deviceBgpType", default=None)

    deviceBgpNeighborIp: Optional[str] = Field(
        validation_alias="deviceBgpNeighborIp", default=None
    )

    deviceBgpNeighborIp6: Optional[str] = Field(
        validation_alias="deviceBgpNeighborIp6", default=None
    )

    deviceBgpNeighborAsn: Optional[str] = Field(
        validation_alias="deviceBgpNeighborAsn", default=None
    )

    deviceBgpFlowspec: Optional[bool] = Field(
        validation_alias="deviceBgpFlowspec", default=None
    )

    deviceBgpPassword: Optional[str] = Field(
        validation_alias="deviceBgpPassword", default=None
    )

    deviceBgpLabelUnicast: Optional[bool] = Field(
        validation_alias="deviceBgpLabelUnicast", default=None
    )

    bgpLookupStrategy: Optional[str] = Field(
        validation_alias="bgpLookupStrategy", default=None
    )

    deviceStatus: Optional[str] = Field(validation_alias="deviceStatus", default=None)

    useBgpDeviceId: Optional[str] = Field(
        validation_alias="useBgpDeviceId", default=None
    )

    customColumns: Optional[str] = Field(validation_alias="customColumns", default=None)

    customColumnData: Optional[List[Optional[CustomColumnData]]] = Field(
        validation_alias="customColumnData", default=None
    )

    deviceChfClientPort: Optional[str] = Field(
        validation_alias="deviceChfClientPort", default=None
    )

    deviceChfClientProtocol: Optional[str] = Field(
        validation_alias="deviceChfClientProtocol", default=None
    )

    deviceChfInterface: Optional[str] = Field(
        validation_alias="deviceChfInterface", default=None
    )

    deviceAgentType: Optional[str] = Field(
        validation_alias="deviceAgentType", default=None
    )

    maxFlowRate: Optional[int] = Field(validation_alias="maxFlowRate", default=None)

    maxBigFlowRate: Optional[int] = Field(
        validation_alias="maxBigFlowRate", default=None
    )

    deviceProxyBgp: Optional[str] = Field(
        validation_alias="deviceProxyBgp", default=None
    )

    deviceProxyBgp6: Optional[str] = Field(
        validation_alias="deviceProxyBgp6", default=None
    )

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)

    deviceSnmpV3ConfEnabled: Optional[bool] = Field(
        validation_alias="deviceSnmpV3ConfEnabled", default=None
    )

    deviceSnmpV3Conf: Optional[DeviceSnmpV3Conf] = Field(
        validation_alias="deviceSnmpV3Conf", default=None
    )

    cdnAttr: Optional[str] = Field(validation_alias="cdnAttr", default=None)

    bgpPeerIp4: Optional[str] = Field(validation_alias="bgpPeerIp4", default=None)

    bgpPeerIp6: Optional[str] = Field(validation_alias="bgpPeerIp6", default=None)

    deviceSubtype: Optional[str] = Field(validation_alias="deviceSubtype", default=None)

    deviceVendorType: Optional[str] = Field(
        validation_alias="deviceVendorType", default=None
    )

    deviceModelType: Optional[str] = Field(
        validation_alias="deviceModelType", default=None
    )

    cloudExportId: Optional[str] = Field(validation_alias="cloudExportId", default=None)

    deviceKproxy: Optional[str] = Field(validation_alias="deviceKproxy", default=None)

    snmpEnabled: Optional[str] = Field(validation_alias="snmpEnabled", default=None)

    snmpDisabledReason: Optional[str] = Field(
        validation_alias="snmpDisabledReason", default=None
    )

    snmpDisabledReasonOther: Optional[str] = Field(
        validation_alias="snmpDisabledReasonOther", default=None
    )

    bgpDisabledReason: Optional[str] = Field(
        validation_alias="bgpDisabledReason", default=None
    )

    bgpDisabledReasonOther: Optional[str] = Field(
        validation_alias="bgpDisabledReasonOther", default=None
    )

    deviceManufacturer: Optional[str] = Field(
        validation_alias="deviceManufacturer", default=None
    )

    deviceAlert: Optional[str] = Field(validation_alias="deviceAlert", default=None)

    role: Optional[str] = Field(validation_alias="role", default=None)

    deviceGnmiV1Conf: Optional[GnmiV1Conf] = Field(
        validation_alias="deviceGnmiV1Conf", default=None
    )

    useAsnFromFlow: Optional[bool] = Field(
        validation_alias="useAsnFromFlow", default=None
    )

    maxInterface: Optional[int] = Field(validation_alias="maxInterface", default=None)

    maxInterfaceCheck: Optional[int] = Field(
        validation_alias="maxInterfaceCheck", default=None
    )

    nms: Optional[DeviceNmsConfig] = Field(validation_alias="nms", default=None)

    deviceBgpCredentialName: Optional[str] = Field(
        validation_alias="deviceBgpCredentialName", default=None
    )

    flowSnmpCredentialName: Optional[str] = Field(
        validation_alias="flowSnmpCredentialName", default=None
    )

    monitoringTemplateId: Optional[int] = Field(
        validation_alias="monitoringTemplateId", default=None
    )

    osName: Optional[str] = Field(validation_alias="osName", default=None)

    osVersion: Optional[str] = Field(validation_alias="osVersion", default=None)

    serialNumber: Optional[str] = Field(validation_alias="serialNumber", default=None)
