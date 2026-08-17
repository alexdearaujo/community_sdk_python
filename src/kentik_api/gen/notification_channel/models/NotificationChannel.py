from typing import Optional

from pydantic import BaseModel, Field

from .ChannelType import ChannelType


class NotificationChannel(BaseModel):
    """
    NotificationChannel model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    type: Optional[ChannelType] = Field(validation_alias="type", default=None)

    enabled: Optional[bool] = Field(validation_alias="enabled", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)
