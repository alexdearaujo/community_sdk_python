# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field

from .labelv202210Label import labelv202210Label


class CreateLabelRequest(BaseModel):
    """
    CreateLabelRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    label: labelv202210Label = Field(validation_alias="label")
