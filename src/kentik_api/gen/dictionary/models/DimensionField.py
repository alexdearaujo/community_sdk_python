from typing import Any, Dict, Optional

from pydantic import BaseModel, Field

from .FieldDataType import FieldDataType
from .FieldDirection import FieldDirection
from .OperatorSetKey import OperatorSetKey


class DimensionField(BaseModel):
    """
    DimensionField model
    A field that can be used as a dimension/filter in a query.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    key: Optional[str] = Field(validation_alias="key", default=None)

    label: Optional[str] = Field(validation_alias="label", default=None)

    dataType: Optional[FieldDataType] = Field(validation_alias="dataType", default=None)

    category: Optional[str] = Field(validation_alias="category", default=None)

    column: Optional[str] = Field(validation_alias="column", default=None)

    direction: Optional[FieldDirection] = Field(
        validation_alias="direction", default=None
    )

    inverse: Optional[str] = Field(validation_alias="inverse", default=None)

    values: Optional[Dict[str, Any]] = Field(validation_alias="values", default=None)

    lastSeen: Optional[str] = Field(validation_alias="lastSeen", default=None)

    operatorSetKey: Optional[OperatorSetKey] = Field(
        validation_alias="operatorSetKey", default=None
    )

    filterOnly: Optional[bool] = Field(validation_alias="filterOnly", default=None)

    filterColumn: Optional[str] = Field(validation_alias="filterColumn", default=None)

    queryColumn: Optional[str] = Field(validation_alias="queryColumn", default=None)

    canCount: Optional[bool] = Field(validation_alias="canCount", default=None)
