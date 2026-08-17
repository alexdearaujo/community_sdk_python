from typing import Optional

from pydantic import BaseModel, Field

from .DNSResponseData import DNSResponseData
from .MetricData import MetricData


class DNSResults(BaseModel):
    """
    DNSResults model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    target: Optional[str] = Field(validation_alias="target", default=None)

    server: Optional[str] = Field(validation_alias="server", default=None)

    latency: Optional[MetricData] = Field(validation_alias="latency", default=None)

    response: Optional[DNSResponseData] = Field(
        validation_alias="response", default=None
    )
