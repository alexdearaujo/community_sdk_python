# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from kentik_api.auth.credentials import KentikCredentials
from kentik_api.core.api_config import APIConfig
from kentik_api.transports.base import BaseTransport


class RestTransport(BaseTransport):
    api_config: APIConfig

    def __init__(
        self,
        credentials: KentikCredentials,
        base_url: str = "https://grpc.api.kentik.com",
        api_config: APIConfig | None = None,
    ):
        self.api_config = api_config or APIConfig(
            base_path=base_url,
            auth_email=credentials.email,
            auth_token=credentials.api_token,
            verify=True,
        )

    def close(self):
        self.api_config.close()
