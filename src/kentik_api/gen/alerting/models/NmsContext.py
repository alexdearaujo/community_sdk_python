# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field

from .NmsContextActivationInfo import NmsContextActivationInfo
from .NmsContextDatasetInfo import NmsContextDatasetInfo


class NmsContext(BaseModel):
    """
    in the comments are evm equivalents model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    activationInfo: Optional[NmsContextActivationInfo] = Field(
        validation_alias="activationInfo", default=None
    )

    datasetInfo: Optional[NmsContextDatasetInfo] = Field(
        validation_alias="datasetInfo", default=None
    )

    targets: Optional[Dict[str, Any]] = Field(validation_alias="targets", default=None)

    metricValues: Optional[Dict[str, Any]] = Field(
        validation_alias="metricValues", default=None
    )

    previousMetricValues: Optional[Dict[str, Any]] = Field(
        validation_alias="previousMetricValues", default=None
    )

    device: Optional[Dict[str, Any]] = Field(validation_alias="device", default=None)

    groupKey: Optional[Dict[str, Any]] = Field(
        validation_alias="groupKey", default=None
    )
