# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class AgentTest(BaseModel):
    """
    AgentTest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    target: Optional[str] = Field(validation_alias="target", default=None)

    useLocalIp: Optional[bool] = Field(validation_alias="useLocalIp", default=None)

    reciprocal: Optional[bool] = Field(validation_alias="reciprocal", default=None)
