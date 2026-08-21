# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Runtime architecture docs (inline Mermaid), the gen/ root README, and per-service READMEs.

Also updates <!-- kentik-gen:MARKER --> blocks in docs/guides/ files so every
reference to generated service names, method names, and class names stays
current without manual edits.
"""

import ast
import re
from pathlib import Path

from ._shared import PROJECT_ROOT, SDK_OUTPUT_DIR, parse_wrapper_methods

_GUIDES_DIR = PROJECT_ROOT / "docs" / "guides"

# Top-level README for src/kentik_api/gen/. This lives inside the fully-wiped
# gen/ tree, so it is generated here rather than hand-written: `make clean`
# (rm -rf gen/) would otherwise delete it with no way to regenerate it.
_GEN_ROOT_README = """\
<!-- AUTO-GENERATED: scripts/generation/docs_rendering.py, _generate_gen_root_readme() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->
# Generated Services (`kentik_api.gen`)

Fully generated. Every [`make generate`](../../../Makefile) run wipes and rebuilds every
subdirectory here, and rewrites this file too. **Never hand-edit
anything under this folder**, including this README. If output here is
wrong, fix the generator ([`scripts/generate_sdk.py`](../../../scripts/generate_sdk.py), a phase module in
[`scripts/generation/`](../../../scripts/generation/README.md)), or a
template in
[`scripts/openapi_templates/`](../../../scripts/openapi_templates/README.md).
Then regenerate.

## Layout

Each subdirectory is one Kentik API service (`device`, `alerting`,
`user`, and so on), built from that service's OpenAPI v3 schema files.
Every service directory has the same shape:

| Path | Contents |
| --- | --- |
| `models/` | Pydantic v2 request/response models |
| `services/` | Raw REST operation functions, plus a unified `<Service>ServiceWrapper` class |
| `error/` | Per-operation error classes, dispatched from each declared response status code |
| `pb/` | gRPC stubs (`*_pb2.py`, `*_pb2_grpc.py`); transport is a stub today, see below |
| `README.md` | One-paragraph pointer to the full Sphinx reference for that service |

```mermaid
flowchart TD
    G["kentik_api.gen.device"] --> M[models/]
    G --> S[services/]
    G --> E[error/]
    G --> P[pb/]
    S -->|calls| R["kentik_api.core.rest_runtime.request_json()"]
    S -->|on error status| E
```

## Where a call actually runs

Every generated REST operation, across every service, routes through
one shared function: `request_json()` in
[`kentik_api.core`](../core/README.md). No service directory here
implements its own HTTP, auth, or retry logic. gRPC transport is
intentionally a stub: generated wrapper methods raise
`NotImplementedError` for `GrpcTransport`. Only REST is fully wired.

## Full reference

For endpoint parameters, response shapes, and usage examples per
service, see `docs/sphinx/services/<service>.md`, or the built
Sphinx docs.
"""


def _generate_gen_root_readme() -> None:
    """Writes src/kentik_api/gen/README.md, kept in sync with the gen/ tree."""
    SDK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (SDK_OUTPUT_DIR / "README.md").write_text(_GEN_ROOT_README, encoding="utf-8")


def _generate_service_readmes():
    """Generates README.md files inside each service directory."""
    print("Generating module READMEs...")
    for service_dir in sorted(SDK_OUTPUT_DIR.iterdir(), key=lambda p: p.name):
        if not service_dir.is_dir() or service_dir.name == "__pycache__":
            continue

        service_name = service_dir.name

        lines = [
            "<!-- AUTO-GENERATED: scripts/generation/docs_rendering.py, _generate_service_readmes() -->",
            "<!-- Rebuilt on every `make generate`. Do not edit by hand. -->",
            f"# {service_name.replace('_', ' ').title()} Service",
            "",
            "This module was automatically generated from the Kentik OpenAPIv3 schema.",
            "",
            "For the full endpoint reference (parameters, responses, usage "
            "examples) and data model documentation, see the Sphinx docs: "
            f"[`docs/sphinx/services/{service_name}.md`](../../../../docs/sphinx/services/{service_name}.md).",
        ]

        doc_content = "\n".join(lines) + "\n"

        # Keep generated README self-contained and deterministic.
        (service_dir / "README.md").write_text(doc_content, encoding="utf-8")


def _module_name_from_path(py_path: Path, package_root: Path) -> str:
    rel = py_path.relative_to(package_root).with_suffix("")
    return "kentik_api." + ".".join(rel.parts)


def _resolve_import_from(current_module: str, level: int, module: str | None) -> str:
    if level == 0:
        return module or ""

    parts = current_module.split(".")[:-1]
    if level > 0:
        # Relative import semantics: one dot is current package.
        ups = max(level - 1, 0)
        parts = parts[: len(parts) - ups] if ups <= len(parts) else []
    suffix = module.split(".") if module else []
    return ".".join(parts + suffix)


# Single source of truth for group labels and their layer assignments.
# _module_group() returns keys from this dict; _generate_runtime_architecture_docs()
# derives _LAYERS from it. Adding a new group = one entry here.
_GROUP_CONFIG: dict[str, str] = {
    "Client API": "client",
    "Client Mixin": "client",
    "Auth Credentials": "foundation",
    "API Config": "foundation",
    "REST Runtime": "foundation",
    "Error Types": "foundation",
    "Transport Base": "transport",
    "REST Transport": "transport",
    "gRPC Transport": "transport",
    "Generated Service Wrappers": "generated",
    "Generated REST Services": "generated",
    "Generated Models": "generated",
    "Generated Error Classes": "generated",
}

_LAYER_NAMES: dict[str, str] = {
    "client": "Client Layer",
    "generated": "Generated Layer",
    "transport": "Transport Layer",
    "foundation": "Shared Foundation",
}


def _module_group(module_name: str, source_file: Path | None = None) -> str | None:
    if module_name == "kentik_api.client":
        return "Client API"
    if module_name == "kentik_api.client_mixin":
        return "Client Mixin"
    if module_name.startswith("kentik_api.auth"):
        return "Auth Credentials"
    if module_name.startswith("kentik_api.core.api_config"):
        return "API Config"
    if module_name.startswith("kentik_api.core.rest_runtime"):
        return "REST Runtime"
    if module_name.startswith("kentik_api.errors"):
        return "Error Types"
    if module_name.startswith("kentik_api.transports.base"):
        return "Transport Base"
    if module_name.startswith("kentik_api.transports.rest_client"):
        return "REST Transport"
    if module_name.startswith("kentik_api.transports.grpc_client"):
        return "gRPC Transport"

    if module_name.startswith("kentik_api.gen."):
        if ".error" in module_name:
            return "Generated Error Classes"
        if ".services." in module_name:
            if source_file is not None and source_file.name[:1].islower():
                return "Generated Service Wrappers"
            tail = module_name.split(".")[-1]
            if tail and tail[0].islower():
                return "Generated Service Wrappers"
            return "Generated REST Services"
        if ".models" in module_name:
            return "Generated Models"

    return None


def _generate_runtime_architecture_docs() -> None:
    """Generates a high-level runtime architecture page with an inline dependency graph."""
    package_root = PROJECT_ROOT / "src" / "kentik_api"
    docs_root = PROJECT_ROOT / "docs" / "sphinx"

    scan_paths: list[Path] = []
    scan_paths.extend([package_root / "client.py", package_root / "client_mixin.py"])
    for rel in ("auth", "core", "errors", "transports"):
        root = package_root / rel
        if root.exists():
            scan_paths.extend(sorted(root.rglob("*.py")))

    gen_root = package_root / "gen"
    if gen_root.exists():
        for service_dir in sorted([p for p in gen_root.iterdir() if p.is_dir()]):
            for folder in ("services", "service"):
                sf = service_dir / folder
                if sf.exists():
                    scan_paths.extend(sorted(sf.glob("*.py")))
            err_file = service_dir / "error" / "__init__.py"
            if err_file.exists():
                scan_paths.append(err_file)

    edge_counts: dict[tuple[str, str], int] = {}
    nodes: set[str] = set()

    for py_file in scan_paths:
        if not py_file.exists() or py_file.name == "__init__.py":
            continue
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        current_module = _module_name_from_path(py_file, package_root)
        src_group = _module_group(current_module, source_file=py_file)
        if src_group is None:
            continue
        nodes.add(src_group)

        for node in ast.walk(tree):
            target_modules: list[str] = []
            if isinstance(node, ast.Import):
                target_modules.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                target_modules.append(
                    _resolve_import_from(current_module, node.level, node.module)
                )

            for target_module in target_modules:
                if not target_module.startswith("kentik_api"):
                    continue
                dst_group = _module_group(target_module)
                if dst_group is None or dst_group == src_group:
                    continue
                nodes.add(dst_group)
                key = (src_group, dst_group)
                edge_counts[key] = edge_counts.get(key, 0) + 1

    # Layer assignments derived from _GROUP_CONFIG and _LAYER_NAMES.
    # Any label returned by _module_group that is not in _GROUP_CONFIG will
    # appear as an ungrouped node — the test_docs_rendering.py coverage check
    # catches this before it silently breaks the generated diagram.
    from collections import defaultdict

    layer_members: dict[str, set[str]] = defaultdict(set)
    for label, layer_key in _GROUP_CONFIG.items():
        layer_members[layer_key].add(label)
    _LAYERS: list[tuple[str, str, set[str]]] = [
        (key, _LAYER_NAMES[key], layer_members[key])
        for key in _LAYER_NAMES
        if layer_members[key]
    ]

    mermaid_lines = ["flowchart TB"]

    placed: set[str] = set()
    for sg_id, sg_label, members in _LAYERS:
        in_layer = members & nodes
        if not in_layer:
            continue
        mermaid_lines.append(f'    subgraph {sg_id}["{sg_label}"]')
        for node_name in sorted(in_layer):
            node_id = re.sub(r"[^A-Za-z0-9_]", "_", node_name)
            mermaid_lines.append(f'        {node_id}["{node_name}"]')
            placed.add(node_name)
        mermaid_lines.append("    end")

    for node_name in sorted(nodes - placed):
        node_id = re.sub(r"[^A-Za-z0-9_]", "_", node_name)
        mermaid_lines.append(f'    {node_id}["{node_name}"]')

    mermaid_lines.append("")
    for (src, dst), count in sorted(edge_counts.items()):
        src_id = re.sub(r"[^A-Za-z0-9_]", "_", src)
        dst_id = re.sub(r"[^A-Za-z0-9_]", "_", dst)
        label = f'|"x{count}"|' if count > 1 else ""
        mermaid_lines.append(f"    {src_id} -->{label} {dst_id}")

    architecture_md = [
        "<!-- AUTO-GENERATED: scripts/generation/docs_rendering.py, _generate_runtime_architecture_docs() -->",
        "<!-- Rebuilt on every `make generate`. Do not edit by hand. -->",
        "",
        "# SDK Runtime Architecture",
        "",
        "This page explains how core runtime modules and generated services connect at runtime.",
        "",
        "## Runtime Flow",
        "",
        "1. `kentik_api.client.KentikAPI` reads credentials and selects transport.",
        "2. `kentik_api.client_mixin.KentikClientMixin` mounts generated service wrappers.",
        "3. Wrapper classes in `kentik_api.gen.<service>.services.<service>` delegate\n   to generated REST functions.",
        "4. Generated REST services use `kentik_api.core.api_config` and `kentik_api.core.rest_runtime`.",
        "5. Runtime failures are normalized into `kentik_api.errors` and generated\n   service-local error classes.",
        "",
        "## Module Dependency Graph",
        "",
        "```mermaid",
        *mermaid_lines,
        "```",
        "",
        "## Reading The Graph",
        "",
        "- `Client API` and `Client Mixin` are the orchestration entrypoints.",
        "- `Generated Service Wrappers` are transport-aware facades exposed as `client.<service>`.",
        "- `Generated REST Services` host operation functions generated from OpenAPI schemas.",
        "- `API Config`, `REST Runtime`, and `Error Types` form the shared runtime foundation.",
        "",
    ]
    (docs_root / "sdk_runtime_architecture.md").write_text(
        "\n".join(architecture_md), encoding="utf-8"
    )

    index_path = docs_root / "index.md"
    if index_path.exists():
        index_text = index_path.read_text(encoding="utf-8")
        if "sdk_runtime_architecture" not in index_text:
            marker = "local_generation_workflow\n"
            if marker in index_text:
                index_text = index_text.replace(
                    marker, marker + "sdk_runtime_architecture\n", 1
                )
            else:
                index_text += "\nsdk_runtime_architecture\n"
            index_path.write_text(index_text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Guide snippet injection
# ---------------------------------------------------------------------------


def _method_to_pascal(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("_"))


def _strip_optional(type_str: str) -> str:
    m = re.match(r"^Optional\[(.+)\]$", type_str)
    return m.group(1) if m else type_str


def _discover_example_ops(
    n_list: int = 3,
) -> tuple[list[dict[str, str]], dict[str, str] | None]:
    """Scans generated *ServiceWrapper files to find representative operations.

    Returns (list_ops, body_op).
    list_ops: up to n_list list_* operations, each {service, method, response_class}.
    body_op: first operation with a data: parameter, {service, method, request_class}.
    """
    list_ops: list[dict[str, str]] = []
    body_op: dict[str, str] | None = None

    if not SDK_OUTPUT_DIR.exists():
        return list_ops, body_op

    for service_dir in sorted(SDK_OUTPUT_DIR.iterdir()):
        if not service_dir.is_dir() or service_dir.name.startswith("_"):
            continue
        service_name = service_dir.name
        services_folder = service_dir / "services"
        if not services_folder.exists():
            continue

        for wrapper_file in sorted(services_folder.glob("*.py")):
            if wrapper_file.name == "__init__.py":
                continue

            for method in parse_wrapper_methods(wrapper_file):
                if (
                    len(list_ops) < n_list
                    and method.name.lower().startswith("list_")
                    and method.return_type
                ):
                    raw = _strip_optional(method.return_type)
                    response_class = raw.rsplit(".", 1)[-1]
                    if response_class:
                        list_ops.append(
                            {
                                "service": service_name,
                                "method": method.name,
                                "response_class": response_class,
                            }
                        )

                if body_op is None and method.has_data_param:
                    for param_name, annotation, _ in method.params:
                        if param_name == "data" and annotation:
                            raw = _strip_optional(annotation)
                            request_class = raw.rsplit(".", 1)[-1]
                            body_op = {
                                "service": service_name,
                                "method": method.name,
                                "request_class": request_class,
                            }
                            break

        if len(list_ops) >= n_list and body_op is not None:
            break

    return list_ops, body_op


def _replace_marker(text: str, marker: str, new_content: str) -> str:
    """Replaces content inside <!-- kentik-gen:MARKER --> / <!-- /kentik-gen:MARKER --> tags."""
    pattern = re.compile(
        r"<!-- kentik-gen:" + re.escape(marker) + r" -->"
        r".*?"
        r"<!-- /kentik-gen:" + re.escape(marker) + r" -->",
        re.DOTALL,
    )
    replacement = (
        f"<!-- kentik-gen:{marker} -->" + new_content + f"<!-- /kentik-gen:{marker} -->"
    )
    return pattern.sub(replacement, text)


def _update_guide_snippets() -> None:
    """Injects current generated operation names and counts into docs/guides/ marker blocks."""
    if not SDK_OUTPUT_DIR.exists():
        return

    service_count = sum(
        1 for d in SDK_OUTPUT_DIR.iterdir() if d.is_dir() and not d.name.startswith("_")
    )

    list_ops, body_op = _discover_example_ops(n_list=3)
    if not list_ops:
        print("    ⚠️  No list operations found; skipping guide snippet updates.")
        return

    primary = list_ops[0]
    pascal_method = _method_to_pascal(primary["method"])
    request_proto = primary["response_class"].replace("Response", "Request")

    # generation.md: inline service count (same marker used twice in the file)
    gen_md = _GUIDES_DIR / "generation.md"
    if gen_md.exists():
        text = gen_md.read_text(encoding="utf-8")
        text = _replace_marker(text, "service-count", str(service_count))
        gen_md.write_text(text, encoding="utf-8")

    # docs/sphinx/README.md: inline service count in the services/ row
    sphinx_readme = PROJECT_ROOT / "docs" / "sphinx" / "README.md"
    if sphinx_readme.exists():
        text = sphinx_readme.read_text(encoding="utf-8")
        text = _replace_marker(text, "service-count", str(service_count))
        sphinx_readme.write_text(text, encoding="utf-8")

    # quickstart.md: first-call-example, grpc-call-example
    qs_md = _GUIDES_DIR / "quickstart.md"
    if qs_md.exists():
        text = qs_md.read_text(encoding="utf-8")
        text = _replace_marker(
            text,
            "first-call-example",
            f"""
```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest")
response = client.{primary["service"]}.{primary["method"]}()
print(response)  # {primary["response_class"]}
```
""",
        )
        text = _replace_marker(
            text,
            "grpc-call-example",
            f"""
```python
client = KentikAPI(protocol="grpc")
response = client.{primary["service"]}.{primary["method"]}()  # same API, same response models
```
""",
        )
        qs_md.write_text(text, encoding="utf-8")

    # rest.md: list-methods-example, request-body-example
    rest_md = _GUIDES_DIR / "rest.md"
    if rest_md.exists():
        text = rest_md.read_text(encoding="utf-8")
        list_lines = "\n".join(
            f"response = client.{op['service']}.{op['method']}()" for op in list_ops
        )
        text = _replace_marker(
            text,
            "list-methods-example",
            f"""
```python
{list_lines}
```
""",
        )
        if body_op:
            text = _replace_marker(
                text,
                "request-body-example",
                f"""
```python
from kentik_api.gen.{body_op["service"]}.models import {body_op["request_class"]}

response = client.{body_op["service"]}.{body_op["method"]}(data={body_op["request_class"]}())
```
""",
            )
        rest_md.write_text(text, encoding="utf-8")

    # grpc.md: grpc-usage-example, rest-callflow-diagram, grpc-callflow-diagram
    grpc_md = _GUIDES_DIR / "grpc.md"
    if grpc_md.exists():
        text = grpc_md.read_text(encoding="utf-8")
        text = _replace_marker(
            text,
            "grpc-usage-example",
            f"""
```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="grpc")
response = client.{primary["service"]}.{primary["method"]}()
print(response)  # {primary["response_class"]}
```
""",
        )
        text = _replace_marker(
            text,
            "rest-callflow-diagram",
            f"""
```mermaid
sequenceDiagram
    participant C as Caller
    participant W as ServiceWrapper
    participant RJ as request_json()
    participant API as Kentik REST API

    C->>W: {primary["method"]}()
    W->>RJ: api_config, method, path, params
    RJ->>API: HTTP request (HTTPS)
    alt success
        API-->>RJ: JSON response
        RJ-->>W: parsed dict
        W-->>C: {primary["response_class"]} (Pydantic)
    else HTTP error
        API-->>RJ: error JSON
        RJ-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```
""",
        )
        text = _replace_marker(
            text,
            "grpc-callflow-diagram",
            f"""
```mermaid
sequenceDiagram
    participant C as Caller
    participant W as ServiceWrapper
    participant B as proto bridge
    participant S as gRPC stub
    participant API as Kentik gRPC API

    C->>W: {primary["method"]}()
    W->>B: ParseDict(params, {request_proto})
    B->>S: {pascal_method} (gRPC/TLS)
    S->>API: serialized proto request
    alt success
        API-->>S: serialized proto response
        S-->>B: {primary["response_class"]} proto
        B-->>W: MessageToDict(response)
        W-->>C: {primary["response_class"]} (Pydantic)
    else gRPC error (status code)
        API-->>S: gRPC status + details
        S-->>W: raise RpcError
        W-->>C: raise HTTPException (normalized)
    end
```
""",
        )
        grpc_md.write_text(text, encoding="utf-8")

    body_label = f"{body_op['service']}.{body_op['method']}" if body_op else "none"
    print(
        f"    ✅ Guide snippets updated "
        f"({service_count} services, list: {primary['service']}.{primary['method']}, "
        f"body: {body_label})."
    )


def generate() -> None:
    """Generates the runtime architecture docs, the gen/ root README, and per-service READMEs."""
    _generate_runtime_architecture_docs()
    _generate_gen_root_readme()
    _generate_service_readmes()
    _update_guide_snippets()
