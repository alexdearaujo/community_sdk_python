# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .InterfacesDetailStatusDetail import InterfacesDetailStatusDetail


class CapacitySummaryInterfacesDetail(BaseModel):
    """
    InterfacesDetail model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    totalCount: Optional[int] = Field(validation_alias="totalCount", default=None)

    totalCapacityBps: Optional[str] = Field(
        validation_alias="totalCapacityBps", default=None
    )

    healthy: Optional[InterfacesDetailStatusDetail] = Field(
        validation_alias="healthy", default=None
    )

    warning: Optional[InterfacesDetailStatusDetail] = Field(
        validation_alias="warning", default=None
    )

    critical: Optional[InterfacesDetailStatusDetail] = Field(
        validation_alias="critical", default=None
    )
