# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class BgpHealthSettings(BaseModel):
    """
    BgpHealthSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    reachabilityWarning: Optional[float] = Field(
        validation_alias="reachabilityWarning", default=None
    )

    reachabilityCritical: Optional[float] = Field(
        validation_alias="reachabilityCritical", default=None
    )
