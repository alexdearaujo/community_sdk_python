# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class Operator(BaseModel):
    """
    Operator model
    An individual filter operator (e.g. &#34;equals&#34;, &#34;contains&#34;).
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    key: Optional[str] = Field(validation_alias="key", default=None)

    label: Optional[str] = Field(validation_alias="label", default=None)
