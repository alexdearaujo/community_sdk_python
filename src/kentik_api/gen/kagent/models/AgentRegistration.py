# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class AgentRegistration(BaseModel):
    """
    AgentRegistration model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    publicKey: Optional[str] = Field(validation_alias="publicKey", default=None)

    siteId: Optional[str] = Field(validation_alias="siteId", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    releaseChannel: Optional[str] = Field(
        validation_alias="releaseChannel", default=None
    )

    clusterId: Optional[str] = Field(validation_alias="clusterId", default=None)
