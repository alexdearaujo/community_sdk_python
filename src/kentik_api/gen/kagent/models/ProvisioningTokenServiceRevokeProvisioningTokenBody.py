# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class ProvisioningTokenServiceRevokeProvisioningTokenBody(BaseModel):
    """
    ProvisioningTokenServiceRevokeProvisioningTokenBody model
    RevokeProvisioningTokenRequest
    Request message for revoking a provisioning token.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    revokedBy: Optional[str] = Field(validation_alias="revokedBy", default=None)
