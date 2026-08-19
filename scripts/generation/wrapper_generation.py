"""Client mixin and dual-transport service wrapper generation."""

import ast
import re
from pathlib import Path

from ._shared import (
    PROJECT_ROOT,
    SDK_OUTPUT_DIR,
    discover_service_model_classes,
    service_to_pascal_case,
)


def _discover_grpc_stubs(
    service_dir: Path, service: str
) -> tuple[list[tuple[str, str, str, str]], dict[str, tuple[int, str, str]]]:
    """AST-parses pb2_grpc files to build a map from gRPC method name to stub info.

    Returns:
      stubs_info: list of (pb2_stem, pb2_grpc_stem, stub_class_name, str_idx)
      method_map: method_name -> (stub_idx, req_class_name, resp_class_name)
    """
    pb_dir = service_dir / "pb"
    if not pb_dir.exists():
        return [], {}

    stubs_info: list[tuple[str, str, str, str]] = []
    method_map: dict[str, tuple[int, str, str]] = {}
    idx = 1

    for pb2_grpc_file in sorted(pb_dir.glob("*_pb2_grpc.py")):
        pb2_grpc_stem = pb2_grpc_file.stem  # e.g. "device_pb2_grpc"
        pb2_stem = pb2_grpc_stem[: -len("_grpc")]  # e.g. "device_pb2"
        try:
            tree = ast.parse(pb2_grpc_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        for cls in ast.walk(tree):
            if not (isinstance(cls, ast.ClassDef) and cls.name.endswith("Stub")):
                continue
            stub_class = cls.name
            stubs_info.append((pb2_stem, pb2_grpc_stem, stub_class, str(idx)))

            for fn in cls.body:
                if not (isinstance(fn, ast.FunctionDef) and fn.name == "__init__"):
                    continue
                for stmt in fn.body:
                    if not (
                        isinstance(stmt, ast.Assign)
                        and isinstance(stmt.targets[0], ast.Attribute)
                        and isinstance(stmt.value, ast.Call)
                    ):
                        continue
                    meth = stmt.targets[0].attr
                    req_cls = resp_cls = None
                    for kw in stmt.value.keywords:
                        parts = ast.unparse(kw.value).split(".")
                        if kw.arg == "request_serializer" and len(parts) >= 2:
                            req_cls = parts[-2]
                        if kw.arg == "response_deserializer" and len(parts) >= 2:
                            resp_cls = parts[-2]
                    if req_cls:
                        method_map[meth] = (
                            idx,
                            req_cls,
                            resp_cls or f"{meth}Response",
                        )
            idx += 1

    return stubs_info, method_map


def qualify_wrapper_annotation_types(text: str, model_classes: set[str]) -> str:
    """Qualifies model type names with rest_models in wrapper annotations."""
    if not model_classes:
        return text

    qualified = text
    for model_name in sorted(model_classes, key=len, reverse=True):
        qualified = re.sub(
            rf"(?<!\.)\b{re.escape(model_name)}\b",
            f"rest_models.{model_name}",
            qualified,
        )
    return qualified


def _generate_service_wrappers():
    """Auto-generates the dual-transport wrapper classes for every service."""
    print("Generating unified service wrappers...")

    def _to_snake_case(name: str) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

    for service_dir in SDK_OUTPUT_DIR.iterdir():
        if not service_dir.is_dir() or service_dir.name in (
            "__pycache__",
            "docs",
            "core",
            "pb",
        ):
            continue

        service = service_dir.name
        title = service_to_pascal_case(service)
        model_classes = discover_service_model_classes(service_dir)

        # 1. Dynamically find the services directory
        services_folder = service_dir / "services"
        if not services_folder.exists():
            services_folder = service_dir / "service"
            if not services_folder.exists():
                continue

        # 2. Collect generated REST service modules (e.g. DeviceService.py, SyntheticsAdminService.py)
        rest_files = [
            f
            for f in sorted(services_folder.glob("*.py"))
            if f.name != "__init__.py"
            and f.name != f"{service}.py"
            and not f.name.startswith("async_")
            and f.stem.endswith("Service")
        ]

        if not rest_files:
            print(
                f"    ⚠️ Could not find REST functions for {service}, skipping wrapper."
            )
            continue

        required_typing_symbols = {"Union", "cast"}

        # Discover gRPC stubs before building wrapper code.
        grpc_stubs_info, grpc_method_map = _discover_grpc_stubs(service_dir, service)

        wrapper_code = [
            "from typing import Union, cast",
            f"from kentik_api.gen.{service} import models as rest_models",
            "from kentik_api.transports.grpc_client import GrpcTransport",
            "from kentik_api.transports.rest_client import RestTransport",
            "",
            f"class {title}ServiceWrapper:",
            '    """Unified Service routing to either gRPC or REST."""',
            "    def __init__(self, transport: Union[GrpcTransport, RestTransport]):",
            "        self._transport = transport",
            "        if isinstance(self._transport, GrpcTransport):",
        ]
        if grpc_stubs_info:
            for pb2_stem, pb2_grpc_stem, stub_class, sidx in grpc_stubs_info:
                # try/except so missing proto deps degrade gracefully to NotImplementedError
                # rather than crashing at import time.
                wrapper_code.append("            try:")
                # __import__() instead of import statement: isort won't reorder it,
                # so this always runs before the service pb2 imports that depend on it.
                wrapper_code.append(
                    "                __import__(\"kentik_api.gen.pb_companions\")"
                )
                wrapper_code.append(
                    f"                import kentik_api.gen.{service}.pb.{pb2_stem} as _pb2_{sidx}_mod"
                )
                wrapper_code.append(
                    f"                import kentik_api.gen.{service}.pb.{pb2_grpc_stem} as _pb2_grpc_{sidx}_mod"
                )
                wrapper_code.append(
                    f"                self._grpc_pb2_{sidx} = _pb2_{sidx}_mod"
                )
                wrapper_code.append(
                    f"                self._grpc_stub_{sidx} = _pb2_grpc_{sidx}_mod.{stub_class}(self._transport.channel)"
                )
                wrapper_code.append("            except (ImportError, TypeError):")
                wrapper_code.append(
                    f"                self._grpc_pb2_{sidx} = None"
                )
                wrapper_code.append(
                    f"                self._grpc_stub_{sidx} = None"
                )
        else:
            wrapper_code.append("            pass  # gRPC not yet implemented for this service")
        wrapper_code.append("")

        emitted_method_names: set[str] = set()

        # Insert REST module imports at the top of wrapper_code (before GrpcTransport).
        for idx, service_py in enumerate(rest_files, start=1):
            rest_module_name = service_py.stem  # e.g., 'DeviceService'
            module_alias = f"Rest{title}Module{idx}"
            wrapper_code.insert(
                2 + (idx - 1),
                f"import kentik_api.gen.{service}.{services_folder.name}.{rest_module_name} as {module_alias}",
            )

        # After REST imports are inserted, inject gRPC imports if stubs were found.
        if grpc_stubs_info:
            rest_transport_line_idx = next(
                i
                for i, line in enumerate(wrapper_code)
                if "from kentik_api.transports.rest_client import RestTransport" in line
            )
            grpc_import_lines = [
                "from google.protobuf.json_format import MessageToDict, ParseDict",
                "from kentik_api.core.grpc_runtime import call_grpc",
            ]
            # Only json_format helpers go at module level; pb2 modules are loaded
            # lazily inside __init__ to avoid proto descriptor errors at import
            # time when googleapis-common-protos is not installed.
            for offset, imp_line in enumerate(grpc_import_lines):
                wrapper_code.insert(rest_transport_line_idx + 1 + offset, imp_line)

        for idx, service_py in enumerate(rest_files, start=1):
            rest_module_name = service_py.stem
            module_alias = f"Rest{title}Module{idx}"
            content = service_py.read_text(encoding="utf-8")
            func_pattern = re.compile(
                r"^def\s+([A-Z][a-zA-Z0-9_]*)\s*\((.*?)\)\s*->\s*([a-zA-Z0-9_\[\]\.]+):",
                re.MULTILINE | re.DOTALL,
            )

            for match in func_pattern.finditer(content):
                func_name_pascal = match.group(1)
                func_args_raw = match.group(2)
                return_type = match.group(3)

                # Convert PascalCase to snake_case (ListDevices -> list_devices)
                func_name_snake = _to_snake_case(func_name_pascal)

                # Keep wrapper method names unique across the full class.
                # If a collision occurs (e.g., many sub-services each define `List`),
                # prefix with module name and then add numeric suffixes if needed.
                unique_method_name = func_name_snake
                if unique_method_name in emitted_method_names:
                    module_prefix = _to_snake_case(
                        re.sub(r"Service$", "", rest_module_name)
                    )
                    unique_method_name = f"{module_prefix}_{func_name_snake}"
                    suffix = 2
                    while unique_method_name in emitted_method_names:
                        unique_method_name = (
                            f"{module_prefix}_{func_name_snake}_{suffix}"
                        )
                        suffix += 1

                emitted_method_names.add(func_name_snake)
                emitted_method_names.add(unique_method_name)

                # Clean up the signature for the wrapper (remove the api_config_override)
                sig_args = re.sub(
                    r"api_config_override:\s*Optional\[APIConfig\]\s*=\s*None,?\s*",
                    "",
                    func_args_raw,
                )
                sig_args = qualify_wrapper_annotation_types(sig_args, model_classes)
                return_type = qualify_wrapper_annotation_types(
                    return_type, model_classes
                )

                # Service modules may alias typing.List to TypingList to avoid
                # collisions with functions named `List`; wrappers should expose
                # standard List annotations.
                sig_args = re.sub(r"\bTypingList\b", "List", sig_args)
                return_type = re.sub(r"\bTypingList\b", "List", return_type)

                for typing_symbol in (
                    "Any",
                    "Optional",
                    "Dict",
                    "List",
                    "Tuple",
                    "Set",
                    "Literal",
                    "Callable",
                ):
                    if re.search(rf"\b{typing_symbol}\b", sig_args) or re.search(
                        rf"\b{typing_symbol}\b", return_type
                    ):
                        required_typing_symbols.add(typing_symbol)

                # Extract variable names to pass into the REST function call
                arg_names = re.findall(r"([a-zA-Z0-9_]+)\s*:", func_args_raw)
                call_args = [
                    f"{arg}={arg}" for arg in arg_names if arg != "api_config_override"
                ]

                call_args_str = ", ".join(call_args)
                if call_args_str:
                    call_args_str = ", " + call_args_str

                # Build the gRPC branch: real call when a matching stub exists,
                # otherwise keep the NotImplementedError placeholder.
                non_data_args = [
                    a for a in arg_names if a not in ("api_config_override", "data")
                ]
                if func_name_pascal in grpc_method_map:
                    stub_idx, req_class, resp_class = grpc_method_map[func_name_pascal]
                    is_none_return = return_type.strip() == "None"
                    # Guard: if proto deps weren't available at init, fall back.
                    stub_guard = [
                        "        if isinstance(self._transport, GrpcTransport):",
                        f"            if self._grpc_stub_{stub_idx} is None:",
                        f'                raise NotImplementedError("gRPC proto dependencies not installed for {service} service")',
                    ]
                    if "data" in arg_names and non_data_args:
                        # Body param + path/query params
                        other_dict = ", ".join(
                            f'"{a}": {a}' for a in non_data_args
                        )
                        grpc_lines = [
                            *stub_guard,
                            "            _req_dict = data.model_dump(by_alias=True, exclude_none=True)",
                            f"            _req_dict.update({{k: v for k, v in {{{other_dict}}}.items() if v is not None}})",
                            f"            _req = ParseDict(_req_dict, self._grpc_pb2_{stub_idx}.{req_class}(), ignore_unknown_fields=True)",
                            f"            _resp = call_grpc(self._grpc_stub_{stub_idx}.{func_name_pascal}, _req)",
                        ]
                    elif "data" in arg_names:
                        # Body param only
                        grpc_lines = [
                            *stub_guard,
                            f"            _req = ParseDict(data.model_dump(by_alias=True, exclude_none=True), self._grpc_pb2_{stub_idx}.{req_class}(), ignore_unknown_fields=True)",
                            f"            _resp = call_grpc(self._grpc_stub_{stub_idx}.{func_name_pascal}, _req)",
                        ]
                    elif non_data_args:
                        # Query/path params only
                        kwarg_dict = ", ".join(
                            f'"{a}": {a}' for a in non_data_args
                        )
                        grpc_lines = [
                            *stub_guard,
                            f"            _req = ParseDict({{k: v for k, v in {{{kwarg_dict}}}.items() if v is not None}}, self._grpc_pb2_{stub_idx}.{req_class}(), ignore_unknown_fields=True)",
                            f"            _resp = call_grpc(self._grpc_stub_{stub_idx}.{func_name_pascal}, _req)",
                        ]
                    else:
                        # No params
                        grpc_lines = [
                            *stub_guard,
                            f"            _req = self._grpc_pb2_{stub_idx}.{req_class}()",
                            f"            _resp = call_grpc(self._grpc_stub_{stub_idx}.{func_name_pascal}, _req)",
                        ]
                    if is_none_return:
                        grpc_lines.append("            return None")
                    else:
                        grpc_lines.append(
                            f"            return {return_type}.model_validate(MessageToDict(_resp))"
                        )
                else:
                    grpc_lines = [
                        "        if isinstance(self._transport, GrpcTransport):",
                        f'            raise NotImplementedError("gRPC translation for {func_name_pascal} is not yet implemented.")',
                    ]

                wrapper_code.extend(
                    [
                        f"    def {unique_method_name}(self, {sig_args}) -> {return_type}:",
                        *grpc_lines,
                        "        elif isinstance(self._transport, RestTransport):",
                        "            rest_transport = cast(RestTransport, self._transport)",
                        f"            return {module_alias}.{func_name_pascal}(",
                        f"                api_config_override=rest_transport.api_config{call_args_str}",
                        "            )",
                        "        else:",
                        '            raise TypeError(f"Unsupported transport type: {self._transport.__class__.__name__}")',
                        "",
                    ]
                )

        preferred_order = [
            "Union",
            "cast",
            "Any",
            "Optional",
            "Dict",
            "List",
            "Tuple",
            "Set",
            "Literal",
            "Callable",
        ]
        ordered_symbols = [
            symbol for symbol in preferred_order if symbol in required_typing_symbols
        ]
        wrapper_code[0] = f"from typing import {', '.join(ordered_symbols)}"

        # Write to gen/<service>/services/<service>.py
        wrapper_file = services_folder / f"{service}.py"
        wrapper_file.write_text("\n".join(wrapper_code), encoding="utf-8")


def _generate_client_mixin():
    """Generates an IDE-friendly Mixin class that mounts all service wrappers."""
    print("Generating IDE-Friendly Client Mixin...")

    imports = []
    type_hints = []
    mounts = []

    for service_dir in sorted(SDK_OUTPUT_DIR.iterdir()):
        if not service_dir.is_dir() or service_dir.name in (
            "__pycache__",
            "docs",
            "core",
            "pb",
        ):
            continue

        service = service_dir.name
        services_folder = service_dir / "services"
        if not services_folder.exists():
            services_folder = service_dir / "service"
            if not services_folder.exists():
                continue

        wrapper_file = services_folder / f"{service}.py"
        if not wrapper_file.exists():
            continue

        title = service_to_pascal_case(service)
        wrapper_class = f"{title}ServiceWrapper"

        # 1. Setup the import from the encapsulated gen directory
        imports.append(
            f"from kentik_api.gen.{service}.{services_folder.name}.{service} import {wrapper_class}"
        )

        # 2. Setup the IDE type hint
        type_hints.append(f"        {service}: '{wrapper_class}'")

        # 3. Setup the runtime mounting logic
        mounts.append(f"        self.{service} = {wrapper_class}(self._transport)")

    mixin_code = [
        "from typing import TYPE_CHECKING",
        "",
        *imports,
        "",
        "if TYPE_CHECKING:",
        "    from kentik_api.transports.grpc_client import GrpcTransport",
        "    from kentik_api.transports.rest_client import RestTransport",
        "",
        "class KentikClientMixin:",
        '    """Auto-generated Mixin to wire up all service wrappers to the main client."""',
        "",
        "    if TYPE_CHECKING:",
        "        _transport: 'GrpcTransport | RestTransport'",
        *type_hints,
        "",
        "    def _mount_generated_services(self) -> None:",
        '        """Mounts all generated service wrappers using the active transport."""',
        *mounts,
        "",
    ]

    mixin_file = PROJECT_ROOT / "src" / "kentik_api" / "client_mixin.py"
    mixin_file.write_text("\n".join(mixin_code), encoding="utf-8")


def generate() -> None:
    """Generates service wrappers, then the client mixin that mounts them."""
    _generate_service_wrappers()
    _generate_client_mixin()
