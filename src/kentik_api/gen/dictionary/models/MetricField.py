# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from .BaseUnit import BaseUnit
from .FieldDataType import FieldDataType
from .FieldDirection import FieldDirection


class MetricField(BaseModel):
    """
    MetricField model
    A field that represents a measurable metric in a query.
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

    windowFn: Optional[str] = Field(validation_alias="windowFn", default=None)

    aggregateFn: Optional[str] = Field(validation_alias="aggregateFn", default=None)

    expression: Optional[str] = Field(validation_alias="expression", default=None)

    dependsOn: Optional[List[str]] = Field(validation_alias="dependsOn", default=None)

    toBits: Optional[bool] = Field(validation_alias="toBits", default=None)

    rollup: Optional[bool] = Field(validation_alias="rollup", default=None)

    healthyValue: Optional[str] = Field(validation_alias="healthyValue", default=None)

    familyKey: Optional[str] = Field(validation_alias="familyKey", default=None)

    baseUnit: Optional[BaseUnit] = Field(validation_alias="baseUnit", default=None)
