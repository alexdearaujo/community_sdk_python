from typing import List, Optional

from pydantic import BaseModel, Field

from .Revision import Revision


class ListDeviceConfigurationRevisionsResponse(BaseModel):
    """
    ListDeviceConfigurationRevisionsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    revisions: Optional[List[Optional[Revision]]] = Field(
        validation_alias="revisions", default=None
    )
