# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class SyntheticsAdminServiceUpdateAgentBody(BaseModel):
    """
    UpdateAgentRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    agent: Optional[Dict[str, Any]] = Field(validation_alias="agent", default=None)
