# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .labelv202210Label import labelv202210Label


class UpdateLabelResponse(BaseModel):
    """
    UpdateLabelResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    label: Optional[labelv202210Label] = Field(validation_alias="label", default=None)
