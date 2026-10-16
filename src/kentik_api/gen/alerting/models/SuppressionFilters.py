# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .Source import Source
from .TimeRange import TimeRange


class SuppressionFilters(BaseModel):
    """
    SuppressionFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    suppressionIds: Optional[List[str]] = Field(
        validation_alias="suppressionIds",
        default=None,
        description="The IDs of the suppression configurations to list.",
    )

    sources: Optional[List[Optional[Source]]] = Field(
        validation_alias="sources",
        default=None,
        description="The source policies the suppression configurations are applied to.",
    )

    userIds: Optional[List[str]] = Field(
        validation_alias="userIds",
        default=None,
        description="The IDs of the users who created the suppression configurations.",
    )

    createdAt: Optional[TimeRange] = Field(validation_alias="createdAt", default=None)

    modifiedAt: Optional[TimeRange] = Field(validation_alias="modifiedAt", default=None)

    startTimeAt: Optional[TimeRange] = Field(
        validation_alias="startTimeAt", default=None
    )

    endTimeAt: Optional[TimeRange] = Field(validation_alias="endTimeAt", default=None)
