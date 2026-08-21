# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class HostMetadata(BaseModel):
    """
    HostMetadata
    Read-only metadata about a host system model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    hostname: Optional[str] = Field(validation_alias="hostname", default=None)

    machineId: Optional[str] = Field(validation_alias="machineId", default=None)

    publicIp: Optional[str] = Field(validation_alias="publicIp", default=None)

    privateIp: Optional[str] = Field(validation_alias="privateIp", default=None)

    os: Optional[str] = Field(validation_alias="os", default=None)

    arch: Optional[str] = Field(validation_alias="arch", default=None)
