# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class Interface(BaseModel):
    """
    Interface model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    interfaceDescription: Optional[str] = Field(
        validation_alias="interfaceDescription", default=None
    )

    initialSnmpSpeed: Optional[str] = Field(
        validation_alias="initialSnmpSpeed", default=None
    )

    deviceId: Optional[str] = Field(validation_alias="deviceId", default=None)

    snmpSpeed: Optional[str] = Field(validation_alias="snmpSpeed", default=None)

    snmpAlias: Optional[str] = Field(validation_alias="snmpAlias", default=None)

    snmpId: Optional[str] = Field(validation_alias="snmpId", default=None)

    connectivityType: Optional[str] = Field(
        validation_alias="connectivityType", default=None
    )

    networkBoundary: Optional[str] = Field(
        validation_alias="networkBoundary", default=None
    )

    provider: Optional[str] = Field(validation_alias="provider", default=None)
