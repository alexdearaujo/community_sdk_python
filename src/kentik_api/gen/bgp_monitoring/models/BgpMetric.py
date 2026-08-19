# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .Nlri import Nlri


class BgpMetric(BaseModel):
    """
    BgpMetric model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    timestamp: Optional[str] = Field(validation_alias="timestamp", default=None)

    nlri: Optional[Nlri] = Field(validation_alias="nlri", default=None)

    reachability: Optional[float] = Field(validation_alias="reachability", default=None)

    pathChanges: Optional[int] = Field(validation_alias="pathChanges", default=None)
