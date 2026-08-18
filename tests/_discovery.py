"""Shared schema/wrapper discovery helpers for the tests/ tree.

Every operation, parameter, and declared response status code exercised by
the generated/e2e test suites is discovered from the generated code itself
(AST-parsed or introspected at runtime) rather than hand-listed, so new
services/endpoints picked up by `make generate` are covered automatically.

Lives at the tests/ root (not inside tests/generated/) because both
tests/generated/*.py and tests/e2e/*.py import it; tests/conftest.py puts
tests/ on sys.path so `import _discovery` resolves the same way regardless
of which subdirectory pytest is invoked against.
"""

from __future__ import annotations

import ast
import importlib
import inspect
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Optional, Union, get_args, get_origin

from pydantic import BaseModel


@dataclass(frozen=True)
class WrapperCase:
    module_path: str
    file_path: Path
    wrapper_class: str
    method_name: str
    rest_module_alias: str
    rest_function_name: str


def case_label(case: WrapperCase) -> str:
    return (
        f"{case.wrapper_class}.{case.method_name} "
        f"[{case.module_path}:{case.rest_module_alias}.{case.rest_function_name}]"
    )


def print_case_start(case: WrapperCase, mode: str) -> None:
    print(f'Testing against "{case_label(case)}". Mode={mode}. START')


def print_case_result(case: WrapperCase, mode: str, result: str) -> None:
    print(f'Testing against "{case_label(case)}". Mode={mode}. RESULT={result}')


def service_to_pascal_case(service: str) -> str:
    return "".join(part.capitalize() for part in service.split("_") if part)


def generated_root() -> Path:
    return Path(__file__).resolve().parents[1] / "src" / "kentik_api" / "gen"


def _parse_wrapper_calls(file_path: Path) -> dict[str, tuple[str, str]]:
    tree = ast.parse(file_path.read_text(encoding="utf-8"))

    wrapper_class = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name.endswith("ServiceWrapper"):
            wrapper_class = node
            break

    if wrapper_class is None:
        return {}

    mapping: dict[str, tuple[str, str]] = {}
    for node in wrapper_class.body:
        if not isinstance(node, ast.FunctionDef) or node.name in {"__init__"}:
            continue

        alias = None
        rest_func = None
        for sub in ast.walk(node):
            if not isinstance(sub, ast.Return) or not isinstance(sub.value, ast.Call):
                continue
            call_func = sub.value.func
            if (
                isinstance(call_func, ast.Attribute)
                and isinstance(call_func.value, ast.Name)
                and call_func.value.id.startswith("Rest")
            ):
                alias = call_func.value.id
                rest_func = call_func.attr
                break

        if alias and rest_func:
            mapping[node.name] = (alias, rest_func)

    return mapping


def discover_cases() -> list[WrapperCase]:
    cases: list[WrapperCase] = []
    root = generated_root()

    for service_dir in sorted(root.iterdir()):
        if not service_dir.is_dir():
            continue

        service = service_dir.name
        services_dir = service_dir / "services"
        if not services_dir.exists():
            services_dir = service_dir / "service"
            if not services_dir.exists():
                continue

        wrapper_file = services_dir / f"{service}.py"
        if not wrapper_file.exists():
            continue

        method_map = _parse_wrapper_calls(wrapper_file)
        wrapper_class = f"{service_to_pascal_case(service)}ServiceWrapper"
        module_path = f"kentik_api.gen.{service}.{services_dir.name}.{service}"

        for method_name, (alias, fn_name) in sorted(method_map.items()):
            cases.append(
                WrapperCase(
                    module_path=module_path,
                    file_path=wrapper_file,
                    wrapper_class=wrapper_class,
                    method_name=method_name,
                    rest_module_alias=alias,
                    rest_function_name=fn_name,
                )
            )

    return cases


def sample_value_by_name(name: str) -> Any:
    lowered = name.lower()
    if lowered in {"id", "tagid", "deviceid", "customdimensionid", "populatorid"}:
        return "id-1"
    if lowered.endswith("name"):
        return "name"
    if lowered.startswith("is") or lowered.startswith("has"):
        return True
    if lowered in {"offset", "limit", "page", "size"}:
        return 1
    return object()


def sample_model_instance(
    model_cls: type[BaseModel], _seen: frozenset = frozenset()
) -> BaseModel:
    """Builds a minimal valid instance of a generated Pydantic model.

    Only required fields are filled (optional fields are left to their
    defaults), mirroring the smallest payload a real caller could send.
    """
    if model_cls in _seen:
        raise ValueError(
            f"Recursive model reference detected while sampling {model_cls!r}"
        )
    seen = _seen | {model_cls}

    kwargs: dict[str, Any] = {}
    for field_name, field_info in model_cls.model_fields.items():
        if not field_info.is_required():
            continue
        kwargs[field_name] = _sample_value_for_type(
            field_info.annotation, field_name, seen
        )
    return model_cls(**kwargs)


def _sample_value_for_type(annotation: Any, name: str, seen: frozenset) -> Any:
    if annotation is inspect.Parameter.empty or annotation is Any:
        return sample_value_by_name(name)

    origin = get_origin(annotation)
    if origin is Union:
        args = [arg for arg in get_args(annotation) if arg is not type(None)]
        return _sample_value_for_type(args[0], name, seen) if args else None

    if origin in (list, set, frozenset):
        args = get_args(annotation)
        item_type = args[0] if args else Any
        item = _sample_value_for_type(item_type, name, seen)
        return [item] if origin is list else {item}

    if origin is dict:
        return {}

    if isinstance(annotation, type) and issubclass(annotation, BaseModel):
        return sample_model_instance(annotation, seen)

    if isinstance(annotation, type) and issubclass(annotation, Enum):
        return next(iter(annotation))

    if annotation is str:
        return f"{name}_value"
    if annotation is int:
        return 1
    if annotation is float:
        return 1.0
    if annotation is bool:
        return True
    if annotation is bytes:
        return b"sample-bytes"

    return sample_value_by_name(name)


def sample_value_for_annotation(annotation: Any, name: str) -> Any:
    if annotation is inspect.Parameter.empty:
        return sample_value_by_name(name)
    return _sample_value_for_type(annotation, name, frozenset())


def build_required_kwargs(method: Any) -> dict[str, Any]:
    sig = inspect.signature(method)
    kwargs: dict[str, Any] = {}
    for param in sig.parameters.values():
        if param.name == "self":
            continue
        if param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
            continue
        if param.default is inspect.Parameter.empty:
            kwargs[param.name] = sample_value_for_annotation(
                param.annotation, param.name
            )
    return kwargs


def build_all_kwargs(method: Any) -> dict[str, Any]:
    """Like `build_required_kwargs`, but also fills optional parameters.

    This exercises every declared option (required and optional) on an
    operation, not just the minimum needed to make a valid call.
    """
    sig = inspect.signature(method)
    kwargs: dict[str, Any] = {}
    for param in sig.parameters.values():
        if param.name == "self":
            continue
        if param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
            continue
        kwargs[param.name] = sample_value_for_annotation(param.annotation, param.name)
    return kwargs


@dataclass(frozen=True)
class RestCallMetadata:
    method: str
    expected_status: int
    error_cls_name: str
    operation_name: str


def parse_rest_call_metadata(
    rest_module: Any, function_name: str
) -> Optional[RestCallMetadata]:
    """Reads the `request_json(...)` call inside a generated REST function.

    `scripts/generate_sdk.py` writes `method`, `expected_status`, `error_cls`,
    and `operation_name` as literal keyword arguments into every generated
    operation, so they can be read back via AST instead of re-deriving them
    from the schema.
    """
    file_path = Path(inspect.getfile(rest_module))
    tree = ast.parse(file_path.read_text(encoding="utf-8"))

    for node in tree.body:
        if not (isinstance(node, ast.FunctionDef) and node.name == function_name):
            continue
        for sub in ast.walk(node):
            if not (
                isinstance(sub, ast.Call)
                and isinstance(sub.func, ast.Name)
                and sub.func.id == "request_json"
            ):
                continue
            method = None
            expected_status = None
            error_cls_name = None
            operation_name = None
            for kw in sub.keywords:
                if kw.arg == "method" and isinstance(kw.value, ast.Constant):
                    method = kw.value.value
                if kw.arg == "expected_status" and isinstance(kw.value, ast.Constant):
                    expected_status = kw.value.value
                if kw.arg == "error_cls" and isinstance(kw.value, ast.Name):
                    error_cls_name = kw.value.id
                if kw.arg == "operation_name" and isinstance(kw.value, ast.Constant):
                    operation_name = kw.value.value
            if None not in (method, expected_status, error_cls_name, operation_name):
                return RestCallMetadata(
                    method=method,
                    expected_status=expected_status,
                    error_cls_name=error_cls_name,
                    operation_name=operation_name,
                )
    return None


def error_module_for(rest_module: Any):
    """Imports the `error` package generated alongside a service's REST module."""
    parts = rest_module.__name__.split(".")
    service_pkg = ".".join(parts[:-2])
    return importlib.import_module(f"{service_pkg}.error")
