from typing import Union, cast, Optional, List
from kentik_api.gen.alerting import models as rest_models
import kentik_api.gen.alerting.services.AlertAutoAckService as RestAlertingModule1
import kentik_api.gen.alerting.services.AlertService as RestAlertingModule2
import kentik_api.gen.alerting.services.AlertSilenceNotificationsService as RestAlertingModule3
import kentik_api.gen.alerting.services.MitigationMethodsService as RestAlertingModule4
import kentik_api.gen.alerting.services.MitigationPlatformsService as RestAlertingModule5
import kentik_api.gen.alerting.services.MitigationsService as RestAlertingModule6
import kentik_api.gen.alerting.services.PolicyService as RestAlertingModule7
import kentik_api.gen.alerting.services.SuppressionService as RestAlertingModule8
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


class AlertingServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.alerting.pb.alert_pb2 as _pb2_1_mod
                import kentik_api.gen.alerting.pb.alert_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.AlertServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.alerting.pb.auto_ack_pb2 as _pb2_2_mod
                import kentik_api.gen.alerting.pb.auto_ack_pb2_grpc as _pb2_grpc_2_mod

                self._grpc_pb2_2 = _pb2_2_mod
                self._grpc_stub_2 = _pb2_grpc_2_mod.AlertAutoAckServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_2 = None
                self._grpc_stub_2 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.alerting.pb.mitigation_method_pb2 as _pb2_3_mod
                import kentik_api.gen.alerting.pb.mitigation_method_pb2_grpc as _pb2_grpc_3_mod

                self._grpc_pb2_3 = _pb2_3_mod
                self._grpc_stub_3 = _pb2_grpc_3_mod.MitigationMethodsServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_3 = None
                self._grpc_stub_3 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.alerting.pb.mitigation_platform_pb2 as _pb2_4_mod
                import kentik_api.gen.alerting.pb.mitigation_platform_pb2_grpc as _pb2_grpc_4_mod

                self._grpc_pb2_4 = _pb2_4_mod
                self._grpc_stub_4 = _pb2_grpc_4_mod.MitigationPlatformsServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_4 = None
                self._grpc_stub_4 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.alerting.pb.policy_pb2 as _pb2_5_mod
                import kentik_api.gen.alerting.pb.policy_pb2_grpc as _pb2_grpc_5_mod

                self._grpc_pb2_5 = _pb2_5_mod
                self._grpc_stub_5 = _pb2_grpc_5_mod.PolicyServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_5 = None
                self._grpc_stub_5 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.alerting.pb.silencing_pb2 as _pb2_6_mod
                import kentik_api.gen.alerting.pb.silencing_pb2_grpc as _pb2_grpc_6_mod

                self._grpc_pb2_6 = _pb2_6_mod
                self._grpc_stub_6 = (
                    _pb2_grpc_6_mod.AlertSilenceNotificationsServiceStub(
                        self._transport.channel
                    )
                )
            except (ImportError, TypeError):
                self._grpc_pb2_6 = None
                self._grpc_stub_6 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.alerting.pb.suppressions_pb2 as _pb2_7_mod
                import kentik_api.gen.alerting.pb.suppressions_pb2_grpc as _pb2_grpc_7_mod

                self._grpc_pb2_7 = _pb2_7_mod
                self._grpc_stub_7 = _pb2_grpc_7_mod.SuppressionServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_7 = None
                self._grpc_stub_7 = None

    def create(
        self, *, data: rest_models.AlertAutoAckServiceCreateRequest
    ) -> rest_models.AlertAutoAckServiceCreateResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceCreateRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Create, _req)
            return rest_models.AlertAutoAckServiceCreateResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.Create(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list(
        self, *, data: rest_models.AlertAutoAckServiceListRequest
    ) -> rest_models.AlertAutoAckServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceListRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.List, _req)
            return rest_models.AlertAutoAckServiceListResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get(self, *, autoAckid: str) -> rest_models.AlertAutoAckServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"autoAckid": autoAckid}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceGetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Get, _req)
            return rest_models.AlertAutoAckServiceGetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.Get(
                api_config_override=rest_transport.api_config, autoAckid=autoAckid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete(
        self, *, autoAckid: str
    ) -> rest_models.AlertAutoAckServiceDeleteResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"autoAckid": autoAckid}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceDeleteRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Delete, _req)
            return rest_models.AlertAutoAckServiceDeleteResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.Delete(
                api_config_override=rest_transport.api_config, autoAckid=autoAckid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def replace(
        self, *, autoAckid: str, data: rest_models.AlertAutoAckServiceReplaceBody
    ) -> rest_models.AlertAutoAckServiceReplaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"autoAckid": autoAckid}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_7.SuppressionServiceReplaceRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Replace, _req)
            return rest_models.AlertAutoAckServiceReplaceResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.Replace(
                api_config_override=rest_transport.api_config,
                autoAckid=autoAckid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_list(
        self, *, data: rest_models.AlertServiceListRequest
    ) -> rest_models.AlertServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceListRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.List, _req)
            return rest_models.AlertServiceListResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def clear(
        self, *, data: rest_models.AlertServiceClearRequest
    ) -> rest_models.AlertServiceClearResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.AlertServiceClearRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.Clear, _req)
            return rest_models.AlertServiceClearResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.Clear(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_comments(
        self, *, alertId: str
    ) -> rest_models.AlertServiceListCommentsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"alertId": alertId}.items() if v is not None},
                self._grpc_pb2_1.AlertServiceListCommentsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ListComments, _req)
            return rest_models.AlertServiceListCommentsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.ListComments(
                api_config_override=rest_transport.api_config, alertId=alertId
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def add_comment(
        self, *, alertId: str, data: rest_models.AlertServiceAddCommentBody
    ) -> rest_models.AlertServiceAddCommentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"alertId": alertId}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.AlertServiceAddCommentRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.AddComment, _req)
            return rest_models.AlertServiceAddCommentResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.AddComment(
                api_config_override=rest_transport.api_config,
                alertId=alertId,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def set_external_context(
        self, *, alertId: str, data: rest_models.AlertServiceSetExternalContextBody
    ) -> rest_models.AlertServiceSetExternalContextResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"alertId": alertId}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.AlertServiceSetExternalContextRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.SetExternalContext, _req)
            return rest_models.AlertServiceSetExternalContextResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.SetExternalContext(
                api_config_override=rest_transport.api_config,
                alertId=alertId,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_get(self, *, id: str) -> rest_models.AlertServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceGetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Get, _req)
            return rest_models.AlertServiceGetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def ack(
        self, *, id: str, data: rest_models.AlertServiceAckBody
    ) -> rest_models.AlertServiceAckResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.AlertServiceAckRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.Ack, _req)
            return rest_models.AlertServiceAckResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.Ack(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def un_ack(
        self, *, id: str, data: rest_models.AlertServiceUnAckBody
    ) -> rest_models.AlertServiceUnAckResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.AlertServiceUnAckRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UnAck, _req)
            return rest_models.AlertServiceUnAckResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.UnAck(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_create(
        self, *, data: rest_models.AlertSilenceNotificationsServiceCreateRequest
    ) -> rest_models.AlertSilenceNotificationsServiceCreateResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceCreateRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Create, _req)
            return rest_models.AlertSilenceNotificationsServiceCreateResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.Create(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_list(
        self, *, data: rest_models.AlertSilenceNotificationsServiceListRequest
    ) -> rest_models.AlertSilenceNotificationsServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceListRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.List, _req)
            return (
                rest_models.AlertSilenceNotificationsServiceListResponse.model_validate(
                    MessageToDict(_resp)
                )
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_get(
        self, *, id: str
    ) -> rest_models.AlertSilenceNotificationsServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceGetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Get, _req)
            return (
                rest_models.AlertSilenceNotificationsServiceGetResponse.model_validate(
                    MessageToDict(_resp)
                )
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_delete(
        self, *, id: str
    ) -> rest_models.AlertSilenceNotificationsServiceDeleteResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceDeleteRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Delete, _req)
            return rest_models.AlertSilenceNotificationsServiceDeleteResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.Delete(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_replace(
        self, *, id: str, data: rest_models.AlertSilenceNotificationsServiceReplaceBody
    ) -> rest_models.AlertSilenceNotificationsServiceReplaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_7.SuppressionServiceReplaceRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Replace, _req)
            return rest_models.AlertSilenceNotificationsServiceReplaceResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.Replace(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigation_methods_list(
        self,
        *,
        paginationlimit: Optional[str] = None,
        paginationoffset: Optional[str] = None,
        paginationincludeTotalCount: Optional[bool] = None,
        filtersmethodIds: Optional[List[str]] = None,
        filtersplatformTypes: Optional[List[str]] = None,
        filterscreatedAtstart: Optional[str] = None,
        filterscreatedAtend: Optional[str] = None,
        filtersmodifiedAtstart: Optional[str] = None,
        filtersmodifiedAtend: Optional[str] = None,
    ) -> rest_models.MitigationMethodsServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "paginationlimit": paginationlimit,
                        "paginationoffset": paginationoffset,
                        "paginationincludeTotalCount": paginationincludeTotalCount,
                        "filtersmethodIds": filtersmethodIds,
                        "filtersplatformTypes": filtersplatformTypes,
                        "filterscreatedAtstart": filterscreatedAtstart,
                        "filterscreatedAtend": filterscreatedAtend,
                        "filtersmodifiedAtstart": filtersmodifiedAtstart,
                        "filtersmodifiedAtend": filtersmodifiedAtend,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_7.SuppressionServiceListRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.List, _req)
            return rest_models.MitigationMethodsServiceListResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule4.List(
                api_config_override=rest_transport.api_config,
                paginationlimit=paginationlimit,
                paginationoffset=paginationoffset,
                paginationincludeTotalCount=paginationincludeTotalCount,
                filtersmethodIds=filtersmethodIds,
                filtersplatformTypes=filtersplatformTypes,
                filterscreatedAtstart=filterscreatedAtstart,
                filterscreatedAtend=filterscreatedAtend,
                filtersmodifiedAtstart=filtersmodifiedAtstart,
                filtersmodifiedAtend=filtersmodifiedAtend,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigation_methods_get(
        self, *, id: str
    ) -> rest_models.MitigationMethodsServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceGetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Get, _req)
            return rest_models.MitigationMethodsServiceGetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule4.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigation_platforms_list(
        self,
        *,
        paginationlimit: Optional[str] = None,
        paginationoffset: Optional[str] = None,
        paginationincludeTotalCount: Optional[bool] = None,
        filtersplatformIds: Optional[List[str]] = None,
        filtersplatformTypes: Optional[List[str]] = None,
        filterscreatedAtstart: Optional[str] = None,
        filterscreatedAtend: Optional[str] = None,
        filtersmodifiedAtstart: Optional[str] = None,
        filtersmodifiedAtend: Optional[str] = None,
    ) -> rest_models.MitigationPlatformsServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "paginationlimit": paginationlimit,
                        "paginationoffset": paginationoffset,
                        "paginationincludeTotalCount": paginationincludeTotalCount,
                        "filtersplatformIds": filtersplatformIds,
                        "filtersplatformTypes": filtersplatformTypes,
                        "filterscreatedAtstart": filterscreatedAtstart,
                        "filterscreatedAtend": filterscreatedAtend,
                        "filtersmodifiedAtstart": filtersmodifiedAtstart,
                        "filtersmodifiedAtend": filtersmodifiedAtend,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_7.SuppressionServiceListRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.List, _req)
            return rest_models.MitigationPlatformsServiceListResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule5.List(
                api_config_override=rest_transport.api_config,
                paginationlimit=paginationlimit,
                paginationoffset=paginationoffset,
                paginationincludeTotalCount=paginationincludeTotalCount,
                filtersplatformIds=filtersplatformIds,
                filtersplatformTypes=filtersplatformTypes,
                filterscreatedAtstart=filterscreatedAtstart,
                filterscreatedAtend=filterscreatedAtend,
                filtersmodifiedAtstart=filtersmodifiedAtstart,
                filtersmodifiedAtend=filtersmodifiedAtend,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigation_platforms_get(
        self, *, id: str
    ) -> rest_models.MitigationPlatformsServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceGetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Get, _req)
            return rest_models.MitigationPlatformsServiceGetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule5.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigations_list(
        self,
        *,
        paginationlimit: Optional[str] = None,
        paginationoffset: Optional[str] = None,
        paginationincludeTotalCount: Optional[bool] = None,
        filterscreatedAtstart: Optional[str] = None,
        filterscreatedAtend: Optional[str] = None,
        filtersmitigationIds: Optional[List[str]] = None,
        filtersalarmIds: Optional[List[str]] = None,
        filtersstates: Optional[List[str]] = None,
        filtersplatformIds: Optional[List[str]] = None,
        filtersmethodIds: Optional[List[str]] = None,
        filtersipCidrs: Optional[List[str]] = None,
        filtersipCidrPattern: Optional[str] = None,
        filterstypes: Optional[List[str]] = None,
    ) -> rest_models.MitigationsServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "paginationlimit": paginationlimit,
                        "paginationoffset": paginationoffset,
                        "paginationincludeTotalCount": paginationincludeTotalCount,
                        "filterscreatedAtstart": filterscreatedAtstart,
                        "filterscreatedAtend": filterscreatedAtend,
                        "filtersmitigationIds": filtersmitigationIds,
                        "filtersalarmIds": filtersalarmIds,
                        "filtersstates": filtersstates,
                        "filtersplatformIds": filtersplatformIds,
                        "filtersmethodIds": filtersmethodIds,
                        "filtersipCidrs": filtersipCidrs,
                        "filtersipCidrPattern": filtersipCidrPattern,
                        "filterstypes": filterstypes,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_7.SuppressionServiceListRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.List, _req)
            return rest_models.MitigationsServiceListResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.List(
                api_config_override=rest_transport.api_config,
                paginationlimit=paginationlimit,
                paginationoffset=paginationoffset,
                paginationincludeTotalCount=paginationincludeTotalCount,
                filterscreatedAtstart=filterscreatedAtstart,
                filterscreatedAtend=filterscreatedAtend,
                filtersmitigationIds=filtersmitigationIds,
                filtersalarmIds=filtersalarmIds,
                filtersstates=filtersstates,
                filtersplatformIds=filtersplatformIds,
                filtersmethodIds=filtersmethodIds,
                filtersipCidrs=filtersipCidrs,
                filtersipCidrPattern=filtersipCidrPattern,
                filterstypes=filterstypes,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigations_create(
        self, *, data: rest_models.MitigationsServiceCreateRequest
    ) -> rest_models.MitigationsServiceCreateResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceCreateRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Create, _req)
            return rest_models.MitigationsServiceCreateResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.Create(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def available_actions(
        self,
    ) -> rest_models.MitigationsServiceAvailableActionsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for AvailableActions is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.AvailableActions(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigations_get(
        self, *, action: str
    ) -> rest_models.MitigationsServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"action": action}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceGetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Get, _req)
            return rest_models.MitigationsServiceGetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.Get(
                api_config_override=rest_transport.api_config, action=action
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def act(
        self, *, action: str, data: rest_models.MitigationsServiceActBody
    ) -> rest_models.MitigationsServiceActResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Act is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.Act(
                api_config_override=rest_transport.api_config, action=action, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def available_actions_for_mitigation(
        self, *, id: str
    ) -> rest_models.MitigationsServiceAvailableActionsForMitigationResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for AvailableActionsForMitigation is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.AvailableActionsForMitigation(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def policy_list(
        self, *, data: rest_models.PolicyServiceListRequest
    ) -> rest_models.PolicyServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceListRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.List, _req)
            return rest_models.PolicyServiceListResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule7.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def policy_get(
        self, *, policyType: str, id: str
    ) -> rest_models.PolicyServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {"policyType": policyType, "id": id}.items()
                    if v is not None
                },
                self._grpc_pb2_7.SuppressionServiceGetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Get, _req)
            return rest_models.PolicyServiceGetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule7.Get(
                api_config_override=rest_transport.api_config,
                policyType=policyType,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def disable(
        self, *, policyType: str, id: str, data: rest_models.PolicyServiceDisableBody
    ) -> rest_models.PolicyServiceDisableResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {
                    k: v
                    for k, v in {"policyType": policyType, "id": id}.items()
                    if v is not None
                }
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_5.PolicyServiceDisableRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_5.Disable, _req)
            return rest_models.PolicyServiceDisableResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule7.Disable(
                api_config_override=rest_transport.api_config,
                policyType=policyType,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def enable(
        self, *, policyType: str, id: str, data: rest_models.PolicyServiceEnableBody
    ) -> rest_models.PolicyServiceEnableResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {
                    k: v
                    for k, v in {"policyType": policyType, "id": id}.items()
                    if v is not None
                }
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_5.PolicyServiceEnableRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_5.Enable, _req)
            return rest_models.PolicyServiceEnableResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule7.Enable(
                api_config_override=rest_transport.api_config,
                policyType=policyType,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_create(
        self, *, data: rest_models.SuppressionServiceCreateRequest
    ) -> rest_models.SuppressionServiceCreateResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceCreateRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Create, _req)
            return rest_models.SuppressionServiceCreateResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.Create(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_list(
        self, *, data: rest_models.SuppressionServiceListRequest
    ) -> rest_models.SuppressionServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_7.SuppressionServiceListRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.List, _req)
            return rest_models.SuppressionServiceListResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_get(self, *, id: str) -> rest_models.SuppressionServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceGetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Get, _req)
            return rest_models.SuppressionServiceGetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_delete(
        self, *, id: str
    ) -> rest_models.SuppressionServiceDeleteResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_7.SuppressionServiceDeleteRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Delete, _req)
            return rest_models.SuppressionServiceDeleteResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.Delete(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_replace(
        self, *, id: str, data: rest_models.SuppressionServiceReplaceBody
    ) -> rest_models.SuppressionServiceReplaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_7 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for alerting service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_7.SuppressionServiceReplaceRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_7.Replace, _req)
            return rest_models.SuppressionServiceReplaceResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.Replace(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
