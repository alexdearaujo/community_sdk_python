# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .HTTPResponseData import HTTPResponseData
from .MetricData import MetricData


class HTTPResults(BaseModel):
    """
    HTTPResults model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    target: Optional[str] = Field(validation_alias="target", default=None)

    latency: Optional[MetricData] = Field(validation_alias="latency", default=None)

    response: Optional[HTTPResponseData] = Field(
        validation_alias="response", default=None
    )

    dstIp: Optional[str] = Field(validation_alias="dstIp", default=None)
