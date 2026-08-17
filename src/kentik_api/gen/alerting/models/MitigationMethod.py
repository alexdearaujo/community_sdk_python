from typing import List, Optional

from pydantic import BaseModel, Field

from .MitigationPlatformType import MitigationPlatformType
from .NotificationChannelAssociation import NotificationChannelAssociation


class MitigationMethod(BaseModel):
    """
    MitigationMethod model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    ackRequired: Optional[bool] = Field(validation_alias="ackRequired", default=None)

    excludedIpCidrs: Optional[List[str]] = Field(
        validation_alias="excludedIpCidrs", default=None
    )

    gracePeriod: Optional[str] = Field(validation_alias="gracePeriod", default=None)

    type: Optional[MitigationPlatformType] = Field(
        validation_alias="type", default=None
    )

    createdAt: Optional[str] = Field(validation_alias="createdAt", default=None)

    modifiedAt: Optional[str] = Field(validation_alias="modifiedAt", default=None)

    notifications: Optional[List[Optional[NotificationChannelAssociation]]] = Field(
        validation_alias="notifications", default=None
    )
