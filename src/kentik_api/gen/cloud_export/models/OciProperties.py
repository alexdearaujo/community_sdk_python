from typing import List, Optional

from pydantic import BaseModel, Field


class OciProperties(BaseModel):
    """
    OciProperties model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    ociUserId: Optional[str] = Field(validation_alias="ociUserId", default=None)

    ociTenancyId: str = Field(validation_alias="ociTenancyId")

    ociCompartmentId: Optional[List[str]] = Field(
        validation_alias="ociCompartmentId", default=None
    )

    ociDefaultRegion: str = Field(validation_alias="ociDefaultRegion")

    ociCollectFlowLogs: Optional[bool] = Field(
        validation_alias="ociCollectFlowLogs", default=None
    )

    ociBucketName: Optional[str] = Field(validation_alias="ociBucketName", default=None)

    ociBucketNamespaceName: Optional[str] = Field(
        validation_alias="ociBucketNamespaceName", default=None
    )

    ociServiceConnectorOcid: Optional[str] = Field(
        validation_alias="ociServiceConnectorOcid", default=None
    )

    ociFlowObjectNamePrefix: Optional[str] = Field(
        validation_alias="ociFlowObjectNamePrefix", default=None
    )

    metadataOnly: Optional[bool] = Field(validation_alias="metadataOnly", default=None)
