# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class ProvisioningTokenAgentConfig(BaseModel):
    """
    AgentConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    siteId: Optional[str] = Field(validation_alias="siteId", default=None)
