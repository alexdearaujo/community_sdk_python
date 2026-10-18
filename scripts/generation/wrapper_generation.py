# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
"""Client mixin and dual-transport service wrapper generation."""

import ast
import keyword
import re
from dataclasses import dataclass
from pathlib import Path

from google.api import annotations_pb2
from google.protobuf import descriptor_pb2

from ._shared import (
    PROJECT_ROOT,
    REGENERATE_COMMAND,
    SDK_OUTPUT_DIR,
    RestOperation,
    discover_service_model_classes,
    iter_service_dirs,
    parse_generated_rest_module,
    service_to_pascal_case,
    write_text_lf,
)
from .public_names import PublicNames, operation_key


@dataclass(frozen=True)
class GrpcMethod:
    """One RPC, as reached through the HTTP rule a REST operation shares with it."""

    stub_idx: str
    name: str
    request_class: str
    path_fields: tuple[str, ...]  # request field path per URL placeholder, in order
    body: str  # HTTP rule body: "" (none), "*" (whole request), or one field name
    update_mask_from: str = ""  # body field grpc-gateway derives update_mask from
    request_module: str = (
        ""  # google.protobuf module holding request_class; "" is the service's pb2
    )


GrpcRuleKey = tuple[str, str, str]  # (proto service, HTTP verb, normalized path)

_PLACEHOLDER = re.compile(r"\{([^}]*)\}")
# Well-known request types an RPC may take instead of its own message.
_WELL_KNOWN_REQUESTS = {".google.protobuf.Empty": ("empty_pb2", "Empty")}
# fixup aliases a shadowed typing name (TypingList); wrappers qualify models instead.
_TYPING_ALIAS = re.compile(
    r"\bTyping(Callable|Dict|List|Optional|Set|Tuple|Type|Union)\b"
)


def _normalize_path(path: str) -> str:
    # Placeholder names differ between the swagger and the proto: protoc-gen-openapiv2
    # renames GetDevice's {id} to {device.id} to match UpdateDevice on the same path.
    return _PLACEHOLDER.sub("{}", path)


def _file_descriptor(pb2_file: Path) -> descriptor_pb2.FileDescriptorProto | None:
    """Reads the descriptor protoc serialized into a _pb2 module, without importing it."""
    try:
        tree = ast.parse(pb2_file.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, ValueError):
        return None
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "AddSerializedFile"
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, bytes)
        ):
            return descriptor_pb2.FileDescriptorProto.FromString(node.args[0].value)
    return None


def _discover_grpc_methods(
    service_dir: Path,
) -> tuple[list[tuple[str, str, str, str]], dict[GrpcRuleKey, GrpcMethod]]:
    """Finds every RPC with an HTTP rule, keyed the way a REST operation can look it up.

    Keyed by proto service as well as path: Services such as alerting declare an
    RPC named `Delete` on several proto services, and only the REST module's own
    service is the right one.

    Returns:
      stubs_info: list of (pb2_stem, pb2_grpc_stem, stub_class_name, str_idx)
      methods: (proto service, HTTP verb, normalized path) -> GrpcMethod
    """
    pb_dir = service_dir / "pb"
    if not pb_dir.exists():
        return [], {}

    stubs_info: list[tuple[str, str, str, str]] = []
    methods: dict[GrpcRuleKey, GrpcMethod] = {}

    for pb2_file in sorted(pb_dir.glob("*_pb2.py")):
        pb2_grpc_stem = f"{pb2_file.stem}_grpc"
        fd = _file_descriptor(pb2_file)
        if fd is None or not (pb_dir / f"{pb2_grpc_stem}.py").exists():
            continue
        local_messages = {f".{fd.package}.{m.name}" for m in fd.message_type}
        messages = {m.name: m for m in fd.message_type}

        for service in fd.service:
            idx = str(len(stubs_info) + 1)
            stubs_info.append(
                (pb2_file.stem, pb2_grpc_stem, f"{service.name}Stub", idx)
            )
            for method in service.method:
                # call_grpc makes one unary call; a stream needs an iterator protocol.
                if method.client_streaming or method.server_streaming:
                    continue
                if method.input_type in _WELL_KNOWN_REQUESTS:
                    request_module, request_class = _WELL_KNOWN_REQUESTS[
                        method.input_type
                    ]
                elif method.input_type in local_messages:
                    request_module = ""
                    request_class = method.input_type.rsplit(".", 1)[1]
                else:
                    # The wrapper reaches request classes through this one module.
                    raise ValueError(
                        f"{service.name}.{method.name} takes {method.input_type}, "
                        f"which {pb2_file.name} does not define"
                    )
                rule = method.options.Extensions[annotations_pb2.http]  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]  # stubs type the handle loosely
                has_update_mask = not request_module and any(
                    field.name == "update_mask"
                    and field.type_name == ".google.protobuf.FieldMask"
                    for field in messages[request_class].field
                )
                for binding in (rule, *rule.additional_bindings):
                    verb = binding.WhichOneof("pattern")
                    if verb is None or verb == "custom":
                        continue
                    if binding.response_body:
                        # REST returns that one field, gRPC the whole message.
                        continue
                    template = getattr(binding, verb)
                    methods[(service.name, verb, _normalize_path(template))] = (
                        GrpcMethod(
                            stub_idx=idx,
                            name=method.name,
                            request_class=request_class,
                            path_fields=tuple(
                                p.split("=", 1)[0]
                                for p in _PLACEHOLDER.findall(template)
                            ),
                            body=binding.body,
                            # grpc-gateway's PATCH rule for a one-field body.
                            update_mask_from=binding.body
                            if verb == "patch"
                            and has_update_mask
                            and binding.body not in ("", "*")
                            else "",
                            request_module=request_module,
                        )
                    )

    return stubs_info, methods


def _grpc_request_fields(
    op: RestOperation, grpc_method: GrpcMethod
) -> list[tuple[str, str]]:
    """Pairs each path and query argument with the request field it sets.

    Mirrors grpc-gateway transcoding: a URL placeholder sets the field its HTTP
    rule names at that position, and a query parameter's wire name is its field
    path. Raises when an argument maps to nothing, rather than dropping it.
    """
    path_args = _PLACEHOLDER.findall(op.path)
    if len(path_args) != len(grpc_method.path_fields):
        raise ValueError(
            f"{op.name}: path {op.path} does not match the placeholders of "
            f"{grpc_method.name}'s HTTP rule {grpc_method.path_fields}"
        )
    fields = [*zip(grpc_method.path_fields, path_args), *op.query_params]
    unmapped = {name for name, _, _ in op.params} - {
        "api_config_override",
        "data",
        *(arg for _, arg in fields),
    }
    if unmapped:
        raise ValueError(f"{op.name}: no gRPC request field for {sorted(unmapped)}")
    return fields


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


def _to_snake_case(name: str) -> str:
    """Converts PascalCase/camelCase to snake_case.

    Acronym-aware: a run of capitals (AS, ASN, IP, ...) stays one word instead
    of splitting per letter (ListASGroups -> list_as_groups, not
    list_a_s_groups). Standard two-pass camel/Pascal -> snake conversion.
    """
    step1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    step2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", step1)
    return step2.lower()


def _drop_service_word(service: str, name: str) -> str:
    """Removes the Service's own word, because `client.<service>` already says it.

    `client.site.create_site` becomes `client.site.create`, `list_sites` becomes
    `list`, and `audit.get_audit_event` becomes `get_event`. A route suffix
    (`_by_...`) is never shortened.
    """
    head, sep, tail = name.partition("_by_")
    words = head.split("_")
    service_words = service.split("_")
    stem = re.sub(r"(ing|s)$", "", service_words[-1])
    for last in dict.fromkeys((service_words[-1], stem, stem + "s")):
        form = [*service_words[:-1], last]
        n = len(form)
        for i in range(len(words) - n + 1):
            if words[i : i + n] == form and len(words) > n:
                return "_".join(words[:i] + words[i + n :]) + sep + tail
    return name


def _wrapper_method_names(
    service: str,
    ops_by_file: dict[Path, list[RestOperation]],
) -> dict[tuple[Path, str], str]:
    """Names each wrapper method from its own operation, never from file order.

    A name declared by more than one REST module gets the module prefix in every
    module, so a bare name always means one operation and cannot move to another
    when a module is added. A second HTTP route of one operation is named by its
    extra path parameters (`get_event_by_ctime`), not by route order.
    """
    base_names: dict[tuple[Path, str], str] = {}
    for rest_file, ops in ops_by_file.items():
        routes: dict[str, list[RestOperation]] = {}
        for op in ops:
            # fixup suffixes a repeated operationId: GetAuditEvent, GetAuditEvent_2.
            base = re.sub(r"_\d+$", "", op.name)
            # protoc's default operationId is `<Module>_<Method>`; the Module is noise,
            # unless only one word is left (`RouteService_List` -> `route_list`).
            method = base.removeprefix(f"{rest_file.stem}_")
            if method != base:
                one_word = re.fullmatch(r"[A-Z][a-z0-9]*", method)
                base = (
                    rest_file.stem.removesuffix("Service") + method
                    if one_word
                    else method
                )
            routes.setdefault(base, []).append(op)
        for base, group in routes.items():
            fewest = min(len(_PLACEHOLDER.findall(op.path)) for op in group)
            shortest = [
                op for op in group if len(_PLACEHOLDER.findall(op.path)) == fewest
            ]
            if len(shortest) > 1:
                raise ValueError(
                    f"{rest_file.name}: routes of {base} have the same number of "
                    "path parameters, so none can keep the bare name"
                )
            known = set(_PLACEHOLDER.findall(shortest[0].path))
            for op in group:
                extra = [p for p in _PLACEHOLDER.findall(op.path) if p not in known]
                name = _to_snake_case(base)
                if extra:
                    name += "_by_" + "_".join(
                        re.sub(r"\W", "_", _to_snake_case(p)) for p in extra
                    )
                base_names[(rest_file, op.name)] = name

    declared_by: dict[str, set[Path]] = {}
    for (rest_file, _), name in base_names.items():
        declared_by.setdefault(name, set()).add(rest_file)

    long_names: dict[tuple[Path, str], str] = {}
    for (rest_file, op_name), name in base_names.items():
        if len(declared_by[name]) > 1:
            prefix = _to_snake_case(re.sub(r"Service$", "", rest_file.stem))
            name = f"{prefix}_{name}"
        long_names[(rest_file, op_name)] = name

    short = {op: _drop_service_word(service, n) for op, n in long_names.items()}
    # `create_device` and `create_devices` both shorten to `create`: keep both long.
    clashes = {n for n in short.values() if list(short.values()).count(n) > 1}
    names: dict[tuple[Path, str], str] = {}
    for op, name in short.items():
        name = long_names[op] if name in clashes else name
        # PEP 8: `Import` becomes `import_`, never the statement `def import(`.
        names[op] = name + "_" if keyword.iskeyword(name) else name

    duplicates = {n for n in names.values() if list(names.values()).count(n) > 1}
    if duplicates:
        raise ValueError(f"Wrapper method names are not unique: {sorted(duplicates)}")
    return names


def _public_method_names(
    service: str,
    ops_by_file: dict[Path, list[RestOperation]],
    names: PublicNames,
) -> dict[tuple[Path, str], str]:
    """Names each wrapper method from public_names.json; a new operation gets its default name."""
    defaults = _wrapper_method_names(service, ops_by_file)
    keys = {
        (rest_file, op.name): operation_key(op.http_method, op.path)
        for rest_file, ops in ops_by_file.items()
        for op in ops
    }
    if len(set(keys.values())) < len(keys):
        raise ValueError(f"{service}: two operations share one operation key")
    public = names.methods(service, {keys[op]: defaults[op] for op in sorted(keys)})
    return {op: public[key] for op, key in keys.items()}


def _rest_modules(service_dir: Path) -> list[Path]:
    """The generated REST modules of a Service (DeviceService.py, ...), sorted."""
    services_folder = service_dir / "services"
    if not services_folder.exists():
        services_folder = service_dir / "service"
    return [
        f
        for f in sorted(services_folder.glob("*.py"))
        if f.name != "__init__.py"
        and f.name != f"{service_dir.name}.py"
        and not f.name.startswith("async_")
        and f.stem.endswith("Service")
    ]


def public_method_names(
    service_dir: Path, names: PublicNames
) -> dict[tuple[Path, str], str]:
    """Maps each (REST module, function) of a Service to its client method name.

    Fails when public_names.json names a method the Service no longer has.
    """
    ops_by_file = {
        f: parse_generated_rest_module(f) for f in _rest_modules(service_dir)
    }
    return _public_method_names(service_dir.name, ops_by_file, names)


def _generate_service_wrappers(names: PublicNames):
    """Auto-generates the dual-transport wrapper classes for every service."""
    print("Generating unified service wrappers...")

    for service_dir in iter_service_dirs(SDK_OUTPUT_DIR):
        service = service_dir.name
        title = service_to_pascal_case(service)
        model_classes = discover_service_model_classes(service_dir)
        rest_files = _rest_modules(service_dir)
        method_names = public_method_names(service_dir, names)

        if not rest_files:
            print(
                f"    ⚠️ Could not find REST functions for {service}, skipping wrapper."
            )
            continue
        services_folder = rest_files[0].parent

        required_typing_symbols = {"Union", "cast"}

        # Discover gRPC stubs before building wrapper code.
        grpc_stubs_info, grpc_methods = _discover_grpc_methods(service_dir)

        wrapper_code = [
            "from typing import Union, cast",
            f"from kentik_api.gen.{service} import models as rest_models",
            "from kentik_api.core.api_config import APIConfig",
            "from kentik_api.transports.grpc_client import GrpcTransport",
            "from kentik_api.transports.rest_client import RestTransport",
            "",
            f"class {title}ServiceWrapper:",
            '    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().',
            f"    Rebuilt on every `{REGENERATE_COMMAND}`. Do not edit by hand.",
            "    Unified Service routing to either gRPC or REST.",
            '    """',
            "    def __init__(self, transport: Union[GrpcTransport, RestTransport]):",
            "        self._transport = transport",
            "        if isinstance(self._transport, GrpcTransport):",
        ]
        if grpc_stubs_info:
            for pb2_stem, pb2_grpc_stem, stub_class, stub_index_str in grpc_stubs_info:
                # try/except so missing proto deps degrade gracefully to NotImplementedError
                # rather than crashing at import time.
                wrapper_code.append("            try:")
                # __import__() instead of import statement: isort won't reorder it,
                # so this always runs before the service pb2 imports that depend on it.
                wrapper_code.append(
                    '                __import__("kentik_api.gen.pb_companions")'
                )
                wrapper_code.append(
                    f"                import kentik_api.gen.{service}.pb.{pb2_stem} as _pb2_{stub_index_str}_mod"
                )
                wrapper_code.append(
                    f"                import kentik_api.gen.{service}.pb.{pb2_grpc_stem} as _pb2_grpc_{stub_index_str}_mod"
                )
                wrapper_code.append(
                    f"                self._grpc_pb2_{stub_index_str} = _pb2_{stub_index_str}_mod"
                )
                wrapper_code.append(
                    f"                self._grpc_stub_{stub_index_str} = _pb2_grpc_{stub_index_str}_mod.{stub_class}(self._transport.channel)"
                )
                wrapper_code.append(
                    "            except (ImportError, TypeError) as exc:"
                )
                wrapper_code.append(
                    f"                self._grpc_pb2_{stub_index_str} = None"
                )
                wrapper_code.append(
                    f"                self._grpc_stub_{stub_index_str} = None"
                )
                # Kept for the call that fails: a descriptor-pool conflict is a
                # TypeError too, and a generic message would hide which one it was.
                wrapper_code.append(
                    f"                self._grpc_import_error_{stub_index_str} = exc"
                )
        else:
            wrapper_code.append(
                "            pass  # gRPC not yet implemented for this service"
            )
        wrapper_code.append("")

        # Insert REST module imports at the top of wrapper_code (before GrpcTransport).
        for idx, service_py in enumerate(rest_files, start=1):
            rest_module_name = service_py.stem  # e.g., 'DeviceService'
            module_alias = f"Rest{title}Module{idx}"
            wrapper_code.insert(
                2 + (idx - 1),
                f"import kentik_api.gen.{service}.{services_folder.name}.{rest_module_name} as {module_alias}",
            )

        # After REST imports are inserted, inject gRPC imports if stubs were found.
        grpc_runtime_symbols = {
            "build_grpc_request",
            "call_grpc",
            "parse_grpc_response",
        }
        well_known_modules: set[str] = set()
        grpc_import_idx = 0
        if grpc_stubs_info:
            rest_transport_line_idx = next(
                i
                for i, line in enumerate(wrapper_code)
                if "from kentik_api.transports.rest_client import RestTransport" in line
            )
            # pb2 modules are loaded lazily inside __init__ to avoid proto
            # descriptor errors at import time when googleapis-common-protos is
            # not installed. The import line is filled in once the methods are known.
            grpc_import_idx = rest_transport_line_idx + 1
            wrapper_code.insert(grpc_import_idx, "")

        ops_by_file = {f: parse_generated_rest_module(f) for f in rest_files}

        for idx, service_py in enumerate(rest_files, start=1):
            rest_module_name = service_py.stem
            module_alias = f"Rest{title}Module{idx}"

            for op in ops_by_file[service_py]:
                func_name_pascal = op.name
                return_type = qualify_wrapper_annotation_types(
                    op.return_type, model_classes
                )
                return_type = _TYPING_ALIAS.sub(r"\1", return_type)

                unique_method_name = method_names[(service_py, op.name)]

                # Build the wrapper signature: the REST params (their own
                # api_config_override is re-added below as keyword-only, so it
                # sits with the other options), with model types qualified.
                def _qualify_annotation(annotation: str) -> str:
                    return _TYPING_ALIAS.sub(
                        r"\1",
                        qualify_wrapper_annotation_types(annotation, model_classes),  # noqa: B023 - called only in this iteration
                    )

                pos_parts = [
                    f"{param_name}: {_qualify_annotation(annotation)}"
                    if is_required
                    else f"{param_name}: {_qualify_annotation(annotation)} = None"
                    for param_name, annotation, is_required in op.params[
                        : op.kwonly_start
                    ]
                    if param_name != "api_config_override"
                ]
                kw_parts = [
                    f"{param_name}: {_qualify_annotation(annotation)}"
                    if is_required
                    else f"{param_name}: {_qualify_annotation(annotation)} = None"
                    for param_name, annotation, is_required in op.params[
                        op.kwonly_start :
                    ]
                ]
                # A per-call override replaces the client's config for this call
                # only (FR-018 to FR-021); omitted, the client's config is used.
                kw_parts = [
                    "api_config_override: Optional[APIConfig] = None",
                    *kw_parts,
                ]
                sig_args = ", ".join(pos_parts + ["*"] + kw_parts)

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

                # Build the call_args from all param names (api_config_override excluded)
                arg_names = [param_name for param_name, _, _ in op.params]
                # A free-form request body is annotated Dict[str, Any], which has
                # no model_dump. Only Pydantic-model bodies get dumped.
                data_annotation = next(
                    (ann for name, ann, _ in op.params if name == "data"), ""
                )
                body_expr = (
                    "dict(data)"
                    if data_annotation.lstrip().lower().startswith("dict[")
                    else "data.model_dump(by_alias=True, exclude_unset=True)"
                )
                call_args = [
                    f"{arg}={arg}" for arg in arg_names if arg != "api_config_override"
                ]
                call_args_str = ", ".join(call_args)
                if call_args_str:
                    call_args_str = ", " + call_args_str

                # Build the gRPC branch: real call when an RPC shares this
                # operation's HTTP rule, otherwise the NotImplementedError placeholder.
                grpc_method = grpc_methods.get(
                    (rest_module_name, op.http_method, _normalize_path(op.path))
                )
                if grpc_method is not None:
                    stub_idx = grpc_method.stub_idx
                    is_none_return = return_type.strip() == "None"
                    request_fields = _grpc_request_fields(op, grpc_method)
                    if "data" not in arg_names:
                        body_arg = "None"
                    elif grpc_method.body in ("", "*"):
                        body_arg = body_expr
                    else:
                        body_arg = f'{{"{grpc_method.body}": {body_expr}}}'
                    fields_arg = ", ".join(
                        f'"{field}": {arg}' for field, arg in request_fields
                    )
                    mask_arg = (
                        f', update_mask_from="{grpc_method.update_mask_from}"'
                        if grpc_method.update_mask_from
                        else ""
                    )
                    if grpc_method.request_module:
                        well_known_modules.add(grpc_method.request_module)
                        request_ref = (
                            f"{grpc_method.request_module}.{grpc_method.request_class}"
                        )
                    else:
                        request_ref = (
                            f"self._grpc_pb2_{stub_idx}.{grpc_method.request_class}"
                        )
                    grpc_lines = [
                        "        if isinstance(self._transport, GrpcTransport):",
                        # Guard: if proto deps weren't available at init, fall back.
                        f"            if self._grpc_pb2_{stub_idx} is None or self._grpc_stub_{stub_idx} is None:",
                        f'                raise NotImplementedError(f"gRPC proto modules for {service} service failed to import: {{self._grpc_import_error_{stub_idx}!r}}") from self._grpc_import_error_{stub_idx}',
                        f"            _req = build_grpc_request({request_ref}, {body_arg}, {{{fields_arg}}}{mask_arg})",
                        (
                            f"            _resp, _rate_limit = call_grpc(self._grpc_stub_{stub_idx}.{grpc_method.name}, _req, "
                            f"api_config=api_config_override, error_cls={module_alias}.{op.error_cls_name})"
                        ),
                    ]
                    if is_none_return:
                        grpc_lines.append("            return None")
                    elif re.match(r"(Dict|dict)\[|Any$", return_type.strip()):
                        # REST returns a free-form body, such as google.protobuf.Empty's, as is.
                        grpc_runtime_symbols.add("grpc_response_body")
                        grpc_lines.append(
                            "            return grpc_response_body(_resp)"
                        )
                    else:
                        grpc_lines.append(
                            f"            return parse_grpc_response({return_type}, _resp, _rate_limit, "
                            f'stub_method=self._grpc_stub_{stub_idx}.{grpc_method.name}, operation_name="{func_name_pascal}")'
                        )
                else:
                    grpc_lines = [
                        "        if isinstance(self._transport, GrpcTransport):",
                        f'            raise NotImplementedError("gRPC translation for {func_name_pascal} is not yet implemented.")',
                    ]

                # Escape back to source: ast.get_docstring returned the runtime text.
                doc_source = op.docstring.replace("\\", "\\\\").replace(
                    '"""', '\\"\\"\\"'
                )
                doc_lines = (
                    [
                        '        """',
                        *(
                            f"        {line}".rstrip()
                            for line in doc_source.split("\n")
                        ),
                        '        """',
                    ]
                    if op.docstring
                    else []
                )

                wrapper_code.extend(
                    [
                        f"    def {unique_method_name}(self, {sig_args}) -> {return_type}:",
                        *doc_lines,
                        *grpc_lines,
                        "        elif isinstance(self._transport, RestTransport):",
                        "            rest_transport = cast(RestTransport, self._transport)",
                        f"            return {module_alias}.{func_name_pascal}(",
                        f"                api_config_override=api_config_override or rest_transport.api_config{call_args_str}",
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
        if grpc_stubs_info:
            wrapper_code[grpc_import_idx : grpc_import_idx + 1] = [
                "from kentik_api.core.grpc_runtime import "
                + ", ".join(sorted(grpc_runtime_symbols)),
                *(
                    f"from google.protobuf import {m}"
                    for m in sorted(well_known_modules)
                ),
            ]

        # Write to gen/<service>/services/<service>.py
        wrapper_file = services_folder / f"{service}.py"
        write_text_lf(wrapper_file, "\n".join(wrapper_code))


def _generate_client_mixin(rest_only: frozenset[str] = frozenset()):
    """Generates an IDE-friendly Mixin class that mounts all service wrappers.

    A REST-only service (from the local schema base) mounts on `_v5_transport`,
    a REST transport on the V5 host that every client has, whatever its protocol.
    """
    print("Generating IDE-Friendly Client Mixin...")

    imports = []
    type_hints = []
    mounts = []

    for service_dir in iter_service_dirs(SDK_OUTPUT_DIR):
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
        transport = "_v5_transport" if service in rest_only else "_transport"
        mounts.append(f"        self.{service} = {wrapper_class}(self.{transport})")

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
        '    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_client_mixin().',
        f"    Rebuilt on every `{REGENERATE_COMMAND}`. Do not edit by hand.",
        '    """',
        "",
        "    if TYPE_CHECKING:",
        "        _transport: 'GrpcTransport | RestTransport'",
        "        _v5_transport: 'RestTransport'",
        *type_hints,
        "",
        "    def _mount_generated_services(self) -> None:",
        '        """Mounts all generated service wrappers using the active transport."""',
        *mounts,
        "",
    ]

    mixin_file = PROJECT_ROOT / "src" / "kentik_api" / "client_mixin.py"
    write_text_lf(mixin_file, "\n".join(mixin_code))


def generate(names: PublicNames, rest_only: frozenset[str] = frozenset()) -> None:
    """Generates service wrappers, then the client mixin that mounts them."""
    _generate_service_wrappers(names)
    _generate_client_mixin(rest_only)
