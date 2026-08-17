import grpc

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.transports.base import BaseTransport


class GrpcTransport(BaseTransport):
    def __init__(
        self, credentials: KentikCredentials, target: str = "grpc.api.kentik.com:443"
    ):
        auth_plugin = credentials.get_grpc_plugin()
        call_creds = grpc.metadata_call_credentials(auth_plugin)
        channel_creds = grpc.ssl_channel_credentials()
        composite_creds = grpc.composite_channel_credentials(channel_creds, call_creds)

        self.channel = grpc.secure_channel(target, composite_creds)

    def close(self):
        self.channel.close()
