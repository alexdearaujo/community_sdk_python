# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List

from pydantic import BaseModel, Field

from .LabelConcise import LabelConcise


class DeviceServiceUpdateDeviceLabelsBody(BaseModel):
    """
    UpdateDeviceLabelsRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    labels: List[LabelConcise] = Field(validation_alias="labels")
