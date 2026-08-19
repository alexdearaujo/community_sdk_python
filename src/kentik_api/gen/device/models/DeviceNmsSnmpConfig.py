# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class DeviceNmsSnmpConfig(BaseModel):
    """
    DeviceNmsSnmpConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    credentialName: Optional[str] = Field(
        validation_alias="credentialName", default=None
    )

    port: Optional[int] = Field(validation_alias="port", default=None)

    timeout: Optional[str] = Field(validation_alias="timeout", default=None)
