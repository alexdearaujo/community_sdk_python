# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field


class FlowContextDeviceDetails(BaseModel):
    """
    FlowContextDeviceDetails model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    type: Optional[str] = Field(validation_alias="type", default=None)

    labels: Optional[List[str]] = Field(validation_alias="labels", default=None)
