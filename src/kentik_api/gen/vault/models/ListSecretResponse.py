from typing import List, Optional

from pydantic import BaseModel, Field

from .Secret import Secret


class ListSecretResponse(BaseModel):
    """
    ListSecretResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    secrets: List[Secret] = Field(validation_alias="secrets")

    invalidCredentialCount: Optional[int] = Field(
        validation_alias="invalidCredentialCount", default=None
    )
