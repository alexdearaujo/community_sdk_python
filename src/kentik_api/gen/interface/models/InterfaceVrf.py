# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field


class InterfaceVrf(BaseModel):
    """
    InterfaceVrf model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    routeDistinguisher: Optional[str] = Field(
        validation_alias="routeDistinguisher", default=None
    )

    extRouteDistinguisher: Optional[str] = Field(
        validation_alias="extRouteDistinguisher", default=None
    )

    routeTarget: Optional[str] = Field(validation_alias="routeTarget", default=None)

    routeTargets: Optional[List[str]] = Field(
        validation_alias="routeTargets", default=None
    )
