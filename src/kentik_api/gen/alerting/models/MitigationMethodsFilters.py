from typing import List, Optional

from pydantic import BaseModel, Field

from .MitigationPlatformType import MitigationPlatformType
from .v202303TimeRange import v202303TimeRange


class MitigationMethodsFilters(BaseModel):
    """
    MitigationMethodsFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    methodIds: Optional[List[str]] = Field(validation_alias="methodIds", default=None)

    platformTypes: Optional[List[Optional[MitigationPlatformType]]] = Field(
        validation_alias="platformTypes", default=None
    )

    createdAt: Optional[v202303TimeRange] = Field(
        validation_alias="createdAt", default=None
    )

    modifiedAt: Optional[v202303TimeRange] = Field(
        validation_alias="modifiedAt", default=None
    )
