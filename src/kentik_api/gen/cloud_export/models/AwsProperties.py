# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field


class AwsProperties(BaseModel):
    """
    AwsProperties model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    iamRoleArn: str = Field(validation_alias="iamRoleArn")

    region: str = Field(validation_alias="region")

    metadataOnly: Optional[bool] = Field(validation_alias="metadataOnly", default=None)

    collectFlowLogs: Optional[bool] = Field(
        validation_alias="collectFlowLogs", default=None
    )

    collectFirewallLogs: Optional[bool] = Field(
        validation_alias="collectFirewallLogs", default=None
    )

    collectMetrics: Optional[bool] = Field(
        validation_alias="collectMetrics", default=None
    )

    bucket: Optional[str] = Field(validation_alias="bucket", default=None)

    bucketPrefix: Optional[str] = Field(validation_alias="bucketPrefix", default=None)

    deleteAfterRead: Optional[bool] = Field(
        validation_alias="deleteAfterRead", default=None
    )

    awsIamRoleArnIsOrg: Optional[bool] = Field(
        validation_alias="awsIamRoleArnIsOrg", default=None
    )

    secondaryAwsAccounts: Optional[List[str]] = Field(
        validation_alias="secondaryAwsAccounts", default=None
    )

    secondaryAwsBlockedAccounts: Optional[List[str]] = Field(
        validation_alias="secondaryAwsBlockedAccounts", default=None
    )

    secondaryAwsRegions: Optional[List[str]] = Field(
        validation_alias="secondaryAwsRegions", default=None
    )

    secondaryAwsSuffix: Optional[str] = Field(
        validation_alias="secondaryAwsSuffix", default=None
    )
