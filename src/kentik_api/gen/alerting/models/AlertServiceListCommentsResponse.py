from typing import List, Optional

from pydantic import BaseModel, Field

from .Comment import Comment


class AlertServiceListCommentsResponse(BaseModel):
    """
    AlertServiceListCommentsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    comments: Optional[List[Optional[Comment]]] = Field(
        validation_alias="comments", default=None
    )
