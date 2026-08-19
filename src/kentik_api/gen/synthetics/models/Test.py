# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .TestSettings import TestSettings
from .TestStatus import TestStatus
from .v202303UserInfo import v202303UserInfo


class Test(BaseModel):
    """
    Test model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    type: Optional[str] = Field(validation_alias="type", default=None)

    status: Optional[TestStatus] = Field(validation_alias="status", default=None)

    settings: Optional[TestSettings] = Field(validation_alias="settings", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    createdBy: Optional[v202303UserInfo] = Field(
        validation_alias="createdBy", default=None
    )

    lastUpdatedBy: Optional[v202303UserInfo] = Field(
        validation_alias="lastUpdatedBy", default=None
    )

    labels: Optional[List[str]] = Field(validation_alias="labels", default=None)
