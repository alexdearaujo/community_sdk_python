from typing import Optional

from pydantic import BaseModel, Field


class Comment(BaseModel):
    """
    Comment model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    text: Optional[str] = Field(validation_alias="text", default=None)

    userId: Optional[str] = Field(validation_alias="userId", default=None)

    userName: Optional[str] = Field(validation_alias="userName", default=None)

    userFullName: Optional[str] = Field(validation_alias="userFullName", default=None)

    userEmail: Optional[str] = Field(validation_alias="userEmail", default=None)

    createdAt: Optional[str] = Field(validation_alias="createdAt", default=None)
