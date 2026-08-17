from typing import Any, Dict

from pydantic import BaseModel, Field


class LabelServiceUpdateLabelBody(BaseModel):
    """
    UpdateLabelRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    label: Dict[str, Any] = Field(validation_alias="label")
