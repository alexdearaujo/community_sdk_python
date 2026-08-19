# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .MitigationPlatformType import MitigationPlatformType


class MitigationPlatform(BaseModel):
    """
    MitigationPlatform model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    type: Optional[MitigationPlatformType] = Field(
        validation_alias="type", default=None
    )

    mitigationMethodIds: Optional[List[str]] = Field(
        validation_alias="mitigationMethodIds", default=None
    )

    createdAt: Optional[str] = Field(validation_alias="createdAt", default=None)

    modifiedAt: Optional[str] = Field(validation_alias="modifiedAt", default=None)
