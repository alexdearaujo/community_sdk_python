# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .Nlri import Nlri


class GetRoutesForTargetRequest(BaseModel):
    """
    GetRoutesForTargetRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    time: str = Field(validation_alias="time")

    target: Nlri = Field(validation_alias="target")

    includeCovered: Optional[bool] = Field(
        validation_alias="includeCovered", default=None
    )

    checkRpki: Optional[bool] = Field(validation_alias="checkRpki", default=None)
