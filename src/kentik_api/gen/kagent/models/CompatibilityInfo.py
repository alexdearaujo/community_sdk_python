# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class CompatibilityInfo(BaseModel):
    """
    CompatibilityInfo provides details when a distro fallback was used model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tier: Optional[int] = Field(validation_alias="tier", default=None)

    tierName: Optional[str] = Field(validation_alias="tierName", default=None)

    requestedDistro: Optional[str] = Field(
        validation_alias="requestedDistro", default=None
    )

    matchedDistro: Optional[str] = Field(validation_alias="matchedDistro", default=None)

    message: Optional[str] = Field(validation_alias="message", default=None)
