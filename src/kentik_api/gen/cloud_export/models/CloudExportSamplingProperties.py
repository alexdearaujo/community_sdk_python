from typing import Optional

from pydantic import BaseModel, Field

from .CloudExportSamplingType import CloudExportSamplingType


class CloudExportSamplingProperties(BaseModel):
    """
    CloudExportSamplingProperties model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    samplingEnabled: Optional[bool] = Field(
        validation_alias="samplingEnabled", default=None
    )

    samplingType: Optional[CloudExportSamplingType] = Field(
        validation_alias="samplingType", default=None
    )

    samplingRate: Optional[int] = Field(validation_alias="samplingRate", default=None)
