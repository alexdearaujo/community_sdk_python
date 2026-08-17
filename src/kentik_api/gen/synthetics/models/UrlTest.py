from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class UrlTest(BaseModel):
    """
    UrlTest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    target: Optional[str] = Field(validation_alias="target", default=None)

    timeout: Optional[int] = Field(validation_alias="timeout", default=None)

    method: Optional[str] = Field(validation_alias="method", default=None)

    headers: Optional[Dict[str, Any]] = Field(validation_alias="headers", default=None)

    body: Optional[str] = Field(validation_alias="body", default=None)

    ignoreTlsErrors: Optional[bool] = Field(
        validation_alias="ignoreTlsErrors", default=None
    )
