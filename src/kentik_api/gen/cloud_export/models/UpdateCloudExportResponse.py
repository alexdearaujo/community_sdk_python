from typing import Optional

from pydantic import BaseModel, Field

from .CloudExport import CloudExport


class UpdateCloudExportResponse(BaseModel):
    """
    UpdateCloudExportResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    export: Optional[CloudExport] = Field(validation_alias="export", default=None)
