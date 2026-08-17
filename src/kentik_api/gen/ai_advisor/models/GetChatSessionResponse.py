from typing import List, Optional

from pydantic import BaseModel, Field

from .ChatMessage import ChatMessage
from .SessionStatus import SessionStatus


class GetChatSessionResponse(BaseModel):
    """
    GetChatSessionResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    status: Optional[SessionStatus] = Field(validation_alias="status", default=None)

    messages: Optional[List[Optional[ChatMessage]]] = Field(
        validation_alias="messages", default=None
    )
