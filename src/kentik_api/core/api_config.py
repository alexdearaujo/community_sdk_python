# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from typing import TYPE_CHECKING, Optional

from kentik_api.errors import HTTPException

if TYPE_CHECKING:
    import httpx

__all__ = ["APIConfig", "HTTPException"]


class APIConfig:
    """Centralized API Configuration for all generated REST services."""

    def __init__(
        self,
        base_path: str = "https://grpc.api.kentik.com",
        auth_email: Optional[str] = None,
        auth_token: Optional[str] = None,
        verify: bool = True,
        http_client: "Optional[httpx.Client]" = None,
    ):
        self.base_path = base_path
        self.auth_email = auth_email
        self.auth_token = auth_token
        self.verify = verify
        # Shared HTTPX client for connection pooling; None means create-per-call.
        self.http_client = http_client
