# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class ConfigRunoutConfig(BaseModel):
    """
    RunoutConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    strategy: Optional[str] = Field(validation_alias="strategy", default=None)

    warnQty: Optional[int] = Field(validation_alias="warnQty", default=None)

    critQty: Optional[int] = Field(validation_alias="critQty", default=None)
