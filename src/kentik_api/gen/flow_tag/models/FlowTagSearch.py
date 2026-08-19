# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .LookupField import LookupField
from .OrderField import OrderField


class FlowTagSearch(BaseModel):
    """
    FlowTagSearch model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    limit: Optional[int] = Field(validation_alias="limit", default=None)

    offset: Optional[int] = Field(validation_alias="offset", default=None)

    lookupFields: Optional[List[Optional[LookupField]]] = Field(
        validation_alias="lookupFields", default=None
    )

    lookupValues: Optional[List[str]] = Field(
        validation_alias="lookupValues", default=None
    )

    orderBy: Optional[List[Optional[OrderField]]] = Field(
        validation_alias="orderBy", default=None
    )

    fieldLimit: Optional[int] = Field(validation_alias="fieldLimit", default=None)
