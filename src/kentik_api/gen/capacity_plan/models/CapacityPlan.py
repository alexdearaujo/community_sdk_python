from typing import List, Optional

from pydantic import BaseModel, Field

from .CapacityPlanInterfaceDetail import CapacityPlanInterfaceDetail
from .Config import Config
from .SummaryStatus import SummaryStatus


class CapacityPlan(BaseModel):
    """
    CapacityPlan model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    status: Optional[str] = Field(validation_alias="status", default=None)

    interfaces: Optional[List[Optional[CapacityPlanInterfaceDetail]]] = Field(
        validation_alias="interfaces", default=None
    )

    config: Optional[Config] = Field(validation_alias="config", default=None)

    summaryStatus: Optional[SummaryStatus] = Field(
        validation_alias="summaryStatus", default=None
    )
