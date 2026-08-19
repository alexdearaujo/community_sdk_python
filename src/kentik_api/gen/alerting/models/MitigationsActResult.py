# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class MitigationsActResult(BaseModel):
    """
    MitigationsActResult model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    mitigationId: Optional[str] = Field(validation_alias="mitigationId", default=None)

    success: Optional[bool] = Field(validation_alias="success", default=None)

    message: Optional[str] = Field(validation_alias="message", default=None)
