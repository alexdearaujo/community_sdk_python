from typing import Any, Dict

from pydantic import BaseModel, Field


class SuppressionServiceReplaceBody(BaseModel):
    """
    SuppressionServiceReplaceBody model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    suppression: Dict[str, Any] = Field(validation_alias="suppression")
