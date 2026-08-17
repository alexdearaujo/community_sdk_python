from pydantic import BaseModel, Field

from .TestStatus import TestStatus


class SyntheticsAdminServiceSetTestStatusBody(BaseModel):
    """
    SetTestStatusRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    status: TestStatus = Field(validation_alias="status")
