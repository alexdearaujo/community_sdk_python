from typing import List, Optional

from pydantic import BaseModel, Field

from .Operator import Operator
from .OperatorSetKey import OperatorSetKey


class OperatorSet(BaseModel):
    """
    OperatorSet model
        A named group of operators applicable to a given data type.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    key: Optional[OperatorSetKey] = Field(validation_alias="key", default=None)

    operators: Optional[List[Optional[Operator]]] = Field(
        validation_alias="operators", default=None
    )
