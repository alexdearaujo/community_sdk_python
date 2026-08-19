# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .DeviceNmsConfig import DeviceNmsConfig
from .DeviceSnmpV3Conf import DeviceSnmpV3Conf


class DeviceConcise(BaseModel):
    """
    DeviceConcise model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    deviceName: Optional[str] = Field(validation_alias="deviceName", default=None)

    deviceSubtype: Optional[str] = Field(validation_alias="deviceSubtype", default=None)

    cdnAttr: Optional[str] = Field(validation_alias="cdnAttr", default=None)

    deviceDescription: Optional[str] = Field(
        validation_alias="deviceDescription", default=None
    )

    sendingIps: Optional[List[str]] = Field(validation_alias="sendingIps", default=None)

    deviceSampleRate: Optional[float] = Field(
        validation_alias="deviceSampleRate", default=None
    )

    planId: Optional[int] = Field(validation_alias="planId", default=None)

    siteId: Optional[int] = Field(validation_alias="siteId", default=None)

    minimizeSnmp: Optional[bool] = Field(validation_alias="minimizeSnmp", default=None)

    deviceSnmpIp: Optional[str] = Field(validation_alias="deviceSnmpIp", default=None)

    deviceSnmpCommunity: Optional[str] = Field(
        validation_alias="deviceSnmpCommunity", default=None
    )

    deviceSnmpV3Conf: Optional[DeviceSnmpV3Conf] = Field(
        validation_alias="deviceSnmpV3Conf", default=None
    )

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

    deviceBgpPassword: Optional[str] = Field(
        validation_alias="deviceBgpPassword", default=None
    )

    useBgpDeviceId: Optional[str] = Field(
        validation_alias="useBgpDeviceId", default=None
    )

    deviceBgpFlowspec: Optional[bool] = Field(
        validation_alias="deviceBgpFlowspec", default=None
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

    deviceAlert: Optional[str] = Field(validation_alias="deviceAlert", default=None)
