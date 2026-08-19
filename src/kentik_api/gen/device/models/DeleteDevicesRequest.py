# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List

from pydantic import BaseModel, Field


class DeleteDevicesRequest(BaseModel):
    """
    DeleteDevicesRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    ids: List[str] = Field(validation_alias="ids")
