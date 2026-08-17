from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .RouteInfo import RouteInfo


class GetRoutesForTargetResponse(BaseModel):
    """
    GetRoutesForTargetResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    routes: Optional[List[Optional[RouteInfo]]] = Field(
        validation_alias="routes", default=None
    )

    asNames: Optional[Dict[str, Any]] = Field(validation_alias="asNames", default=None)
