# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class ConfigUtilConfig(BaseModel):
    """
    UtilConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    aggregate: Optional[str] = Field(validation_alias="aggregate", default=None)

    warnPct: Optional[int] = Field(validation_alias="warnPct", default=None)

    critPct: Optional[int] = Field(validation_alias="critPct", default=None)
