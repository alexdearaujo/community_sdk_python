# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class PolicyPolicyErrorInfo(BaseModel):
    """
    PolicyPolicyErrorInfo model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    timestamp: Optional[str] = Field(validation_alias="timestamp", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)
