from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class PageLoadTest(BaseModel):
    """
    PageLoadTest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    target: Optional[str] = Field(validation_alias="target", default=None)

    timeout: Optional[int] = Field(validation_alias="timeout", default=None)

    headers: Optional[Dict[str, Any]] = Field(validation_alias="headers", default=None)

    ignoreTlsErrors: Optional[bool] = Field(
        validation_alias="ignoreTlsErrors", default=None
    )

    cssSelectors: Optional[Dict[str, Any]] = Field(
        validation_alias="cssSelectors", default=None
    )
