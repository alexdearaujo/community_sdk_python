# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Per-endpoint documentation: extracted from swagger while the schema is available,
rendered as Sphinx MyST stubs later, once wrapper method signatures exist.

EndpointDocsCollector accumulates the extract() results across the
schema-availability loop. It does not enforce the two-phase ordering:
render() reads wrapper signatures off disk, so it must run after service
wrapper generation, and that remains the caller's responsibility.
"""

import ast
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from types import FunctionType

from ._shared import (
    PROJECT_ROOT,
    discover_service_model_classes,
    iter_service_dirs,
    parse_wrapper_methods,
)

MD_FENCE = "`" * 3


def _provenance(writer: FunctionType) -> str:
    """Builds the AUTO-GENERATED header naming the code that wrote the file.

    Derived from the writer rather than typed out, so renaming it cannot leave
    the header pointing at a function that no longer exists.
    """
    module_path = Path(sys.modules[writer.__module__].__file__ or "").resolve()
    try:
        rel = module_path.relative_to(PROJECT_ROOT)
    except ValueError:
        rel = Path(module_path.name)
    return f"<!-- AUTO-GENERATED: {rel.as_posix()}, {writer.__name__}() -->"


@dataclass(frozen=True)
class EndpointParam:
    name: str
    location: str
    type_label: str
    required: bool


@dataclass(frozen=True)
class EndpointResponse:
    status: str
    description: str
    type_label: str


@dataclass(frozen=True)
class EndpointDoc:
    tag: str
    method: str
    path: str
    operation_id: str
    summary: str
    description: str
    parameters: list[EndpointParam]
    request_body: EndpointParam | None
    responses: list[EndpointResponse]


def _schema_type_label(schema: object) -> str:
    """Renders a short, human-readable type label for an OpenAPI schema object."""
    if not isinstance(schema, dict):
        return "-"
    ref = schema.get("$ref")
    if isinstance(ref, str) and ref:
        return ref.rsplit("/", 1)[-1]
    if schema.get("type") == "array":
        return f"{_schema_type_label(schema.get('items'))}[]"
    schema_type = schema.get("type")
    if isinstance(schema_type, str) and schema_type:
        fmt = schema.get("format")
        return f"{schema_type} ({fmt})" if isinstance(fmt, str) and fmt else schema_type
    return "object"


def extract_endpoint_docs(swagger_path: Path) -> list[EndpointDoc]:
    """Extracts per-operation documentation (params, every response) from a swagger file.

    Unlike collect_operation_error_responses (which only looks at non-2xx
    responses, for error-class generation), this captures every declared
    response so it can be rendered as real Sphinx text -- tables and a
    generated usage example -- instead of a rendered diagram image.
    """
    with open(swagger_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    tags_raw = schema.get("tags") if isinstance(schema.get("tags"), list) else []
    default_tag = None
    for tag in tags_raw:
        if isinstance(tag, dict) and tag.get("name"):
            default_tag = str(tag["name"]).strip()
            break

    paths_obj = schema.get("paths") if isinstance(schema.get("paths"), dict) else {}
    method_order = ["get", "post", "put", "patch", "delete", "options", "head", "trace"]

    docs: list[EndpointDoc] = []
    for endpoint, methods in sorted(paths_obj.items(), key=lambda item: item[0]):
        if not isinstance(methods, dict):
            continue
        for method in method_order:
            op = methods.get(method)
            if not isinstance(op, dict):
                continue

            op_tags_raw = op.get("tags")
            op_tags = op_tags_raw if isinstance(op_tags_raw, list) else []
            tag = next(
                (
                    str(item).strip()
                    for item in op_tags
                    if isinstance(item, str) and str(item).strip()
                ),
                default_tag or "default",
            )

            parameters: list[EndpointParam] = []
            for param in op.get("parameters") or []:
                if not isinstance(param, dict):
                    continue
                parameters.append(
                    EndpointParam(
                        name=str(param.get("name") or "-"),
                        location=str(param.get("in") or "-"),
                        type_label=_schema_type_label(param.get("schema")),
                        required=bool(param.get("required", False)),
                    )
                )

            request_body: EndpointParam | None = None
            body = op.get("requestBody")
            if isinstance(body, dict):
                content = body.get("content", {})
                json_content = (
                    content.get("application/json", {})
                    if isinstance(content, dict)
                    else {}
                )
                request_body = EndpointParam(
                    name="data",
                    location="body",
                    type_label=_schema_type_label(
                        json_content.get("schema")
                        if isinstance(json_content, dict)
                        else None
                    ),
                    required=bool(body.get("required", False)),
                )

            responses: list[EndpointResponse] = []
            responses_obj = op.get("responses")
            if isinstance(responses_obj, dict):
                for status, resp in sorted(responses_obj.items()):
                    if not isinstance(resp, dict):
                        continue
                    content = resp.get("content", {})
                    json_content = (
                        content.get("application/json", {})
                        if isinstance(content, dict)
                        else {}
                    )
                    responses.append(
                        EndpointResponse(
                            status=str(status),
                            description=str(resp.get("description") or "-"),
                            type_label=_schema_type_label(
                                json_content.get("schema")
                                if isinstance(json_content, dict)
                                else None
                            ),
                        )
                    )

            docs.append(
                EndpointDoc(
                    tag=tag,
                    method=method.upper(),
                    path=str(endpoint),
                    operation_id=str(op.get("operationId") or "-"),
                    summary=str(op.get("summary") or ""),
                    description=str(op.get("description") or ""),
                    parameters=parameters,
                    request_body=request_body,
                    responses=responses,
                )
            )

    return docs


def _md_cell(value: str) -> str:
    """Escapes text for safe use inside a single Markdown table cell."""
    text = re.sub(r"\s+", " ", str(value)).strip()
    return text.replace("|", "\\|") or "-"


def _normalize_path_for_matching(path: str) -> str:
    """Strips dots from path-parameter placeholders (`{device.id}` -> `{deviceid}`)
    so a raw-schema path and its generated-code path template compare equal."""
    return re.sub(r"\{([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)\}", r"{\1\2}", path)


def _rest_function_path_and_method(
    rest_file: Path, function_name: str
) -> tuple[str, str] | None:
    """Returns (HTTP_METHOD_UPPER, path) for a named function in a generated REST module."""
    from ._shared import parse_generated_rest_module

    for op in parse_generated_rest_module(rest_file):
        if op.name == function_name:
            return op.http_method.upper(), op.path
    return None


def parse_wrapper_method_signatures(
    wrapper_file: Path,
) -> dict[tuple[str, str], tuple[str, list[tuple[str, str, bool]]]]:
    """Maps (http_method, normalized_path) -> (wrapper_method_name, params).

    Keyed by method+path rather than operationId: multi-swagger-file
    services legitimately reuse generic operationIds like "List"/"Get"
    across different underlying REST modules (e.g. alerting's AlertService
    and SuppressionService both declare an operationId of exactly "List"),
    so operationId alone can't disambiguate which wrapper method an
    EndpointDoc (extracted straight from one swagger file) corresponds to.
    Method+path is guaranteed unique -- OpenAPI forbids two operations
    sharing both within one merged service.

    Reads the actual generated ServiceWrapper class and its underlying REST
    module (via AST, no import/execution) so example snippets always match
    the real, callable signature -- including flattened nested-object
    parameter names like `pagination.limit` -> `paginationlimit` that only
    exist post-generation.
    """
    # params come from the shared parser; only the REST-alias resolution is specific here.
    method_params = {
        m.name: list(m.params) for m in parse_wrapper_methods(wrapper_file)
    }
    if not method_params:
        return {}

    try:
        tree = ast.parse(wrapper_file.read_text(encoding="utf-8"))
    except Exception:
        return {}

    services_folder = wrapper_file.parent

    module_alias_to_file: dict[str, Path] = {}
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if not alias.asname or "." not in alias.name:
                    continue
                candidate = services_folder / f"{alias.name.rsplit('.', 1)[-1]}.py"
                if candidate.exists():
                    module_alias_to_file[alias.asname] = candidate

    wrapper_class = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name.endswith("ServiceWrapper"):
            wrapper_class = node
            break
    if wrapper_class is None:
        return {}

    mapping: dict[tuple[str, str], tuple[str, list[tuple[str, str, bool]]]] = {}
    for node in wrapper_class.body:
        if not isinstance(node, ast.FunctionDef) or node.name == "__init__":
            continue

        params = method_params.get(node.name)
        if params is None:
            continue

        rest_alias: str | None = None
        operation_id: str | None = None
        for sub in ast.walk(node):
            if (
                isinstance(sub, ast.Return)
                and isinstance(sub.value, ast.Call)
                and isinstance(sub.value.func, ast.Attribute)
                and isinstance(sub.value.func.value, ast.Name)
                and sub.value.func.value.id.startswith("Rest")
            ):
                rest_alias = sub.value.func.value.id
                operation_id = sub.value.func.attr
                break
        if rest_alias is None or operation_id is None:
            continue

        rest_file = module_alias_to_file.get(rest_alias)
        if rest_file is None:
            continue
        metadata = _rest_function_path_and_method(rest_file, operation_id)
        if metadata is None:
            continue
        http_method, path_template = metadata

        mapping[(http_method, _normalize_path_for_matching(path_template))] = (
            node.name,
            params,
        )

    return mapping


def _example_value_for_annotation(annotation_text: str, name: str) -> str:
    """Builds a plausible Python source snippet for a parameter's example value."""
    text = annotation_text.strip()
    if text.startswith("Optional[") and text.endswith("]"):
        text = text[len("Optional[") : -1].strip()
    for list_prefix in ("List[", "list["):
        if text.startswith(list_prefix) and text.endswith("]"):
            inner = text[len(list_prefix) : -1].strip()
            return f"[{_example_value_for_annotation(inner, name)}]"

    if text == "str":
        return f'"{name}-example"'
    if text == "int":
        return "1"
    if text == "float":
        return "1.0"
    if text == "bool":
        return "True"
    if text == "bytes":
        return 'b"example"'
    if text in ("Any", ""):
        return "..."

    # Anything else is a model reference (e.g. rest_models.CreateASGroupRequest).
    class_name = text.rsplit(".", 1)[-1]
    return f"{class_name}(...)"


def _render_example_snippet(
    service: str, method_name: str, params: list[tuple[str, str, bool]]
) -> str:
    """Renders a runnable-looking usage example from a real wrapper method signature."""
    required_params = [p for p in params if p[2]]
    lines = [
        "from kentik_api.client import KentikAPI",
        "",
        '# Both transports work: protocol="rest" (default) or protocol="grpc".',
        'client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env',
    ]
    if required_params:
        lines.append(f"response = client.{service}.{method_name}(")
        for param_name, annotation_text, _ in required_params:
            lines.append(
                f"    {param_name}={_example_value_for_annotation(annotation_text, param_name)},"
            )
        lines.append(")")
    else:
        lines.append(f"response = client.{service}.{method_name}()")
    return "\n".join(lines)


def _render_operation_sequence_diagram(
    service: str,
    doc: EndpointDoc,
    method_name: str,
    params: list[tuple[str, str, bool]],
) -> list[str]:
    """Renders REST and gRPC sequence diagrams side by side for one operation."""
    req_params = [(p, t) for p, t, r in params if r]
    if req_params:
        call_args = ", ".join(
            f"{p}={_example_value_for_annotation(t, p)}" for p, t in req_params
        )
    else:
        call_args = ""

    success_resp = next((r for r in doc.responses if r.status.startswith("2")), None)
    success_model = success_resp.type_label if success_resp else "response"

    # gRPC request class follows the convention {OperationId}Request where OperationId
    # comes from the HTTP method + path, so we derive it from the swagger operationId.
    grpc_req_class = (
        f"{doc.operation_id}Request" if doc.operation_id != "-" else "Request"
    )

    rest_diagram = [
        "**REST transport**",
        "",
        f"{MD_FENCE}mermaid",
        "sequenceDiagram",
        "    participant C as Caller",
        f"    participant W as client.{service}",
        "    participant API as Kentik REST API",
        "",
        f"    C->>W: {method_name}({call_args})",
        f"    W->>API: {doc.method} {doc.path}",
        "    alt success",
        f"        API-->>W: {success_model} (JSON)",
        f"        W-->>C: {success_model}",
        "    else error",
        "        API-->>W: error body",
        "        W-->>C: raise HTTPException",
        "    end",
        MD_FENCE,
        "",
    ]

    grpc_diagram = [
        "**gRPC transport**",
        "",
        f"{MD_FENCE}mermaid",
        "sequenceDiagram",
        "    participant C as Caller",
        f"    participant W as client.{service}",
        "    participant B as proto bridge",
        "    participant API as Kentik gRPC API",
        "",
        f"    C->>W: {method_name}({call_args})",
        f"    W->>B: ParseDict(params, {grpc_req_class})",
        f"    B->>API: {method_name} (gRPC/TLS)",
        "    alt success",
        f"        API-->>B: {success_model} proto",
        "        B-->>W: MessageToDict(response)",
        f"        W-->>C: {success_model}",
        "    else gRPC error",
        "        API-->>B: gRPC status + details",
        "        B-->>W: raise HTTPException",
        "        W-->>C: raise HTTPException",
        "    end",
        MD_FENCE,
        "",
    ]

    return rest_diagram + grpc_diagram


def _render_endpoint_section(
    service: str,
    doc: EndpointDoc,
    wrapper_signatures: dict[tuple[str, str], tuple[str, list[tuple[str, str, bool]]]],
    heading_level: int = 4,
) -> list[str]:
    heading = "#" * heading_level
    sub_heading = "#" * (heading_level + 1)

    # Resolve the wrapper signature early so we can use it for the sequence
    # diagram, which appears before the parameter/response detail tables.
    signature = wrapper_signatures.get(
        (doc.method, _normalize_path_for_matching(doc.path))
    )
    method_name, params = signature if signature else (None, [])

    lines = [f"{heading} `{doc.method}` `{doc.path}`", ""]
    if doc.summary:
        lines.extend([doc.summary, ""])
    if doc.description and doc.description != doc.summary:
        lines.extend([doc.description, ""])

    # Sequence diagram gives the reader a visual of the full call path
    # before they read the parameter/response detail tables.
    if method_name is not None:
        lines.extend(
            _render_operation_sequence_diagram(service, doc, method_name, params)
        )

    all_params = list(doc.parameters)
    if doc.request_body:
        all_params.append(doc.request_body)

    if all_params:
        lines.extend(
            [
                f"{sub_heading} Parameters",
                "",
                "| Name | In | Type | Required |",
                "| --- | --- | --- | --- |",
            ]
        )
        for param in all_params:
            # Generated wrapper methods flatten dotted nested-object params
            # (e.g. schema `asGroup.id` -> kwarg `asGroupid`); show the name
            # callers actually type, matching the example below.
            display_name = param.name.replace(".", "")
            lines.append(
                f"| `{_md_cell(display_name)}` | {_md_cell(param.location)} | "
                f"`{_md_cell(param.type_label)}` | {'Yes' if param.required else 'No'} |"
            )
        lines.append("")

    if doc.responses:
        lines.extend(
            [
                f"{sub_heading} Responses",
                "",
                "| Status | Description | Model |",
                "| --- | --- | --- |",
            ]
        )
        for resp in doc.responses:
            lines.append(
                f"| {_md_cell(resp.status)} | {_md_cell(resp.description)} | "
                f"`{_md_cell(resp.type_label)}` |"
            )
        lines.append("")

    if method_name is not None:
        lines.extend(
            [
                f"{sub_heading} Example",
                "",
                f"{MD_FENCE}python",
                _render_example_snippet(service, method_name, params),
                MD_FENCE,
                "",
            ]
        )

    return lines


def _autodoc_directive_for_model(models_dir: Path, class_name: str) -> str:
    """Picks the right autodoc directive for a generated model class.

    Most generated classes are Pydantic BaseModel subclasses, which
    sphinxcontrib.autodoc_pydantic renders beautifully via
    `autopydantic_model`. But OpenAPI enum schemas generate plain
    `class X(str, Enum)` classes -- feeding those into autopydantic_model
    crashes the Sphinx build (it assumes `__pydantic_decorators__` exists),
    so they need the standard `autoclass` directive instead.
    """
    model_file = models_dir / f"{class_name}.py"
    try:
        tree = ast.parse(model_file.read_text(encoding="utf-8"))
    except Exception:
        return "autopydantic_model"

    for node in tree.body:
        if not (isinstance(node, ast.ClassDef) and node.name == class_name):
            continue
        for base in node.bases:
            base_name = ast.unparse(base)
            if base_name.rsplit(".", 1)[-1] == "BaseModel":
                return "autopydantic_model"
        return "autoclass"

    return "autopydantic_model"


def _model_reference_edges(
    models_dir: Path, model_classes: list[str]
) -> dict[str, set[str]]:
    """Maps each model to the sibling models it names in a field annotation.

    Parses annotations statically (no import) and matches sibling class names
    by word boundary, so `Optional[List[FooConfig]]` yields an edge to
    `FooConfig` when `FooConfig` is another model in the same service.
    """
    names = set(model_classes)
    edges: dict[str, set[str]] = {}
    for cls in model_classes:
        refs: set[str] = set()
        try:
            tree = ast.parse((models_dir / f"{cls}.py").read_text(encoding="utf-8"))
        except Exception:
            edges[cls] = refs
            continue
        for node in ast.walk(tree):
            annotation = getattr(node, "annotation", None)
            if annotation is None:
                continue
            text = ast.unparse(annotation)
            for other in names:
                if other != cls and re.search(rf"\b{re.escape(other)}\b", text):
                    refs.add(other)
        edges[cls] = refs
    return edges


# Cap the model class diagram so dense services (e.g. alerting's 185 models)
# stay legible and don't overwhelm the browser-side Mermaid renderer.
_MODEL_DIAGRAM_MAX_NODES = 30


def _render_model_relationship_diagram(
    endpoint_docs: list[EndpointDoc],
    models_dir: Path,
    model_classes: list[str],
) -> list[str]:
    """Renders a collapsible Mermaid classDiagram of the service's model graph.

    Focuses on the public surface -- the request/response models the operations
    use, plus the models they directly reference -- and falls back to the
    service's own models for schema-only services. Caps the node count so dense
    services stay readable.
    """
    if not model_classes:
        return []

    edges = _model_reference_edges(models_dir, model_classes)
    names = set(model_classes)

    entry: set[str] = set()
    for doc in endpoint_docs:
        labels = [r.type_label for r in doc.responses]
        if doc.request_body:
            labels.append(doc.request_body.type_label)
        for label in labels:
            base = label.replace("[]", "").strip()
            if base in names:
                entry.add(base)

    if not entry:
        entry = set(model_classes)

    nodes: set[str] = set(entry)
    for cls in entry:
        nodes |= edges.get(cls, set())

    if len(nodes) > _MODEL_DIAGRAM_MAX_NODES:
        nodes = set(sorted(nodes)[:_MODEL_DIAGRAM_MAX_NODES])

    shown_edges = sorted(
        (src, dst) for src in nodes for dst in edges.get(src, set()) if dst in nodes
    )

    diagram = ["classDiagram"]
    for name in sorted(nodes):
        diagram.append(f"    class {name}")
    for src, dst in shown_edges:
        diagram.append(f"    {src} --> {dst}")

    summary = f"Model relationships ({len(nodes)} of {len(model_classes)} models)"
    return [
        "<details>",
        f"<summary>{summary}</summary>",
        "",
        f"{MD_FENCE}mermaid",
        *diagram,
        MD_FENCE,
        "",
        "</details>",
        "",
    ]


def _render_service_overview(
    service: str, group_order: list[str], grouped: dict[str, list[EndpointDoc]]
) -> list[str]:
    """Renders a component diagram showing the SDK code structure for this service.

    Returns nothing for schema-only services.
    """
    if not group_order:
        return []

    title = service.replace("_", " ").title()
    return [
        "## Overview",
        "",
        f"{MD_FENCE}mermaid",
        "flowchart LR",
        '    subgraph sdk["kentik_api"]',
        '        KA["KentikAPI"]',
        f'        W["{title}ServiceWrapper\\nclient.{service}"]',
        f'        REST["REST functions\\ngen/{service}/services/"]',
        '        RJ["request_json()\\ncore/rest_runtime"]',
        f'        M["Models\\ngen/{service}/models/"]',
        f'        E["Error classes\\ngen/{service}/error/"]',
        "    end",
        '    API["Kentik API"]',
        "",
        "    KA --> W",
        "    W --> REST",
        "    REST --> RJ",
        "    REST --> M",
        "    REST --> E",
        "    RJ --> API",
        MD_FENCE,
        "",
    ]


def render_endpoint_docs(service_endpoint_docs: dict[str, list[EndpointDoc]]):
    """Generates Sphinx MyST stubs with real per-endpoint text and model docs.

    Replaces an image-rendered "API table" (unreadable once summaries/
    descriptions got long, and rendered even for swagger files with zero
    operations) with real MyST tables plus an auto-generated usage example
    per endpoint, and replaces image-rendered model class diagrams (illegible
    once a service has more than a couple dozen models, e.g. alerting's 185)
    with sphinxcontrib.autodoc_pydantic's per-model field/JSON-schema docs.
    """
    print("Generating Sphinx documentation stubs...")

    DOCS_SERVICES_DIR = PROJECT_ROOT / "docs" / "sphinx" / "services"
    DOCS_SERVICES_DIR.mkdir(parents=True, exist_ok=True)

    # Every .md here is generated, so clear them first. Writing without clearing
    # leaves a page behind for any service that stops existing, which is how a
    # page for a non-Service directory survived earlier regenerations.
    for stale in DOCS_SERVICES_DIR.glob("*.md"):
        stale.unlink()

    index_entries: list[str] = []

    for service_dir in iter_service_dirs():
        service = service_dir.name
        title = service.replace("_", " ").title()

        services_folder = service_dir / "services"
        if not services_folder.exists():
            services_folder = service_dir / "service"
        wrapper_file = (
            services_folder / f"{service}.py" if services_folder.exists() else None
        )
        wrapper_signatures = (
            parse_wrapper_method_signatures(wrapper_file)
            if wrapper_file and wrapper_file.exists()
            else {}
        )

        lines = [
            _provenance(render_endpoint_docs),
            "<!-- Rebuilt on every `make generate`. Do not edit by hand. -->",
            "",
            f"# {title} Service",
            "",
        ]

        endpoint_docs = service_endpoint_docs.get(service, [])
        grouped: dict[str, list[EndpointDoc]] = {}
        group_order: list[str] = []
        for doc in endpoint_docs:
            if doc.tag not in grouped:
                grouped[doc.tag] = []
                group_order.append(doc.tag)
            grouped[doc.tag].append(doc)

        lines.extend(_render_service_overview(service, group_order, grouped))
        lines.extend(["## Endpoints", ""])

        if not endpoint_docs:
            lines.extend(
                [
                    "This service's schema defines shared types only -- no REST endpoints.",
                    "",
                ]
            )
        else:
            show_group_headers = len(group_order) > 1
            endpoint_heading_level = 4 if show_group_headers else 3
            for group_name in group_order:
                if show_group_headers:
                    lines.extend([f"### {group_name}", ""])
                # A thematic break between consecutive endpoints within a
                # group makes long pages (e.g. alerting's 37 operations)
                # scannable -- without it, sections with the same shape
                # (heading, prose, two tables, a code block) visually
                # bleed into each other. Not needed before the first
                # endpoint in a group: the group/service heading above it
                # is already a strong enough break.
                for idx, doc in enumerate(grouped[group_name]):
                    if idx > 0:
                        lines.extend(["---", ""])
                    lines.extend(
                        _render_endpoint_section(
                            service, doc, wrapper_signatures, endpoint_heading_level
                        )
                    )

        lines.extend(["## Data Models", ""])
        models_dir = service_dir / "models"
        model_classes = sorted(discover_service_model_classes(service_dir))
        if not model_classes:
            lines.extend(["No data models for this service.", ""])
        else:
            lines.extend(
                _render_model_relationship_diagram(
                    endpoint_docs, models_dir, model_classes
                )
            )
            for class_name in model_classes:
                directive = _autodoc_directive_for_model(models_dir, class_name)
                lines.extend(
                    [
                        f"{MD_FENCE}{{eval-rst}}",
                        f".. {directive}:: kentik_api.gen.{service}.models.{class_name}",
                        *(["   :members:"] if directive == "autoclass" else []),
                        f"{MD_FENCE}",
                        "",
                    ]
                )

        stub_content = "\n".join(lines)

        (DOCS_SERVICES_DIR / f"{service}.md").write_text(stub_content, encoding="utf-8")
        index_entries.append(service)

    index_content = (
        _provenance(render_endpoint_docs) + "\n"
        "<!-- Rebuilt on every `make generate`. Do not edit by hand. -->\n\n"
        "# API Services\n\n"
        "For a runtime-level map of how the SDK client, mixin, auth/core/errors, "
        "and generated services connect, see "
        "[SDK Runtime Architecture](../sdk_runtime_architecture.md).\n\n"
        f"{MD_FENCE}{{toctree}}\n:maxdepth: 1\n\n"
    )
    index_content += "\n".join(sorted(index_entries)) + "\n"
    index_content += f"{MD_FENCE}\n"
    (DOCS_SERVICES_DIR / "index.md").write_text(index_content, encoding="utf-8")

    # Build the services/README.md table from the same data so it never goes stale.
    readme_rows: list[str] = []
    for service in sorted(index_entries):
        title = service.replace("_", " ").title()
        docs = service_endpoint_docs.get(service, [])
        # Use the first endpoint summary as a short service description.
        blurb = next((d.summary for d in docs if d.summary), "")
        # Use space-content-space for filled cells; single space for empty ones so
        # markdownlint doesn't flag the double-space |  | pattern.
        desc_cell = f" {blurb} " if blurb else " "
        readme_rows.append(f"| {title} | [{service}.md]({service}.md) |{desc_cell}|")

    readme_content = "\n".join(
        [
            _provenance(render_endpoint_docs),
            "<!-- Rebuilt on every `make generate`. Do not edit by hand. -->",
            "",
            "# API Service Pages",
            "",
            "One Markdown page per Kentik API service, generated by",
            "[`scripts/generation/endpoint_docs.py`](../../scripts/generation/endpoint_docs.py). **Do not hand-edit these files**;",
            "they are overwritten on every `make generate` run.",
            "",
            "## What each page contains",
            "",
            f"{MD_FENCE}mermaid",
            "flowchart LR",
            '    subgraph page["service.md"]',
            '        OV["Overview\\n(component diagram)"]',
            '        EP["Endpoints\\n(one section per operation)"]',
            '        subgraph sec["per-operation section"]',
            '            SD["Sequence diagram"]',
            '            PT["Parameter table"]',
            '            RT["Response table"]',
            '            EX["Usage example"]',
            "        end",
            "        OV --> EP --> sec",
            "    end",
            MD_FENCE,
            "",
            "## Services",
            "",
            "| Service | Page | Description |",
            "| --- | --- | --- |",
            *readme_rows,
            "",
        ]
    )
    (DOCS_SERVICES_DIR / "README.md").write_text(readme_content, encoding="utf-8")


class EndpointDocsCollector:
    """Accumulates extract_endpoint_docs results, then renders them.

    Exists for callers that accumulate across a schema-availability loop;
    calling extract_endpoint_docs / render_endpoint_docs directly with a plain
    dict is equivalent. The ordering constraint (render() after wrapper
    generation) is the caller's responsibility, matching the module docstring.

    extract() deliberately does not catch exceptions: a swallowed failure
    publishes a silently empty page while the run reports success.
    """

    def __init__(self) -> None:
        self._docs: dict[str, list[EndpointDoc]] = {}

    def extract(self, service: str, swagger_path: Path) -> None:
        self._docs.setdefault(service, []).extend(extract_endpoint_docs(swagger_path))

    def render(self) -> None:
        render_endpoint_docs(self._docs)
