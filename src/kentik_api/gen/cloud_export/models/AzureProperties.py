# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class AzureProperties(BaseModel):
    """
    AzureProperties model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    location: str = Field(validation_alias="location")

    resourceGroup: str = Field(validation_alias="resourceGroup")

    storageAccount: str = Field(validation_alias="storageAccount")

    subscriptionId: str = Field(validation_alias="subscriptionId")

    securityPrincipalEnabled: Optional[bool] = Field(
        validation_alias="securityPrincipalEnabled", default=None
    )
