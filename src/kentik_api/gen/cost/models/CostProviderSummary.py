from typing import Optional

from pydantic import BaseModel, Field

from .costv202308Status import costv202308Status


class CostProviderSummary(BaseModel):
    """
    CostProviderSummary model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    date: Optional[str] = Field(validation_alias="date", default=None)

    status: Optional[costv202308Status] = Field(validation_alias="status", default=None)

    totalCost: Optional[float] = Field(validation_alias="totalCost", default=None)

    totalCostVariation: Optional[str] = Field(
        validation_alias="totalCostVariation", default=None
    )

    totalCostGroupAdditionalCost: Optional[float] = Field(
        validation_alias="totalCostGroupAdditionalCost", default=None
    )

    totalCostGroupAdditionalInterfaceCost: Optional[float] = Field(
        validation_alias="totalCostGroupAdditionalInterfaceCost", default=None
    )

    currency: Optional[str] = Field(validation_alias="currency", default=None)

    costPerMbps: Optional[float] = Field(validation_alias="costPerMbps", default=None)

    costPerMbpsVariation: Optional[str] = Field(
        validation_alias="costPerMbpsVariation", default=None
    )

    providerName: Optional[str] = Field(validation_alias="providerName", default=None)

    costGroupName: Optional[str] = Field(validation_alias="costGroupName", default=None)

    costGroupConnType: Optional[str] = Field(
        validation_alias="costGroupConnType", default=None
    )

    siteName: Optional[str] = Field(validation_alias="siteName", default=None)

    siteMarket: Optional[str] = Field(validation_alias="siteMarket", default=None)

    ingressTrafficMbps: Optional[float] = Field(
        validation_alias="ingressTrafficMbps", default=None
    )

    ingressTrafficVariation: Optional[str] = Field(
        validation_alias="ingressTrafficVariation", default=None
    )

    egressTrafficMbps: Optional[float] = Field(
        validation_alias="egressTrafficMbps", default=None
    )

    egressTrafficVariation: Optional[str] = Field(
        validation_alias="egressTrafficVariation", default=None
    )
