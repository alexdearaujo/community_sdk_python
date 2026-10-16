# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class TelemetryConfig(BaseModel):
    """
    TelemetryConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    logsEndpoint: Optional[str] = Field(validation_alias="logsEndpoint", default=None)

    metricsEndpoint: Optional[str] = Field(
        validation_alias="metricsEndpoint", default=None
    )

    kmetricsEndpoint: Optional[str] = Field(
        validation_alias="kmetricsEndpoint", default=None
    )

    sentryEndpoint: Optional[str] = Field(
        validation_alias="sentryEndpoint", default=None
    )
