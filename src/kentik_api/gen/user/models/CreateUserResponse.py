from typing import Optional

from pydantic import BaseModel, Field

from .User import User


class CreateUserResponse(BaseModel):
    """
    CreateUserResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    user: Optional[User] = Field(validation_alias="user", default=None)
