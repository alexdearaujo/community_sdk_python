# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class GceProperties(BaseModel):
    """
    GceProperties model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    project: str = Field(validation_alias="project")

    subscription: Optional[str] = Field(validation_alias="subscription", default=None)

    metadataOnly: Optional[bool] = Field(validation_alias="metadataOnly", default=None)

    collectFlowLogs: Optional[bool] = Field(
        validation_alias="collectFlowLogs", default=None
    )

    collectMetrics: Optional[bool] = Field(
        validation_alias="collectMetrics", default=None
    )
