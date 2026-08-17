from typing import List, Optional

from pydantic import BaseModel, Field

from .Layer import Layer


class LayerSet(BaseModel):
    """
    LayerSet model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    layers: Optional[List[Optional[Layer]]] = Field(
        validation_alias="layers", default=None
    )
