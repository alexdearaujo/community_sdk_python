from typing import Optional

from pydantic import BaseModel, Field

from .v202303AttributeFilter import v202303AttributeFilter
from .v202303SimpleAttributeFilter import v202303SimpleAttributeFilter


class v202303KeyValueFilter(BaseModel):
    """
    v202303KeyValueFilter model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    key: Optional[v202303SimpleAttributeFilter] = Field(
        validation_alias="key", default=None
    )

    value: Optional[v202303AttributeFilter] = Field(
        validation_alias="value", default=None
    )
