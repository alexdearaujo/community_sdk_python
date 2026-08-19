# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .MitigationState import MitigationState
from .MitigationStateEntry import MitigationStateEntry
from .MitigationType import MitigationType
from .Source import Source
from .v202506MitigationTarget import v202506MitigationTarget


class Mitigation(BaseModel):
    """
    Mitigation model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    type: Optional[MitigationType] = Field(validation_alias="type", default=None)

    alarmIds: Optional[List[str]] = Field(validation_alias="alarmIds", default=None)

    target: Optional[v202506MitigationTarget] = Field(
        validation_alias="target", default=None
    )

    currentState: Optional[MitigationState] = Field(
        validation_alias="currentState", default=None
    )

    previousState: Optional[MitigationState] = Field(
        validation_alias="previousState", default=None
    )

    platformId: Optional[str] = Field(validation_alias="platformId", default=None)

    methodId: Optional[str] = Field(validation_alias="methodId", default=None)

    startTimeAt: Optional[str] = Field(validation_alias="startTimeAt", default=None)

    endTimeAt: Optional[str] = Field(validation_alias="endTimeAt", default=None)

    states: Optional[List[Optional[MitigationStateEntry]]] = Field(
        validation_alias="states", default=None
    )

    autoStopTtl: Optional[str] = Field(validation_alias="autoStopTtl", default=None)

    comment: Optional[str] = Field(validation_alias="comment", default=None)

    source: Optional[Source] = Field(validation_alias="source", default=None)
