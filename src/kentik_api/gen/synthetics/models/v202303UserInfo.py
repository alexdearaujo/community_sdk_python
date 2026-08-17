from typing import Optional

from pydantic import BaseModel, Field


class v202303UserInfo(BaseModel):
    """
    UserInfo model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    email: Optional[str] = Field(validation_alias="email", default=None)

    fullName: Optional[str] = Field(validation_alias="fullName", default=None)
