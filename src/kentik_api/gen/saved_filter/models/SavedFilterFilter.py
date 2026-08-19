# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .FilterField import FilterField
from .FilterOperator import FilterOperator


class SavedFilterFilter(BaseModel):
    """
    SavedFilterFilter model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    filterField: Optional[FilterField] = Field(
        validation_alias="filterField", default=None
    )

    operator: Optional[FilterOperator] = Field(
        validation_alias="operator", default=None
    )

    filterValue: Optional[str] = Field(validation_alias="filterValue", default=None)

    filterFieldString: Optional[str] = Field(
        validation_alias="filterFieldString", default=None
    )

    metric: Optional[str] = Field(validation_alias="metric", default=None)

    aggregate: Optional[str] = Field(validation_alias="aggregate", default=None)

    rightFilterField: Optional[str] = Field(
        validation_alias="rightFilterField", default=None
    )
