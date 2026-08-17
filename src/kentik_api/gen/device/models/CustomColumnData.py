from typing import Optional

from pydantic import BaseModel, Field


class CustomColumnData(BaseModel):
    """
    CustomColumnData model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    deviceId: Optional[str] = Field(validation_alias="deviceId", default=None)

    fieldId: Optional[str] = Field(validation_alias="fieldId", default=None)

    colName: Optional[str] = Field(validation_alias="colName", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    colType: Optional[str] = Field(validation_alias="colType", default=None)

    deviceType: Optional[str] = Field(validation_alias="deviceType", default=None)
