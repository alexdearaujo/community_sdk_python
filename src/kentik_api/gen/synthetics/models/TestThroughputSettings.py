# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class TestThroughputSettings(BaseModel):
    """
    TestThroughputSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    port: Optional[int] = Field(validation_alias="port", default=None)

    omit: Optional[int] = Field(validation_alias="omit", default=None)

    duration: Optional[int] = Field(validation_alias="duration", default=None)

    bandwidth: Optional[int] = Field(validation_alias="bandwidth", default=None)

    protocol: Optional[str] = Field(validation_alias="protocol", default=None)
