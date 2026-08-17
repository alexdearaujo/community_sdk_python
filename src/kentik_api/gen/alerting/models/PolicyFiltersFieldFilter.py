from typing import Optional

from pydantic import BaseModel, Field

from .PolicyFiltersOperator import PolicyFiltersOperator


class PolicyFiltersFieldFilter(BaseModel):
    """
    PolicyFiltersFieldFilter model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    field: Optional[str] = Field(validation_alias="field", default=None)

    operator: Optional[PolicyFiltersOperator] = Field(
        validation_alias="operator", default=None
    )

    value: Optional[str] = Field(validation_alias="value", default=None)
