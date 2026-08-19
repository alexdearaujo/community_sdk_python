# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .TraceHop import TraceHop


class PathTrace(BaseModel):
    """
    PathTrace model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asPath: Optional[List[int]] = Field(validation_alias="asPath", default=None)

    isComplete: Optional[bool] = Field(validation_alias="isComplete", default=None)

    hops: Optional[List[Optional[TraceHop]]] = Field(
        validation_alias="hops", default=None
    )
