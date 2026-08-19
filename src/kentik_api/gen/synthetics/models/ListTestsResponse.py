# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .Test import Test


class ListTestsResponse(BaseModel):
    """
    ListTestsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tests: Optional[List[Optional[Test]]] = Field(
        validation_alias="tests", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
