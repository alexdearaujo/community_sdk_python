from typing import Optional

from pydantic import BaseModel, Field

from .CustomApplication import CustomApplication


class UpdateCustomApplicationResponse(BaseModel):
    """
    UpdateCustomApplicationResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    application: Optional[CustomApplication] = Field(
        validation_alias="application", default=None
    )
