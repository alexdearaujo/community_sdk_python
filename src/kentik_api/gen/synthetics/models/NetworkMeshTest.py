# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class NetworkMeshTest(BaseModel):
    """
    NetworkMeshTest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    useLocalIp: Optional[bool] = Field(validation_alias="useLocalIp", default=None)
