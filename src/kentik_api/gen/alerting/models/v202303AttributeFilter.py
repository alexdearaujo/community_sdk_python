from typing import Optional

from pydantic import BaseModel, Field

from .v202303AttributeFilterStringArray import v202303AttributeFilterStringArray


class v202303AttributeFilter(BaseModel):
    """
    v202303AttributeFilter model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    not_: Optional[bool] = Field(validation_alias="not", default=None)

    empty: Optional[bool] = Field(validation_alias="empty", default=None)

    equals: Optional[str] = Field(validation_alias="equals", default=None)

    startsWith: Optional[str] = Field(validation_alias="startsWith", default=None)

    endsWith: Optional[str] = Field(validation_alias="endsWith", default=None)

    contains: Optional[str] = Field(validation_alias="contains", default=None)

    in_: Optional[v202303AttributeFilterStringArray] = Field(
        validation_alias="in", default=None
    )

    any: Optional[bool] = Field(validation_alias="any", default=None)
