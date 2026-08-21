# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class AgentCapability(BaseModel):
    """
    AgentCapability model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: Optional[str] = Field(validation_alias="name", default=None)

    bundleId: Optional[str] = Field(validation_alias="bundleId", default=None)

    enabled: Optional[bool] = Field(validation_alias="enabled", default=None)

    version: Optional[str] = Field(validation_alias="version", default=None)

    channel: Optional[str] = Field(validation_alias="channel", default=None)

    configId: Optional[str] = Field(validation_alias="configId", default=None)

    groupId: Optional[str] = Field(validation_alias="groupId", default=None)

    groupIndex: Optional[int] = Field(validation_alias="groupIndex", default=None)
