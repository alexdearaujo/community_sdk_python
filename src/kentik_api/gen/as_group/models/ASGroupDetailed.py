from typing import List, Optional

from pydantic import BaseModel, Field

from .AutonomousSystem import AutonomousSystem


class ASGroupDetailed(BaseModel):
    """
    ASGroupDetailed model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: str = Field(validation_alias="name")

    asn: Optional[List[Optional[AutonomousSystem]]] = Field(
        validation_alias="asn", default=None
    )

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)
