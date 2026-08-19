# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class CloudExportAdminServiceUpdateCloudExportBody(BaseModel):
    """
    UpdateCloudExportRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    export: Optional[Dict[str, Any]] = Field(validation_alias="export", default=None)
