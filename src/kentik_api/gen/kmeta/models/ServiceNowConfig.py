# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class ServiceNowConfig(BaseModel):
    """
    ServiceNowConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)

    name: str = Field(validation_alias="name")

    description: Optional[str] = Field(validation_alias="description", default=None)

    deviceStagingTableName: Optional[str] = Field(
        validation_alias="deviceStagingTableName", default=None
    )

    pushFrequencySeconds: Optional[int] = Field(
        validation_alias="pushFrequencySeconds", default=None
    )

    proxyAgentId: Optional[str] = Field(validation_alias="proxyAgentId", default=None)

    credentialVaultName: Optional[str] = Field(
        validation_alias="credentialVaultName", default=None
    )

    enabled: Optional[bool] = Field(validation_alias="enabled", default=None)

    apiUrl: str = Field(validation_alias="apiUrl")
