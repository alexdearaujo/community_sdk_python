# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional
from typing import List as TypingList

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    ActError,
    AvailableActionsError,
    AvailableActionsForMitigationError,
    CreateError,
    GetError,
    ListError,
)
from ..models import (  # noqa: F401
    AggregationType,
    Alert,
    AlertAcknowledgement,
    AlertAutoAck,
    AlertAutoAckFilters,
    AlertAutoAckServiceCreateRequest,
    AlertAutoAckServiceCreateResponse,
    AlertAutoAckServiceDeleteResponse,
    AlertAutoAckServiceGetResponse,
    AlertAutoAckServiceListRequest,
    AlertAutoAckServiceListResponse,
    AlertAutoAckServiceReplaceBody,
    AlertAutoAckServiceReplaceResponse,
    AlertFilters,
    AlertPhase,
    AlertServiceAckBody,
    AlertServiceAckResponse,
    AlertServiceAddCommentBody,
    AlertServiceAddCommentResponse,
    AlertServiceClearRequest,
    AlertServiceClearResponse,
    AlertServiceGetResponse,
    AlertServiceListCommentsResponse,
    AlertServiceListRequest,
    AlertServiceListResponse,
    AlertServiceSetExternalContextBody,
    AlertServiceSetExternalContextResponse,
    AlertServiceUnAckBody,
    AlertServiceUnAckResponse,
    AlertSilenceNotificationFilters,
    AlertSilenceNotificationsDefinition,
    AlertSilenceNotificationsServiceCreateRequest,
    AlertSilenceNotificationsServiceCreateResponse,
    AlertSilenceNotificationsServiceDeleteResponse,
    AlertSilenceNotificationsServiceGetResponse,
    AlertSilenceNotificationsServiceListRequest,
    AlertSilenceNotificationsServiceListResponse,
    AlertSilenceNotificationsServiceReplaceBody,
    AlertSilenceNotificationsServiceReplaceResponse,
    AlertState,
    BaselineConditionDeltaType,
    BaselineConfigCompareMode,
    Comment,
    ConditionsBaselineCondition,
    ConditionsForecastCondition,
    ConditionsInterfaceCapacityCondition,
    ConditionsRatioCondition,
    ConditionsStaticCondition,
    ConditionsTopKeysCondition,
    EventPolicyLevelSettings,
    EventPolicySettings,
    EventPolicySettingsEventType,
    ExternalContext,
    FieldBy,
    FlowContext,
    FlowContextActivationStatus,
    FlowContextAlertKeyDetails,
    FlowContextDeviceDetails,
    FlowContextInterfaceDetails,
    FlowContextMetricValue,
    FlowContextSiteDetails,
    FlowPolicyLevelSettings,
    FlowPolicyLevelSettingsActivationSettings,
    FlowPolicyLevelSettingsConditions,
    FlowPolicyLevelSettingsConditionsOperator,
    FlowPolicyLevelSettingsMitigationAssociation,
    FlowPolicySettings,
    FlowPolicySettingsBaselineConfig,
    FlowPolicySettingsDatasetConfig,
    FlowPolicySettingsEvaluationConfig,
    JiraCloudContext,
    Mitigation,
    MitigationActionDetail,
    MitigationEvent,
    MitigationFilters,
    MitigationMethod,
    MitigationMethodsFilters,
    MitigationMethodsServiceGetResponse,
    MitigationMethodsServiceListResponse,
    MitigationPlatform,
    MitigationPlatformsFilters,
    MitigationPlatformsServiceGetResponse,
    MitigationPlatformsServiceListResponse,
    MitigationPlatformType,
    MitigationsActResult,
    MitigationsServiceActBody,
    MitigationsServiceActResponse,
    MitigationsServiceAvailableActionsForMitigationResponse,
    MitigationsServiceAvailableActionsResponse,
    MitigationsServiceAvailableActionsResponseMitigationAvailableTransitions,
    MitigationsServiceCreateRequest,
    MitigationsServiceCreateResponse,
    MitigationsServiceGetResponse,
    MitigationsServiceListResponse,
    MitigationState,
    MitigationStateEntry,
    MitigationType,
    MitigationUserAction,
    NmsActivateOrClearConditions,
    NmsCondition,
    NmsConditionConnector,
    NmsConditionGroup,
    NmsConditionOperator,
    NmsContext,
    NmsContextActivationInfo,
    NmsContextAlarmMetricMap,
    NmsContextAlarmTarget,
    NmsContextDatasetInfo,
    NmsPolicyLevelSettings,
    NmsPolicyLevelSettingsClearType,
    NmsPolicySettings,
    NmsPolicySettingsDatasetConfig,
    NmsPolicySettingsEvaluationConfig,
    NmsStateChangeCondition,
    NmsStateSet,
    NmsThresholdCondition,
    NotificationChannelAssociation,
    Policy,
    PolicyDataSources,
    PolicyDataSourcesDeviceTag,
    PolicyDimensionFilters,
    PolicyDimensionFiltersConjunction,
    PolicyDimensionFiltersEntry,
    PolicyDimensionFiltersEntryStringArray,
    PolicyFilters,
    PolicyFiltersFieldFilter,
    PolicyFiltersFilterConnector,
    PolicyFiltersOperator,
    PolicyFiltersSavedFilter,
    PolicyListFilters,
    PolicyPolicyErrorInfo,
    PolicyPolicyLevel,
    PolicyServiceDisableBody,
    PolicyServiceDisableResponse,
    PolicyServiceEnableBody,
    PolicyServiceEnableResponse,
    PolicyServiceGetResponse,
    PolicyServiceListRequest,
    PolicyServiceListResponse,
    PolicyType,
    RatioConditionDirection,
    ServiceNowContext,
    SortingConfigField,
    SortingConfigOrder,
    Source,
    Suppression,
    SuppressionFilters,
    SuppressionServiceCreateRequest,
    SuppressionServiceCreateResponse,
    SuppressionServiceDeleteResponse,
    SuppressionServiceGetResponse,
    SuppressionServiceListRequest,
    SuppressionServiceListResponse,
    SuppressionServiceReplaceBody,
    SuppressionServiceReplaceResponse,
    TopKeysConditionTopKeysEvent,
    protobufAny,
    rpcStatus,
    typesv202506PaginationConfig,
    typesv202506PaginationInfo,
    typesv202506SortingConfig,
    v202303AttributeFilter,
    v202303AttributeFilterStringArray,
    v202303KeyValue,
    v202303KeyValueFilter,
    v202303MultiAttributeFilter,
    v202303Severity,
    v202303SimpleAttributeFilter,
    v202303SimpleAttributeFilterStringArray,
    v202303TimeRange,
    v202501BitwiseOp,
    v202501FlowspecMatch,
    v202501Fragment,
    v202501FragmentFormula,
    v202501FragmentPredicate,
    v202501FragmentPredicateGroup,
    v202501NumericFormula,
    v202501NumericOp,
    v202501NumericPredicate,
    v202501NumericPredicateGroup,
    v202501TCPFlag,
    v202501TCPFlagsFormula,
    v202501TCPFlagsPredicate,
    v202501TCPFlagsPredicateGroup,
    v202506MitigationTarget,
)


def List(
    api_config_override: Optional[APIConfig] = None,
    *,
    paginationlimit: Optional[str] = None,
    paginationoffset: Optional[str] = None,
    paginationincludeTotalCount: Optional[bool] = None,
    filterscreatedAtstart: Optional[str] = None,
    filterscreatedAtend: Optional[str] = None,
    filtersmitigationIds: Optional[TypingList[str]] = None,
    filtersalarmIds: Optional[TypingList[str]] = None,
    filtersstates: Optional[TypingList[str]] = None,
    filtersplatformIds: Optional[TypingList[str]] = None,
    filtersmethodIds: Optional[TypingList[str]] = None,
    filtersipCidrs: Optional[TypingList[str]] = None,
    filtersipCidrPattern: Optional[str] = None,
    filterstypes: Optional[TypingList[str]] = None,
) -> MitigationsServiceListResponse:
    query_params: Dict[str, Any] = {
        "pagination.limit": paginationlimit,
        "pagination.offset": paginationoffset,
        "pagination.includeTotalCount": paginationincludeTotalCount,
        "filters.createdAt.start": filterscreatedAtstart,
        "filters.createdAt.end": filterscreatedAtend,
        "filters.mitigationIds": filtersmitigationIds,
        "filters.alarmIds": filtersalarmIds,
        "filters.states": filtersstates,
        "filters.platformIds": filtersplatformIds,
        "filters.methodIds": filtersmethodIds,
        "filters.ipCidrs": filtersipCidrs,
        "filters.ipCidrPattern": filtersipCidrPattern,
        "filters.types": filterstypes,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/v202505/mitigations",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="List",
        error_cls=ListError,
    )

    return (
        MitigationsServiceListResponse(**body)
        if body is not None
        else MitigationsServiceListResponse.model_construct()
    )


def Create(
    api_config_override: Optional[APIConfig] = None,
    *,
    data: MitigationsServiceCreateRequest,
) -> MitigationsServiceCreateResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/v202505/mitigations",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="Create",
        error_cls=CreateError,
    )

    return (
        MitigationsServiceCreateResponse(**body)
        if body is not None
        else MitigationsServiceCreateResponse.model_construct()
    )


def AvailableActions(
    api_config_override: Optional[APIConfig] = None,
) -> MitigationsServiceAvailableActionsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/v202505/mitigations/actions",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="AvailableActions",
        error_cls=AvailableActionsError,
    )

    return (
        MitigationsServiceAvailableActionsResponse(**body)
        if body is not None
        else MitigationsServiceAvailableActionsResponse.model_construct()
    )


def Get(
    api_config_override: Optional[APIConfig] = None, *, action: str
) -> MitigationsServiceGetResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/v202505/mitigations/{action}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="Get",
        error_cls=GetError,
    )

    return (
        MitigationsServiceGetResponse(**body)
        if body is not None
        else MitigationsServiceGetResponse.model_construct()
    )


def Act(
    api_config_override: Optional[APIConfig] = None,
    *,
    action: str,
    data: MitigationsServiceActBody,
) -> MitigationsServiceActResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/v202505/mitigations/{action}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="Act",
        error_cls=ActError,
    )

    return (
        MitigationsServiceActResponse(**body)
        if body is not None
        else MitigationsServiceActResponse.model_construct()
    )


def AvailableActionsForMitigation(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> MitigationsServiceAvailableActionsForMitigationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/v202505/mitigations/{id}/actions",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="AvailableActionsForMitigation",
        error_cls=AvailableActionsForMitigationError,
    )

    return (
        MitigationsServiceAvailableActionsForMitigationResponse(**body)
        if body is not None
        else MitigationsServiceAvailableActionsForMitigationResponse.model_construct()
    )
