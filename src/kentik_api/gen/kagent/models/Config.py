# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .ConfigLayer import ConfigLayer
from .RuntimeConfig import RuntimeConfig
from .TelemetryConfig import TelemetryConfig


class Config(BaseModel):
    """
    Config model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: Optional[str] = Field(validation_alias="name", default=None)

    capability: Optional[str] = Field(validation_alias="capability", default=None)

    version: Optional[str] = Field(validation_alias="version", default=None)

    runtime: Optional[RuntimeConfig] = Field(validation_alias="runtime", default=None)

    telemetry: Optional[TelemetryConfig] = Field(
        validation_alias="telemetry", default=None
    )

    layers: Optional[List[Optional[ConfigLayer]]] = Field(
        validation_alias="layers", default=None
    )
