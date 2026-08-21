# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .TokenRevoked import TokenRevoked


class RevokeProvisioningTokenResponse(BaseModel):
    """
    RevokeProvisioningTokenResponse model
    RevokeProvisioningTokenResponse
    Response message for revoking a provisioning token.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    revoked: Optional[TokenRevoked] = Field(validation_alias="revoked", default=None)
