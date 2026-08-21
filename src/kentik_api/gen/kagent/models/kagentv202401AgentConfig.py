# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class kagentv202401AgentConfig(BaseModel):
    """
    AgentConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    created: Optional[str] = Field(validation_alias="created", default=None)

    edited: Optional[str] = Field(validation_alias="edited", default=None)

    siteId: Optional[str] = Field(validation_alias="siteId", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    releaseChannel: Optional[str] = Field(
        validation_alias="releaseChannel", default=None
    )

    osDistribution: Optional[str] = Field(
        validation_alias="osDistribution", default=None
    )
