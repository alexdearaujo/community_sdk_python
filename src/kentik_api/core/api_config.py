# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from typing import Optional

from kentik_api.errors import HTTPException

__all__ = ["APIConfig", "HTTPException"]


class APIConfig:
    """Centralized API Configuration for all generated REST services."""

    def __init__(
        self,
        base_path: str = "https://grpc.api.kentik.com",
        auth_email: Optional[str] = None,
        auth_token: Optional[str] = None,
        verify: bool = True,
    ):
        self.base_path = base_path
        self.auth_email = auth_email
        self.auth_token = auth_token
        self.verify = verify
