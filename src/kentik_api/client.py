import os

from dotenv import find_dotenv, load_dotenv

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.client_mixin import KentikClientMixin
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class KentikAPI(KentikClientMixin):
    def __init__(
        self,
        email: str | None = None,
        api_token: str | None = None,
        protocol: str = "grpc",
        region: str = "us",
    ):
        # Load from the nearest .env based on current working directory.
        dotenv_path = find_dotenv(filename=".env", usecwd=True)
        if dotenv_path:
            load_dotenv(dotenv_path=dotenv_path, override=False)

        email = email or os.getenv("KENTIK_EMAIL")
        api_token = api_token or os.getenv("KENTIK_API_TOKEN")

        if not email or not api_token:
            raise ValueError(
                "Missing Kentik credentials. Provide email/api_token explicitly or set "
                "KENTIK_EMAIL and KENTIK_API_TOKEN in a .env file at the project root."
            )

        self.credentials = KentikCredentials(email, api_token)

        region = region.lower()
        if region == "us":
            grpc_target = "grpc.api.kentik.com:443"
            rest_base_url = "https://grpc.api.kentik.com"
        elif region == "eu":
            grpc_target = "grpc.api.kentik.eu:443"
            rest_base_url = "https://grpc.api.kentik.eu"
        else:
            raise ValueError(f"Invalid region '{region}'. Must be 'us' or 'eu'.")

        if protocol.lower() == "grpc":
            self._transport = GrpcTransport(self.credentials, target=grpc_target)
        elif protocol.lower() == "rest":
            self._transport = RestTransport(self.credentials, base_url=rest_base_url)
        else:
            raise ValueError("Protocol must be 'grpc' or 'rest'")

        self._mount_generated_services()

    def close(self):
        self._transport.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
