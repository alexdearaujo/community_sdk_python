from typing import Optional

from pydantic import BaseModel, Field


class NotificationChannel(BaseModel):
    """
    NotificationChannel model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)
