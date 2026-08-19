# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field


class GetResultsForTestsRequest(BaseModel):
    """
    GetResultsForTestsRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    ids: List[str] = Field(validation_alias="ids")

    startTime: str = Field(validation_alias="startTime")

    endTime: str = Field(validation_alias="endTime")

    agentIds: Optional[List[str]] = Field(validation_alias="agentIds", default=None)

    targets: Optional[List[str]] = Field(validation_alias="targets", default=None)

    aggregate: Optional[bool] = Field(validation_alias="aggregate", default=None)
