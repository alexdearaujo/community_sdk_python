# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class typesv202506PaginationInfo(BaseModel):
    """
    typesv202506PaginationInfo model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    totalCount: Optional[str] = Field(validation_alias="totalCount", default=None)

    hasMoreResults: Optional[bool] = Field(
        validation_alias="hasMoreResults", default=None
    )
