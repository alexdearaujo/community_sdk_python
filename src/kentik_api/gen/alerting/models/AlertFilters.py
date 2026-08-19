# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .AlertAcknowledgement import AlertAcknowledgement
from .AlertState import AlertState
from .Source import Source
from .v202303MultiAttributeFilter import v202303MultiAttributeFilter
from .v202303Severity import v202303Severity
from .v202303TimeRange import v202303TimeRange


class AlertFilters(BaseModel):
    """
    AlertFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    severities: Optional[List[Optional[v202303Severity]]] = Field(
        validation_alias="severities", default=None
    )

    alertIds: Optional[List[str]] = Field(validation_alias="alertIds", default=None)

    sources: Optional[List[Optional[Source]]] = Field(
        validation_alias="sources", default=None
    )

    keys: Optional[v202303MultiAttributeFilter] = Field(
        validation_alias="keys", default=None
    )

    states: Optional[List[Optional[AlertState]]] = Field(
        validation_alias="states", default=None
    )

    startedAt: Optional[v202303TimeRange] = Field(
        validation_alias="startedAt", default=None
    )

    endedAt: Optional[v202303TimeRange] = Field(
        validation_alias="endedAt", default=None
    )

    highestSeverities: Optional[List[Optional[v202303Severity]]] = Field(
        validation_alias="highestSeverities", default=None
    )

    recentSeverities: Optional[List[Optional[v202303Severity]]] = Field(
        validation_alias="recentSeverities", default=None
    )

    ackStates: Optional[List[Optional[AlertAcknowledgement]]] = Field(
        validation_alias="ackStates", default=None
    )

    activeAt: Optional[v202303TimeRange] = Field(
        validation_alias="activeAt", default=None
    )

    ackedByUserIds: Optional[List[str]] = Field(
        validation_alias="ackedByUserIds", default=None
    )

    includeRemovedPolicies: Optional[bool] = Field(
        validation_alias="includeRemovedPolicies", default=None
    )

    contextSearch: Optional[List[str]] = Field(
        validation_alias="contextSearch", default=None
    )
