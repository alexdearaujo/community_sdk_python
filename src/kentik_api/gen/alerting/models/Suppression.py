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

    id: Optional[str] = Field(validation_alias="id", default=None)

    userId: Optional[str] = Field(validation_alias="userId", default=None)

    source: Optional[Source] = Field(validation_alias="source", default=None)

    keyFilter: Optional[v202303MultiAttributeFilter] = Field(
        validation_alias="keyFilter", default=None
    )

    strict: Optional[bool] = Field(validation_alias="strict", default=None)

    comment: Optional[str] = Field(validation_alias="comment", default=None)

    startTimeAt: str = Field(validation_alias="startTimeAt")

    endTimeAt: Optional[str] = Field(validation_alias="endTimeAt", default=None)

    createdAt: Optional[str] = Field(validation_alias="createdAt", default=None)

    modifiedAt: Optional[str] = Field(validation_alias="modifiedAt", default=None)

    displayName: Optional[str] = Field(validation_alias="displayName", default=None)

    severities: Optional[List[Optional[v202303Severity]]] = Field(
        validation_alias="severities", default=None
    )
