from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .Path import Path


class GetTraceForTestResponse(BaseModel):
    """
    GetTraceForTestResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    nodes: Optional[Dict[str, Any]] = Field(validation_alias="nodes", default=None)

    paths: Optional[List[Optional[Path]]] = Field(
        validation_alias="paths", default=None
    )
