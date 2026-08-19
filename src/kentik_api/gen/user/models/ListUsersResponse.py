# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .User import User


class ListUsersResponse(BaseModel):
    """
    ListUsersResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    users: Optional[List[Optional[User]]] = Field(
        validation_alias="users", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
