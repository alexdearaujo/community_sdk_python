from typing import Optional

from pydantic import BaseModel, Field


class FlowspecActionTrafficRateBytes(BaseModel):
    """
        FlowspecActionTrafficRateBytes model
            FlowspecActionTrafficRateBytes specifies the maximum traffic rate
    in bytes per second.

    Extended Community type and sub-type: 0x8006
    https://datatracker.ietf.org/doc/html/rfc8955#traffic_rate_in_bytes
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    bytesPerSecond: Optional[float] = Field(
        validation_alias="bytesPerSecond", default=None
    )
