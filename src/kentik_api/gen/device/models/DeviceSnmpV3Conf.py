# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class DeviceSnmpV3Conf(BaseModel):
    """
    DeviceSnmpV3Conf model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    username: Optional[str] = Field(validation_alias="username", default=None)

    authenticationProtocol: Optional[str] = Field(
        validation_alias="authenticationProtocol", default=None
    )

    authenticationPassphrase: Optional[str] = Field(
        validation_alias="authenticationPassphrase", default=None
    )

    privacyProtocol: Optional[str] = Field(
        validation_alias="privacyProtocol", default=None
    )

    privacyPassphrase: Optional[str] = Field(
        validation_alias="privacyPassphrase", default=None
    )
