# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class FlowContextInterfaceDetails(BaseModel):
    """
    FlowContextInterfaceDetails model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    snmpId: Optional[str] = Field(validation_alias="snmpId", default=None)

    snmpAlias: Optional[str] = Field(validation_alias="snmpAlias", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    snmpSpeedMbps: Optional[str] = Field(validation_alias="snmpSpeedMbps", default=None)
