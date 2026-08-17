import grpc


class KentikCredentials:
    """Unified credentials for both REST and gRPC."""

    def __init__(self, email: str, api_token: str):
        self.email = email
        self.api_token = api_token

    def get_rest_headers(self) -> dict:
        """Returns standard HTTP headers for OpenAPI/REST."""
        return {
            "X-CH-Auth-Email": self.email,
            "X-CH-Auth-API-Token": self.api_token,
            "Content-Type": "application/json",
        }

    def get_grpc_plugin(self) -> grpc.AuthMetadataPlugin:
        """Returns the auth plugin required for the gRPC channel."""

        # We define the plugin class and give it its own __init__
        class KentikPlugin(grpc.AuthMetadataPlugin):
            def __init__(self, plugin_email: str, plugin_token: str):
                self._email = plugin_email
                self._token = plugin_token

            def __call__(self, context, callback):
                metadata = (
                    ("x-ch-auth-email", self._email),
                    ("x-ch-auth-api-token", self._token),
                )
                callback(metadata, None)

        # Instantiate the plugin with the outer class's credentials
        return KentikPlugin(self.email, self.api_token)
