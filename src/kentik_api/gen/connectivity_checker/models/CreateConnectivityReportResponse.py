# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field


class CreateConnectivityReportResponse(BaseModel):
    """
    CreateConnectivityReportResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    reachable: Optional[bool] = Field(validation_alias="reachable", default=None)

    returnReachable: Optional[bool] = Field(
        validation_alias="returnReachable", default=None
    )

    queryStatus: Optional[str] = Field(validation_alias="queryStatus", default=None)

    reportUrl: Optional[str] = Field(validation_alias="reportUrl", default=None)

    paths: Optional[List[str]] = Field(validation_alias="paths", default=None)

    returnPaths: Optional[List[str]] = Field(
        validation_alias="returnPaths", default=None
    )

    lastMetadataFetch: Optional[str] = Field(
        validation_alias="lastMetadataFetch", default=None
    )
