# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .BaseUnit import BaseUnit
from .MetricQuantity import MetricQuantity


class MetricFamilyDef(BaseModel):
    """
    MetricFamilyDef model
    Definition of a metric family grouping related metrics by quantity and unit.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    key: Optional[str] = Field(validation_alias="key", default=None)

    label: Optional[str] = Field(validation_alias="label", default=None)

    quantity: Optional[MetricQuantity] = Field(
        validation_alias="quantity", default=None
    )

    baseUnit: Optional[BaseUnit] = Field(validation_alias="baseUnit", default=None)

    dualAxisCompatible: Optional[List[str]] = Field(
        validation_alias="dualAxisCompatible", default=None
    )

    incompatibleWith: Optional[List[str]] = Field(
        validation_alias="incompatibleWith", default=None
    )
