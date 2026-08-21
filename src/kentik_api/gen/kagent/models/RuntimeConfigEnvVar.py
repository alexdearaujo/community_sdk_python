# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class RuntimeConfigEnvVar(BaseModel):
    """
    EnvVar model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: Optional[str] = Field(validation_alias="name", default=None)

    value: Optional[str] = Field(validation_alias="value", default=None)

    origin: Optional[str] = Field(validation_alias="origin", default=None)
