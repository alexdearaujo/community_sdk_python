# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .RuntimeConfigEnvVar import RuntimeConfigEnvVar


class RuntimeConfig(BaseModel):
    """
    RuntimeConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    args: Optional[List[str]] = Field(validation_alias="args", default=None)

    env: Optional[List[Optional[RuntimeConfigEnvVar]]] = Field(
        validation_alias="env", default=None
    )

    binary: Optional[str] = Field(validation_alias="binary", default=None)

    linuxCapabilities: Optional[List[str]] = Field(
        validation_alias="linuxCapabilities", default=None
    )
