# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class CloudExportStatus(BaseModel):
    """
    CloudExportStatus model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    status: Optional[str] = Field(validation_alias="status", default=None)

    errorMessage: Optional[str] = Field(validation_alias="errorMessage", default=None)

    flowFound: Optional[bool] = Field(validation_alias="flowFound", default=None)

    apiAccess: Optional[bool] = Field(validation_alias="apiAccess", default=None)

    storageAccountAccess: Optional[bool] = Field(
        validation_alias="storageAccountAccess", default=None
    )
