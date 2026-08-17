from typing import List, Optional

from pydantic import BaseModel, Field


class IpTest(BaseModel):
    """
    IpTest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    targets: Optional[List[str]] = Field(validation_alias="targets", default=None)

    useLocalIp: Optional[bool] = Field(validation_alias="useLocalIp", default=None)
