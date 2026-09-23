# HAND-WRITTEN: not modified by `make generate`. Edit directly.
import grpc

# The one definition of Kentik's auth scheme. REST sends these as headers and
# gRPC as call metadata, lowercased because gRPC requires lowercase keys.
AUTH_EMAIL_KEY = "X-CH-Auth-Email"
AUTH_TOKEN_KEY = "X-CH-Auth-API-Token"


def auth_headers(email: str | None, api_token: str | None) -> dict[str, str | None]:
    """The auth headers for one credential pair, as REST sends them."""
    return {AUTH_EMAIL_KEY: email, AUTH_TOKEN_KEY: api_token}


class _KentikAuthPlugin(grpc.AuthMetadataPlugin):
    def __init__(self, email: str, api_token: str) -> None:
        self._metadata = tuple(
            (key.lower(), value)
            for key, value in auth_headers(email, api_token).items()
        )

    def __call__(self, context, callback):
        callback(self._metadata, None)


class KentikCredentials:
    """Unified credentials for both REST and gRPC."""

    def __init__(self, email: str, api_token: str):
        self.email = email
        self.api_token = api_token

    def get_grpc_plugin(self) -> grpc.AuthMetadataPlugin:
        """Returns the auth plugin required for the gRPC channel."""
        return _KentikAuthPlugin(self.email, self.api_token)
