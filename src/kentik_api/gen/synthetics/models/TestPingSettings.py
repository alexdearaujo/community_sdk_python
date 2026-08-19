# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class TestPingSettings(BaseModel):
    """
    TestPingSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    count: Optional[int] = Field(validation_alias="count", default=None)

    protocol: Optional[str] = Field(validation_alias="protocol", default=None)

    port: Optional[int] = Field(validation_alias="port", default=None)

    timeout: Optional[int] = Field(validation_alias="timeout", default=None)

    delay: Optional[float] = Field(validation_alias="delay", default=None)

    dscp: Optional[int] = Field(validation_alias="dscp", default=None)
