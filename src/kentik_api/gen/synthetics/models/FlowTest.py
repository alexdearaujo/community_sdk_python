from typing import Optional

from pydantic import BaseModel, Field


class FlowTest(BaseModel):
    """
    FlowTest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    target: Optional[str] = Field(validation_alias="target", default=None)

    targetRefreshIntervalMillis: Optional[int] = Field(
        validation_alias="targetRefreshIntervalMillis", default=None
    )

    maxProviders: Optional[int] = Field(validation_alias="maxProviders", default=None)

    maxIpTargets: Optional[int] = Field(validation_alias="maxIpTargets", default=None)

    type: Optional[str] = Field(validation_alias="type", default=None)

    inetDirection: Optional[str] = Field(validation_alias="inetDirection", default=None)

    direction: Optional[str] = Field(validation_alias="direction", default=None)
