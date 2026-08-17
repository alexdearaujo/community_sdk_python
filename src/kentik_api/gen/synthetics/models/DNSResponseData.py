from typing import Optional

from pydantic import BaseModel, Field


class DNSResponseData(BaseModel):
    """
    DNSResponseData model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    status: Optional[int] = Field(validation_alias="status", default=None)

    data: Optional[str] = Field(validation_alias="data", default=None)
