# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class typesv202506PaginationConfig(BaseModel):
    """
    typesv202506PaginationConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    limit: Optional[str] = Field(
        validation_alias="limit",
        default=None,
        description="limit is how many items to return at most",
    )

    offset: Optional[str] = Field(
        validation_alias="offset",
        default=None,
        description="offset is the offset into the list of items",
    )

    includeTotalCount: Optional[bool] = Field(
        validation_alias="includeTotalCount",
        default=None,
        description="include_total_count is a flag to enforce API service to include the total count of items in the response,\nwhich in some cases may be very expensive to fetch",
    )
