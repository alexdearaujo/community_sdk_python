from typing import List, Optional

from pydantic import BaseModel, Field


class AlertServiceClearResponse(BaseModel):
    """
    AlertServiceClearResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    clearedAlertIds: Optional[List[str]] = Field(
        validation_alias="clearedAlertIds", default=None
    )
