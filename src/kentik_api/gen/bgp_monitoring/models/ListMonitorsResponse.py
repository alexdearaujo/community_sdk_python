# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .BgpMonitor import BgpMonitor


class ListMonitorsResponse(BaseModel):
    """
    ListMonitorsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    monitors: Optional[List[Optional[BgpMonitor]]] = Field(
        validation_alias="monitors", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
