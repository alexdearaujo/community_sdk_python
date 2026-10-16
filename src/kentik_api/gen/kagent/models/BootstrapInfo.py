# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class BootstrapInfo(BaseModel):
    """
    BootstrapInfo model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    linuxInstallCommand: Optional[str] = Field(
        validation_alias="linuxInstallCommand", default=None
    )

    dockerInstallCommand: Optional[str] = Field(
        validation_alias="dockerInstallCommand", default=None
    )

    provisioningToken: Optional[str] = Field(
        validation_alias="provisioningToken", default=None
    )
