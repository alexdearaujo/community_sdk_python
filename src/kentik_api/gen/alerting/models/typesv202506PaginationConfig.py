# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class typesv202506PaginationConfig(BaseModel):
    """
    typesv202506PaginationConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    limit: Optional[str] = Field(validation_alias="limit", default=None)

    offset: Optional[str] = Field(validation_alias="offset", default=None)

    includeTotalCount: Optional[bool] = Field(
        validation_alias="includeTotalCount", default=None
    )
