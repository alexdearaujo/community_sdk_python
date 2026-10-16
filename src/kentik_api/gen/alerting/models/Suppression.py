# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .Source import Source
from .v202303MultiAttributeFilter import v202303MultiAttributeFilter
from .v202303Severity import v202303Severity


class Suppression(BaseModel):
    """
    Suppression model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(
        validation_alias="id",
        default=None,
        description="The ID of the suppression configuration.",
    )

    userId: Optional[str] = Field(
        validation_alias="userId",
        default=None,
        description="The ID of the user who most recently updated the suppression configuration.",
    )

    source: Optional[Source] = Field(validation_alias="source", default=None)

    keyFilter: Optional[v202303MultiAttributeFilter] = Field(
        validation_alias="keyFilter", default=None
    )

    strict: Optional[bool] = Field(
        validation_alias="strict",
        default=None,
        description="Whether the suppression is strict (all alert key dimensions must have some filter applied and matching).",
    )

    comment: Optional[str] = Field(
        validation_alias="comment",
        default=None,
        description="The comment for the suppression configuration.",
    )

    startTimeAt: str = Field(
        validation_alias="startTimeAt",
        description="The start time when the suppression configuration is active, preventing the alert from being activated.",
    )

    endTimeAt: Optional[str] = Field(
        validation_alias="endTimeAt",
        default=None,
        description="The end time when the suppression configuration is no longer active, allowing the alert to be activated again.",
    )

    createdAt: Optional[str] = Field(
        validation_alias="createdAt",
        default=None,
        description="The time when the suppression configuration was created.",
    )

    modifiedAt: Optional[str] = Field(
        validation_alias="modifiedAt",
        default=None,
        description="The time when the suppression configuration was last modified.",
    )

    displayName: Optional[str] = Field(
        validation_alias="displayName",
        default=None,
        description="The name of the suppression configuration.",
    )

    severities: Optional[List[Optional[v202303Severity]]] = Field(
        validation_alias="severities",
        default=None,
        description="The alarm severities the suppression applies to.",
    )
