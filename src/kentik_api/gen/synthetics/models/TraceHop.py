# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class TraceHop(BaseModel):
    """
    TraceHop model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    latency: Optional[int] = Field(validation_alias="latency", default=None)

    nodeId: Optional[str] = Field(validation_alias="nodeId", default=None)
