from pydantic import BaseModel


class SetMonitorStatusResponse(BaseModel):
    """
    SetMonitorStatusResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
