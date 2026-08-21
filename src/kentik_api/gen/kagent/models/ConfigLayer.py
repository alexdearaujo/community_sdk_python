# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .ConfigLayerLayerType import ConfigLayerLayerType


class ConfigLayer(BaseModel):
    """
    ConfigLayer model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: Optional[str] = Field(validation_alias="name", default=None)

    type: Optional[ConfigLayerLayerType] = Field(validation_alias="type", default=None)
