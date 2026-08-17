from typing import List, Optional

from pydantic import BaseModel, Field


class AddressInfo(BaseModel):
    """
    AddressInfo model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    addresses: Optional[List[str]] = Field(validation_alias="addresses", default=None)

    totalCount: Optional[int] = Field(validation_alias="totalCount", default=None)
