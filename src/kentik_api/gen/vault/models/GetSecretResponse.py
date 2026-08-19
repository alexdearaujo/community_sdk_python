# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field

from .Secret import Secret


class GetSecretResponse(BaseModel):
    """
    GetSecretResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    secret: Secret = Field(validation_alias="secret")
