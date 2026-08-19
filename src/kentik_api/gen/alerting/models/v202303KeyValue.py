# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class v202303KeyValue(BaseModel):
    """
    v202303KeyValue model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    value: Optional[Dict[str, Any]] = Field(validation_alias="value", default=None)
