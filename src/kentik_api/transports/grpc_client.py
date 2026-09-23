# HAND-WRITTEN: not modified by `make generate`. Edit directly.
import collections

import grpc

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.core.api_config import APIConfig
from kentik_api.transports.base import BaseTransport


class _CallDetails(
    collections.namedtuple(
        "_CallDetails",
        (
            "method",
            "timeout",
            "metadata",
            "credentials",
            "wait_for_ready",
            "compression",
        ),
    ),
    grpc.ClientCallDetails,
):
    """grpc.ClientCallDetails is abstract; interceptors must supply their own."""


class _DefaultDeadlineInterceptor(grpc.UnaryUnaryClientInterceptor):
    """Bounds every call on the channel without touching generated call sites.

    Generated wrappers call stubs with no timeout, and gRPC's default is to
    wait forever. A deadline the call already carries is left alone, so a
    per-call override takes precedence over the client-wide default.
    """

    def __init__(self, api_config: APIConfig) -> None:
        self._api_config = api_config

    def intercept_unary_unary(self, continuation, client_call_details, request):
        if client_call_details.timeout is None:
            client_call_details = _CallDetails(
                method=client_call_details.method,
                # Read per call, so the deadline follows the client's current config.
                timeout=self._api_config.grpc_deadline,
                metadata=client_call_details.metadata,
                credentials=client_call_details.credentials,
                wait_for_ready=client_call_details.wait_for_ready,
                compression=client_call_details.compression,
            )
        return continuation(client_call_details, request)


class GrpcTransport(BaseTransport):
    channel: grpc.Channel  # set by __init__; declared here so mock spec includes it
    api_config: APIConfig

    def __init__(
        self,
        credentials: KentikCredentials,
        target: str = "grpc.api.kentik.com:443",
        api_config: APIConfig | None = None,
    ):
        self.api_config = api_config or APIConfig(
            auth_email=credentials.email,
            auth_token=credentials.api_token,
        )

        auth_plugin = credentials.get_grpc_plugin()
        call_creds = grpc.metadata_call_credentials(auth_plugin)
        channel_creds = grpc.ssl_channel_credentials()
        composite_creds = grpc.composite_channel_credentials(channel_creds, call_creds)

        self.channel = grpc.intercept_channel(
            grpc.secure_channel(target, composite_creds),
            _DefaultDeadlineInterceptor(self.api_config),
        )

    def close(self):
        self.channel.close()
