# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .DeviceNmsSnmpConfig import DeviceNmsSnmpConfig
from .DeviceNmsStConfig import DeviceNmsStConfig


class DeviceNmsConfig(BaseModel):
    """
    DeviceNmsConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    agentId: Optional[str] = Field(validation_alias="agentId", default=None)

    ipAddress: Optional[str] = Field(validation_alias="ipAddress", default=None)

    snmp: Optional[DeviceNmsSnmpConfig] = Field(validation_alias="snmp", default=None)

    st: Optional[DeviceNmsStConfig] = Field(validation_alias="st", default=None)
