from typing import Union, cast

import kentik_api.gen.dictionary.services.DictionaryService as RestDictionaryModule1
from kentik_api.gen.dictionary import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class DictionaryServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def get_dictionary(
        self,
    ) -> rest_models.GetDictionaryResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetDictionary is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDictionaryModule1.GetDictionary(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
