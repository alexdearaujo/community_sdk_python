from typing import Optional, Union, cast

import kentik_api.gen.audit.services.AuditService as RestAuditModule1
from kentik_api.gen.audit import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class AuditServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_audit_events(
        self,
        *,
        startTime: Optional[str] = None,
        endTime: Optional[str] = None,
        offset: Optional[str] = None,
        limit: Optional[str] = None,
    ) -> rest_models.ListAuditEventsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListAuditEvents is not yet implemented."
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
        self,
        *,
        id: str,
        ctime: Optional[str] = None,
    ) -> rest_models.GetAuditEventResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetAuditEvent is not yet implemented."
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
