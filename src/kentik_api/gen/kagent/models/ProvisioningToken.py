# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .ProvisioningTokenAgentConfig import ProvisioningTokenAgentConfig
from .TokenRevoked import TokenRevoked


class ProvisioningToken(BaseModel):
    """
    ProvisioningToken model
    ProvisioningToken
    ProvisioningToken represents a provisioning token for automated agent registration.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    token: Optional[str] = Field(validation_alias="token", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    maxUsageCount: Optional[int] = Field(validation_alias="maxUsageCount", default=None)

    currentUsageCount: Optional[int] = Field(
        validation_alias="currentUsageCount", default=None
    )

    expiresAt: Optional[str] = Field(validation_alias="expiresAt", default=None)

    allowedPrivateCidrs: Optional[List[str]] = Field(
        validation_alias="allowedPrivateCidrs", default=None
    )

    allowedPublicCidrs: Optional[List[str]] = Field(
        validation_alias="allowedPublicCidrs", default=None
    )

    clusterId: Optional[str] = Field(validation_alias="clusterId", default=None)

    requiresApproval: Optional[bool] = Field(
        validation_alias="requiresApproval", default=None
    )

    config: Optional[ProvisioningTokenAgentConfig] = Field(
        validation_alias="config", default=None
    )

    revoked: Optional[TokenRevoked] = Field(validation_alias="revoked", default=None)

    createdBy: Optional[str] = Field(validation_alias="createdBy", default=None)

    ctime: Optional[str] = Field(validation_alias="ctime", default=None)

    utime: Optional[str] = Field(validation_alias="utime", default=None)
