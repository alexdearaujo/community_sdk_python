from typing import List, Optional

from pydantic import BaseModel, Field


class ASGroupConcise(BaseModel):
    """
    ASGroupConcise model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: str = Field(validation_alias="name")

    asn: Optional[List[str]] = Field(validation_alias="asn", default=None)

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)
