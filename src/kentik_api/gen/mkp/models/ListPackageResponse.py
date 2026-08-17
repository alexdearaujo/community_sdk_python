from typing import List, Optional

from pydantic import BaseModel, Field

from .Package import Package


class ListPackageResponse(BaseModel):
    """
    ListPackageResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    packages: Optional[List[Optional[Package]]] = Field(
        validation_alias="packages", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
