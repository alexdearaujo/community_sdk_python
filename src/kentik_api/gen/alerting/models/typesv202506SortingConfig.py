from typing import List, Optional

from pydantic import BaseModel, Field

from .SortingConfigField import SortingConfigField


class typesv202506SortingConfig(BaseModel):
    """
    typesv202506SortingConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    fields: Optional[List[Optional[SortingConfigField]]] = Field(
        validation_alias="fields", default=None
    )
