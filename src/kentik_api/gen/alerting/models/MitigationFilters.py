from typing import List, Optional

from pydantic import BaseModel, Field

from .MitigationState import MitigationState
from .MitigationType import MitigationType
from .Source import Source
from .v202303TimeRange import v202303TimeRange


class MitigationFilters(BaseModel):
    """
    MitigationFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    createdAt: Optional[v202303TimeRange] = Field(
        validation_alias="createdAt", default=None
    )

    mitigationIds: Optional[List[str]] = Field(
        validation_alias="mitigationIds", default=None
    )

    sources: Optional[List[Optional[Source]]] = Field(
        validation_alias="sources", default=None
    )

    alarmIds: Optional[List[str]] = Field(validation_alias="alarmIds", default=None)

    states: Optional[List[Optional[MitigationState]]] = Field(
        validation_alias="states", default=None
    )

    platformIds: Optional[List[str]] = Field(
        validation_alias="platformIds", default=None
    )

    methodIds: Optional[List[str]] = Field(validation_alias="methodIds", default=None)

    ipCidrs: Optional[List[str]] = Field(validation_alias="ipCidrs", default=None)

    ipCidrPattern: Optional[str] = Field(validation_alias="ipCidrPattern", default=None)

    types: Optional[List[Optional[MitigationType]]] = Field(
        validation_alias="types", default=None
    )
