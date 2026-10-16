# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class SyntheticsError(HTTPException):
    """Base service-local error for the synthetics API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "SyntheticsError":
        preview = getattr(response, "text", "")[:200].replace("\n", " ")
        headers = getattr(response, "headers", {})
        content_type = (
            headers.get("content-type", "unknown")
            if hasattr(headers, "get")
            else "unknown"
        )
        details: dict[str, Any] = {
            "content_type": content_type,
            "preview": preview,
        }
        message = f"{operation_name} failed with status code: {getattr(response, 'status_code', 'unknown')}"
        try:
            payload = response.json()
        except Exception:
            payload = None
        if isinstance(payload, dict):
            details["response_json"] = payload
            try:
                status = rpcStatus.model_validate(payload)
            except Exception:
                status = None
            if status is not None:
                details["rpc_status"] = payload
                if status.code is not None:
                    details["rpc_status_code"] = status.code
                if status.message:
                    message = status.message
                else:
                    message = payload.get("message") or message
            else:
                message = payload.get("message") or message
        elif payload is not None:
            details["response_json"] = payload
        return cls(
            getattr(response, "status_code", 500),
            message,
            method=method,
            path=path,
            details=details,
        )

    @classmethod
    def from_response(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "SyntheticsError":
        status_key = str(getattr(response, "status_code", ""))
        response_error_map = getattr(cls, "response_error_map", {})
        target_cls = (
            response_error_map.get(status_key)
            or response_error_map.get("default")
            or cls
        )
        return target_cls._build_error(
            response,
            operation_name=operation_name,
            method=method,
            path=path,
        )


class CreateAgentAlertError(SyntheticsError):
    """Operation-local error for CreateAgentAlert."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class CreateAgentAlertUnexpectedError(CreateAgentAlertError):
    """Operation-local response error for CreateAgentAlert (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateAgentAlertError.response_error_map = {
    "default": CreateAgentAlertUnexpectedError,
}


class CreateTestError(SyntheticsError):
    """Operation-local error for CreateTest."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class CreateTestUnexpectedError(CreateTestError):
    """Operation-local response error for CreateTest (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateTestError.response_error_map = {
    "default": CreateTestUnexpectedError,
}


class DeleteAgentError(SyntheticsError):
    """Operation-local error for DeleteAgent."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class DeleteAgentUnexpectedError(DeleteAgentError):
    """Operation-local response error for DeleteAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteAgentError.response_error_map = {
    "default": DeleteAgentUnexpectedError,
}


class DeleteAgentAlertError(SyntheticsError):
    """Operation-local error for DeleteAgentAlert."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class DeleteAgentAlertUnexpectedError(DeleteAgentAlertError):
    """Operation-local response error for DeleteAgentAlert (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteAgentAlertError.response_error_map = {
    "default": DeleteAgentAlertUnexpectedError,
}


class DeleteTestError(SyntheticsError):
    """Operation-local error for DeleteTest."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class DeleteTestUnexpectedError(DeleteTestError):
    """Operation-local response error for DeleteTest (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteTestError.response_error_map = {
    "default": DeleteTestUnexpectedError,
}


class GetAgentError(SyntheticsError):
    """Operation-local error for GetAgent."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class GetAgentUnexpectedError(GetAgentError):
    """Operation-local response error for GetAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetAgentError.response_error_map = {
    "default": GetAgentUnexpectedError,
}


class GetAgentAlertError(SyntheticsError):
    """Operation-local error for GetAgentAlert."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class GetAgentAlertUnexpectedError(GetAgentAlertError):
    """Operation-local response error for GetAgentAlert (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetAgentAlertError.response_error_map = {
    "default": GetAgentAlertUnexpectedError,
}


class GetResultsForTestsError(SyntheticsError):
    """Operation-local error for GetResultsForTests."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class GetResultsForTestsUnexpectedError(GetResultsForTestsError):
    """Operation-local response error for GetResultsForTests (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetResultsForTestsError.response_error_map = {
    "default": GetResultsForTestsUnexpectedError,
}


class GetResultsForTestsCsvError(SyntheticsError):
    """Operation-local error for GetResultsForTestsCsv."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class GetResultsForTestsCsvUnexpectedError(GetResultsForTestsCsvError):
    """Operation-local response error for GetResultsForTestsCsv (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetResultsForTestsCsvError.response_error_map = {
    "default": GetResultsForTestsCsvUnexpectedError,
}


class GetTestError(SyntheticsError):
    """Operation-local error for GetTest."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class GetTestUnexpectedError(GetTestError):
    """Operation-local response error for GetTest (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetTestError.response_error_map = {
    "default": GetTestUnexpectedError,
}


class GetTraceForTestError(SyntheticsError):
    """Operation-local error for GetTraceForTest."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class GetTraceForTestUnexpectedError(GetTraceForTestError):
    """Operation-local response error for GetTraceForTest (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetTraceForTestError.response_error_map = {
    "default": GetTraceForTestUnexpectedError,
}


class ListAgentAlertsError(SyntheticsError):
    """Operation-local error for ListAgentAlerts."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class ListAgentAlertsUnexpectedError(ListAgentAlertsError):
    """Operation-local response error for ListAgentAlerts (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListAgentAlertsError.response_error_map = {
    "default": ListAgentAlertsUnexpectedError,
}


class ListAgentsError(SyntheticsError):
    """Operation-local error for ListAgents."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class ListAgentsUnexpectedError(ListAgentsError):
    """Operation-local response error for ListAgents (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListAgentsError.response_error_map = {
    "default": ListAgentsUnexpectedError,
}


class ListTestsError(SyntheticsError):
    """Operation-local error for ListTests."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class ListTestsUnexpectedError(ListTestsError):
    """Operation-local response error for ListTests (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListTestsError.response_error_map = {
    "default": ListTestsUnexpectedError,
}


class SetTestStatusError(SyntheticsError):
    """Operation-local error for SetTestStatus."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class SetTestStatusUnexpectedError(SetTestStatusError):
    """Operation-local response error for SetTestStatus (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


SetTestStatusError.response_error_map = {
    "default": SetTestStatusUnexpectedError,
}


class UpdateAgentError(SyntheticsError):
    """Operation-local error for UpdateAgent."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class UpdateAgentUnexpectedError(UpdateAgentError):
    """Operation-local response error for UpdateAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateAgentError.response_error_map = {
    "default": UpdateAgentUnexpectedError,
}


class UpdateAgentAlertError(SyntheticsError):
    """Operation-local error for UpdateAgentAlert."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class UpdateAgentAlertUnexpectedError(UpdateAgentAlertError):
    """Operation-local response error for UpdateAgentAlert (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateAgentAlertError.response_error_map = {
    "default": UpdateAgentAlertUnexpectedError,
}


class UpdateTestError(SyntheticsError):
    """Operation-local error for UpdateTest."""

    response_error_map: dict[str, type[SyntheticsError]] = {}


class UpdateTestUnexpectedError(UpdateTestError):
    """Operation-local response error for UpdateTest (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateTestError.response_error_map = {
    "default": UpdateTestUnexpectedError,
}

ERROR_BY_OPERATION: dict[str, type[SyntheticsError]] = {
    "CreateAgentAlert": CreateAgentAlertError,
    "CreateTest": CreateTestError,
    "DeleteAgent": DeleteAgentError,
    "DeleteAgentAlert": DeleteAgentAlertError,
    "DeleteTest": DeleteTestError,
    "GetAgent": GetAgentError,
    "GetAgentAlert": GetAgentAlertError,
    "GetResultsForTests": GetResultsForTestsError,
    "GetResultsForTestsCsv": GetResultsForTestsCsvError,
    "GetTest": GetTestError,
    "GetTraceForTest": GetTraceForTestError,
    "ListAgentAlerts": ListAgentAlertsError,
    "ListAgents": ListAgentsError,
    "ListTests": ListTestsError,
    "SetTestStatus": SetTestStatusError,
    "UpdateAgent": UpdateAgentError,
    "UpdateAgentAlert": UpdateAgentAlertError,
    "UpdateTest": UpdateTestError,
}

__all__ = [
    "SyntheticsError",
    "CreateAgentAlertUnexpectedError",
    "CreateTestUnexpectedError",
    "DeleteAgentUnexpectedError",
    "DeleteAgentAlertUnexpectedError",
    "DeleteTestUnexpectedError",
    "GetAgentUnexpectedError",
    "GetAgentAlertUnexpectedError",
    "GetResultsForTestsUnexpectedError",
    "GetResultsForTestsCsvUnexpectedError",
    "GetTestUnexpectedError",
    "GetTraceForTestUnexpectedError",
    "ListAgentAlertsUnexpectedError",
    "ListAgentsUnexpectedError",
    "ListTestsUnexpectedError",
    "SetTestStatusUnexpectedError",
    "UpdateAgentUnexpectedError",
    "UpdateAgentAlertUnexpectedError",
    "UpdateTestUnexpectedError",
    "CreateAgentAlertError",
    "CreateTestError",
    "DeleteAgentError",
    "DeleteAgentAlertError",
    "DeleteTestError",
    "GetAgentError",
    "GetAgentAlertError",
    "GetResultsForTestsError",
    "GetResultsForTestsCsvError",
    "GetTestError",
    "GetTraceForTestError",
    "ListAgentAlertsError",
    "ListAgentsError",
    "ListTestsError",
    "SetTestStatusError",
    "UpdateAgentError",
    "UpdateAgentAlertError",
    "UpdateTestError",
    "ERROR_BY_OPERATION",
]
