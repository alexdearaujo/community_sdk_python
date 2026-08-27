from typing import Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.connectivity_checker.services.ConnectivityCheckerAdminService as RestConnectivityCheckerModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.connectivity_checker import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class ConnectivityCheckerServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.connectivity_checker.pb.connectivity_checker_pb2 as _pb2_1_mod
                import kentik_api.gen.connectivity_checker.pb.connectivity_checker_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.ConnectivityCheckerAdminServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def create_connectivity_report(
        self, *, data: rest_models.CreateConnectivityReportRequest
    ) -> rest_models.CreateConnectivityReportResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for connectivity_checker service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateConnectivityReportRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateConnectivityReport, _req)
            return rest_models.CreateConnectivityReportResponse.model_validate(
                MessageToDict(_resp, always_print_fields_with_no_presence=True)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestConnectivityCheckerModule1.CreateConnectivityReport(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
