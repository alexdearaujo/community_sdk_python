from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class FetchValuesByIdsResponse(BaseModel):
    """
    FetchValuesByIdsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    values: Optional[Dict[str, Any]] = Field(validation_alias="values", default=None)
