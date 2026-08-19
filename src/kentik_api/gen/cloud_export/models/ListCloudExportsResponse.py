# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .CloudExport import CloudExport


class ListCloudExportsResponse(BaseModel):
    """
    ListCloudExportsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    exports: Optional[List[Optional[CloudExport]]] = Field(
        validation_alias="exports", default=None
    )

    invalidExportsCount: Optional[int] = Field(
        validation_alias="invalidExportsCount", default=None
    )
