# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .SessionStatus import SessionStatus


class UpdateChatSessionResponse(BaseModel):
    """
    UpdateChatSessionResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    status: Optional[SessionStatus] = Field(validation_alias="status", default=None)
