from typing import List, Optional

from pydantic import BaseModel, Field

from .SrcGroupBy import SrcGroupBy


class GroupedAlertSetting(BaseModel):
    """
    GroupedAlertSetting model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    metric: Optional[str] = Field(validation_alias="metric", default=None)

    srcGroupBy: Optional[SrcGroupBy] = Field(
        validation_alias="srcGroupBy", default=None
    )

    percentOfSrcGroup: Optional[int] = Field(
        validation_alias="percentOfSrcGroup", default=None
    )

    filterIds: Optional[List[int]] = Field(validation_alias="filterIds", default=None)
