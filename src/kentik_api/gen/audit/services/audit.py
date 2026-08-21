from typing import Union, cast, Optional
from kentik_api.gen.audit import models as rest_models
import kentik_api.gen.audit.services.AuditService as RestAuditModule1
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


class AuditServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.audit.pb.audit_pb2 as _pb2_1_mod
                import kentik_api.gen.audit.pb.audit_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.AuditServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_audit_events(
        self,
        *,
        startTime: Optional[str] = None,
        endTime: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> rest_models.ListAuditEventsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for audit service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "startTime": startTime,
                        "endTime": endTime,
                        "offset": offset,
                        "limit": limit,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.ListAuditEventsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ListAuditEvents, _req)
            return rest_models.ListAuditEventsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAuditModule1.ListAuditEvents(
                api_config_override=rest_transport.api_config,
                startTime=startTime,
                endTime=endTime,
                offset=offset,
                limit=limit,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_audit_event(
        self, *, id: str, ctime: Optional[str] = None
    ) -> rest_models.GetAuditEventResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for audit service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id, "ctime": ctime}.items() if v is not None},
                self._grpc_pb2_1.GetAuditEventRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetAuditEvent, _req)
            return rest_models.GetAuditEventResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAuditModule1.GetAuditEvent(
                api_config_override=rest_transport.api_config, id=id, ctime=ctime
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_audit_event_2(
        self, *, id: str, ctime: str
    ) -> rest_models.GetAuditEventResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetAuditEvent_2 is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAuditModule1.GetAuditEvent_2(
                api_config_override=rest_transport.api_config, id=id, ctime=ctime
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
