# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class Market(BaseModel):
    """
    Market model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    marketId: Optional[str] = Field(validation_alias="marketId", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)
