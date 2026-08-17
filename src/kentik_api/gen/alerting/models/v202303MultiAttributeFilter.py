from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .v202303KeyValueFilter import v202303KeyValueFilter


class v202303MultiAttributeFilter(BaseModel):
    """
    v202303MultiAttributeFilter model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    filter: Optional[Dict[str, Any]] = Field(validation_alias="filter", default=None)

    filters: Optional[List[Optional[v202303KeyValueFilter]]] = Field(
        validation_alias="filters", default=None
    )
