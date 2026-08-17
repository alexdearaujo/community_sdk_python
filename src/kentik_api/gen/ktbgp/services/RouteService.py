from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    RouteService_AnnounceError,
    RouteService_ListError,
    RouteService_WithdrawError,
)
from ..models import (  # noqa: F401
    AdvertStatus,
    BitwiseOp,
    DeviceAdverts,
    ExtendedCommunityRouteType,
    FlowspecAction,
    FlowspecActionAccept,
    FlowspecActionDiscard,
    FlowspecActionExtendedCommunity,
    FlowspecActionIPNextHopCopy,
    FlowspecActionIPNextHopRedirect,
    FlowspecActionLargeCommunity,
    FlowspecActionMarkDSCP,
    FlowspecActionRegularCommunity,
    FlowspecActionRouteTargetRedirect,
    FlowspecActionTerminalSample,
    FlowspecActionTrafficRateBytes,
    FlowspecMatch,
    FlowspecUpdate,
    Fragment,
    FragmentFormula,
    FragmentPredicate,
    FragmentPredicateGroup,
    InetType,
    NumericFormula,
    NumericOp,
    NumericPredicate,
    NumericPredicateGroup,
    RouteServiceAnnounceRequest,
    RouteServiceAnnounceResponse,
    RouteServiceListRequest,
    RouteServiceListResponse,
    RouteServiceWithdrawRequest,
    RouteServiceWithdrawResponse,
    RoutesFilter,
    RTBHAction,
    RTBHMatch,
    RTBHUpdate,
    TCPFlag,
    TCPFlagsFormula,
    TCPFlagsPredicate,
    TCPFlagsPredicateGroup,
    UpdateResult,
    ktbgpv202501Withdraw,
    protobufAny,
    rpcStatus,
)


def RouteService_Announce(
    api_config_override: Optional[APIConfig] = None,
    *,
    data: RouteServiceAnnounceRequest,
) -> RouteServiceAnnounceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/routes/announce",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="RouteService_Announce",
        error_cls=RouteService_AnnounceError,
    )

    return (
        RouteServiceAnnounceResponse(**body)
        if body is not None
        else RouteServiceAnnounceResponse.model_construct()
    )


def RouteService_List(
    api_config_override: Optional[APIConfig] = None, *, data: RouteServiceListRequest
) -> RouteServiceListResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/routes/list",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="RouteService_List",
        error_cls=RouteService_ListError,
    )

    return (
        RouteServiceListResponse(**body)
        if body is not None
        else RouteServiceListResponse.model_construct()
    )


def RouteService_Withdraw(
    api_config_override: Optional[APIConfig] = None,
    *,
    data: RouteServiceWithdrawRequest,
) -> RouteServiceWithdrawResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/routes/withdraw",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="RouteService_Withdraw",
        error_cls=RouteService_WithdrawError,
    )

    return (
        RouteServiceWithdrawResponse(**body)
        if body is not None
        else RouteServiceWithdrawResponse.model_construct()
    )
