from typing import List, Optional

from pydantic import BaseModel, Field

from .MitigationPlatform import MitigationPlatform
from .typesv202506PaginationInfo import typesv202506PaginationInfo


class MitigationPlatformsServiceListResponse(BaseModel):
    """
    MitigationPlatformsServiceListResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    pagination: Optional[typesv202506PaginationInfo] = Field(
        validation_alias="pagination", default=None
    )

    platforms: Optional[List[Optional[MitigationPlatform]]] = Field(
        validation_alias="platforms", default=None
    )
