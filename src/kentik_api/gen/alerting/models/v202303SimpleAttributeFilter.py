from typing import Optional

from pydantic import BaseModel, Field

from .v202303SimpleAttributeFilterStringArray import (
    v202303SimpleAttributeFilterStringArray,
)


class v202303SimpleAttributeFilter(BaseModel):
    """
    v202303SimpleAttributeFilter model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    equals: Optional[str] = Field(validation_alias="equals", default=None)

    startsWith: Optional[str] = Field(validation_alias="startsWith", default=None)

    endsWith: Optional[str] = Field(validation_alias="endsWith", default=None)

    contains: Optional[str] = Field(validation_alias="contains", default=None)

    in_: Optional[v202303SimpleAttributeFilterStringArray] = Field(
        validation_alias="in", default=None
    )

    any: Optional[bool] = Field(validation_alias="any", default=None)
