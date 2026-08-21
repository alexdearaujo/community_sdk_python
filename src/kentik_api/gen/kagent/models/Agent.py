# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .InstallConfig import InstallConfig
from .kagentv202401AgentConfig import kagentv202401AgentConfig


class Agent(BaseModel):
    """
    Agent model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    running: Optional[bool] = Field(validation_alias="running", default=None)

    clusterId: Optional[str] = Field(validation_alias="clusterId", default=None)

    publicKey: Optional[str] = Field(validation_alias="publicKey", default=None)

    provisioningToken: Optional[str] = Field(
        validation_alias="provisioningToken", default=None
    )

    config: Optional[kagentv202401AgentConfig] = Field(
        validation_alias="config", default=None
    )

    install: Optional[InstallConfig] = Field(validation_alias="install", default=None)
