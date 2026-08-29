# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Constants and helpers used by more than one generation phase module."""

import ast
import re
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
SDK_OUTPUT_DIR = PROJECT_ROOT / "src" / "kentik_api" / "gen"

# Directories under gen/ that the generator creates for itself rather than
# deriving from a schema Service. pb_companions is written by
# _compile_proto_companions(); it holds shared proto descriptors, not an API.
INTERNAL_GEN_DIRS = frozenset({"__pycache__", "pb_companions"})


def iter_service_dirs(root: Path | None = None) -> list[Path]:
    """Returns every generated Service directory under root, sorted by name.

    The one place that answers "is this directory a Service". A Service with no
    operations still counts: six exist today with models but no wrapper, and
    five of them are documented, so absence of a wrapper must not reclassify one
    as internal. Callers needing a wrapper should check for it separately.

    root resolves at call time, not at import time, so a caller that overrides
    its own SDK_OUTPUT_DIR (as the generator tests do) is honoured.
    """
    root = SDK_OUTPUT_DIR if root is None else root
    if not root.exists():
        return []
    return sorted(
        (p for p in root.iterdir() if p.is_dir() and p.name not in INTERNAL_GEN_DIRS),
        key=lambda p: p.name,
    )


def service_to_pascal_case(service: str) -> str:
    """Converts a snake_case service name to PascalCase."""
    return "".join(part.capitalize() for part in service.split("_") if part)


def discover_service_model_classes(service_dir: Path) -> set[str]:
    """Collects model class names generated for a service."""
    model_classes: set[str] = set()

    files_to_scan = (
        list((service_dir / "models").rglob("*.py"))
        if (service_dir / "models").exists()
        else []
    )
    if (service_dir / "models.py").exists():
        files_to_scan.append(service_dir / "models.py")

    for model_file in files_to_scan:
        model_classes.update(
            re.findall(
                r"^class ([A-Za-z0-9_]+)[\(:]", model_file.read_text(), re.MULTILINE
            )
        )

    return model_classes


@dataclass(frozen=True)
class RestOperation:
    """Parsed representation of one operation from a generated REST service module.

    Consumers:
    - tests/_discovery.py: uses http_method, expected_status, error_cls_name, operation_name
    - generation/endpoint_docs.py: uses http_method, path
    - generation/wrapper_generation.py: uses name, params, kwonly_start, return_type
    """

    name: str  # PascalCase function name
    http_method: str  # as written in source (e.g. "get", "post")
    path: str  # URL path template
    expected_status: int
    error_cls_name: str
    operation_name: str
    params: tuple[
        tuple[str, str, bool], ...
    ]  # (name, annotation, is_required) positional then kwonly
    kwonly_start: int  # params[:kwonly_start] are positional; the rest are keyword-only
    return_type: str  # annotation text as-is from the source


def parse_generated_rest_module(path: Path) -> list[RestOperation]:
    """AST-parses a generated REST service module, returning one RestOperation per PascalCase function.

    Replaces three independent re-implementations in _discovery.py, endpoint_docs.py,
    and wrapper_generation.py. Skips functions without a request_json() call.
    """
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception:
        return []

    ops: list[RestOperation] = []
    for node in tree.body:
        if not (isinstance(node, ast.FunctionDef) and node.name[:1].isupper()):
            continue

        return_type = ast.unparse(node.returns) if node.returns else ""

        defaults_start = len(node.args.args) - len(node.args.defaults)
        positional: list[tuple[str, str, bool]] = [
            (
                arg.arg,
                ast.unparse(arg.annotation) if arg.annotation else "Any",
                i < defaults_start,
            )
            for i, arg in enumerate(node.args.args)
        ]
        kwonly: list[tuple[str, str, bool]] = [
            (
                arg.arg,
                ast.unparse(arg.annotation) if arg.annotation else "Any",
                default is None,
            )
            for arg, default in zip(node.args.kwonlyargs, node.args.kw_defaults)
        ]

        # Extract request_json() keyword arguments.
        http_method: str | None = None
        path_val: str | None = None
        expected_status = 0
        error_cls_name = ""
        operation_name = ""

        for sub in ast.walk(node):
            if not (
                isinstance(sub, ast.Call)
                and isinstance(sub.func, ast.Name)
                and sub.func.id == "request_json"
            ):
                continue
            for kw in sub.keywords:
                if kw.arg == "method" and isinstance(kw.value, ast.Constant):
                    http_method = str(kw.value.value)
                elif kw.arg == "path":
                    if isinstance(kw.value, ast.Constant):
                        path_val = str(kw.value.value)
                    elif isinstance(kw.value, ast.JoinedStr):
                        parts: list[str] = []
                        for part in kw.value.values:
                            if isinstance(part, ast.Constant):
                                parts.append(str(part.value))
                            elif isinstance(part, ast.FormattedValue):
                                parts.append(f"{{{ast.unparse(part.value)}}}")
                        path_val = "".join(parts)
                elif (
                    kw.arg == "expected_status"
                    and isinstance(kw.value, ast.Constant)
                    and isinstance(kw.value.value, int)
                ):
                    expected_status = kw.value.value
                elif kw.arg == "error_cls" and isinstance(kw.value, ast.Name):
                    error_cls_name = kw.value.id
                elif kw.arg == "operation_name" and isinstance(kw.value, ast.Constant):
                    operation_name = str(kw.value.value)
            break  # one request_json call per operation

        if http_method is None or path_val is None:
            continue  # helper function without a request_json call

        ops.append(
            RestOperation(
                name=node.name,
                http_method=http_method,
                path=path_val,
                expected_status=expected_status,
                error_cls_name=error_cls_name,
                operation_name=operation_name or node.name,
                params=tuple(positional + kwonly),
                kwonly_start=len(positional),
                return_type=return_type,
            )
        )

    return ops


@dataclass(frozen=True)
class WrapperMethod:
    """Parsed representation of one method from a generated *ServiceWrapper class.

    Consumers:
    - generation/docs_rendering.py: uses name, params, return_type, has_data_param
    - generation/endpoint_docs.py: uses name, params, kwonly_start for required flags
    """

    name: str
    params: tuple[
        tuple[str, str, bool], ...
    ]  # (name, annotation, is_required) positional then kwonly
    kwonly_start: int
    return_type: str
    has_data_param: bool  # True if any kwonly param is named "data"


def parse_wrapper_methods(path: Path) -> list[WrapperMethod]:
    """AST-parses a *ServiceWrapper file and returns one WrapperMethod per public method.

    Skips __init__ and any method starting with '_'. Symmetric with
    parse_generated_rest_module for REST service files.
    """
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception:
        return []

    wrapper_class: ast.ClassDef | None = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name.endswith("ServiceWrapper"):
            wrapper_class = node
            break
    if wrapper_class is None:
        return []

    methods: list[WrapperMethod] = []
    for node in wrapper_class.body:
        if not isinstance(node, ast.FunctionDef) or node.name.startswith("_"):
            continue

        return_type = ast.unparse(node.returns) if node.returns else ""

        defaults_start = len(node.args.args) - len(node.args.defaults)
        positional: list[tuple[str, str, bool]] = [
            (
                arg.arg,
                ast.unparse(arg.annotation) if arg.annotation else "Any",
                i < defaults_start,
            )
            for i, arg in enumerate(node.args.args)
            if arg.arg != "self"
        ]
        kwonly: list[tuple[str, str, bool]] = [
            (
                arg.arg,
                ast.unparse(arg.annotation) if arg.annotation else "Any",
                default is None,
            )
            for arg, default in zip(node.args.kwonlyargs, node.args.kw_defaults)
        ]
        all_params = tuple(positional + kwonly)
        has_data = any(name == "data" for name, _, _ in all_params)

        methods.append(
            WrapperMethod(
                name=node.name,
                params=all_params,
                kwonly_start=len(positional),
                return_type=return_type,
                has_data_param=has_data,
            )
        )

    return methods
