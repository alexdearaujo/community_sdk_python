# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
"""Runtime architecture docs (inline Mermaid), the gen/ root README, and per-service READMEs.

Also updates <!-- kentik-gen:MARKER --> blocks in docs/sphinx/guides/ files so every
reference to generated service names, method names, and class names stays
current without manual edits.
"""

import ast
import re
from pathlib import Path

from . import diagram_kit as dk
from ._shared import (
    PROJECT_ROOT,
    REGENERATE_COMMAND,
    SDK_OUTPUT_DIR,
    iter_service_dirs,
    mermaid_init,
    parse_generated_rest_module,
    parse_wrapper_methods,
    write_text_lf,
)
from .explorer_docs import fragment, write_static_assets

_GUIDES_DIR = PROJECT_ROOT / "docs" / "sphinx" / "guides"

_GEN_ROOT_README = f"""\
<!-- AUTO-GENERATED: scripts/generation/docs_rendering.py, _generate_gen_root_readme() -->
<!-- Rebuilt on every `{REGENERATE_COMMAND}`. Do not edit by hand. -->
# Generated Services (`kentik_api.gen`)

The generator builds every file in this folder. Each
[`{REGENERATE_COMMAND}`](../../../pyproject.toml) run deletes each subdirectory here,
builds it again, and writes this README again.

> [!WARNING]
> Do not edit any file in this folder, this README included. The next run deletes the edit.
> If the output is wrong, fix the generator ([`scripts/generate_sdk.py`](../../../scripts/generate_sdk.py)),
> a phase module in [`scripts/generation/`](../../../scripts/generation/README.md), or a template in
> [`scripts/openapi_templates/`](../../../scripts/openapi_templates/README.md). Then run the generator again.

## Layout

Each subdirectory is one Kentik API service (`device`, `alerting`, `user`, and others).
The generator builds it from the OpenAPI v3 schema files of that service.
Each service directory has the same shape:

```text
gen/device/
├── models/      Pydantic v2 request and response models
├── services/    one REST function per operation, and the DeviceServiceWrapper class
├── error/       one error class per operation, picked by the response status code
├── pb/          gRPC stubs (*_pb2.py, *_pb2_grpc.py) for the gRPC transport
└── README.md    a link to the Sphinx reference page of the service
```

## Where a call runs

No service directory here has its own HTTP, auth, or retry code.

- On a REST transport, each generated REST function calls `request_json()` in
  [`kentik_api.core`](../core/README.md). That one function sends the REST traffic of every service.
- On a gRPC transport, a wrapper method calls `call_grpc()` in [`kentik_api.core`](../core/README.md).
  The generator writes that call when an RPC has the same HTTP rule as the REST operation: the same
  proto service, verb, and path.

A wrapper method raises `NotImplementedError` on a `GrpcTransport` in two cases only:

1. The proto companions of the service did not import.
2. No RPC has the same HTTP rule as the operation.

[SDK Runtime Architecture](../../../docs/sphinx/sdk_runtime_architecture.md) shows the full call path.

## Full reference

The page `docs/sphinx/services/<service>.md` gives the parameters, the response shapes, and a usage
example for each operation of a service. The built Sphinx docs show the same pages.
"""


def _services_without_wrappers_section() -> list[str]:
    """Explains why some generated Services are absent from the client.

    Generated rather than hand-written prose so the service list cannot go stale:
    the gap closes on its own if upstream adds the missing HTTP bindings.
    """
    unmounted = [
        service_dir.name
        for service_dir in iter_service_dirs()
        if not any(
            parse_generated_rest_module(module)
            for module in (service_dir / "services").glob("*.py")
        )
    ]
    if not unmounted:
        return []

    return [
        "## Services Without A Wrapper",
        "",
        "The REST paths in the OpenAPI schema drive wrapper generation. If the schema",
        "of a Service declares no paths, the generator writes its models and proto",
        "stubs but no wrapper, and the client does not mount it. This is intentional.",
        "REST operations are the contract of this SDK. Wrapper generation from protos",
        "is out of scope.",
        "",
        f"{len(unmounted)} Services are in that state today: "
        + ", ".join(f"`{name}`" for name in unmounted)
        + ".",
        "",
        "Some of these Services declare gRPC RPCs upstream, but the RPCs have no",
        "`google.api.http` annotation, so no path reaches the schema. That is a gap",
        "in the upstream schema, not in the SDK. If upstream adds the annotation, the",
        "next run generates the wrapper.",
        "",
    ]


def _rest_only_services_section(rest_only: frozenset[str]) -> list[str]:
    """Names the Services generated from the local schema base, which are REST only."""
    if not rest_only:
        return []
    return [
        "## REST-Only Services",
        "",
        "These Services come from the local schema base, `schema/openapi/`. It holds",
        "descriptions, maintained by hand, of endpoints that upstream does not publish.",
        "Each client mounts these Services on a REST transport to their own host. A",
        'client with `protocol="grpc"` also sends their calls over REST: '
        + ", ".join(f"`{name}`" for name in sorted(rest_only))
        + ".",
        "",
    ]


def _generate_gen_root_readme() -> None:
    """Writes src/kentik_api/gen/README.md, kept in sync with the gen/ tree."""
    SDK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_text_lf(SDK_OUTPUT_DIR / "README.md", _GEN_ROOT_README)


def _generate_service_readmes(rest_only: frozenset[str] = frozenset()):
    """Generates README.md files inside each service directory."""
    print("Generating module READMEs...")
    for service_dir in iter_service_dirs():
        service_name = service_dir.name
        source = (
            "a description in the local schema base, `schema/openapi/`. It is REST only."
            if service_name in rest_only
            else "the Kentik OpenAPI v3 schema."
        )

        lines = [
            "<!-- AUTO-GENERATED: scripts/generation/docs_rendering.py, _generate_service_readmes() -->",
            f"<!-- Rebuilt on every `{REGENERATE_COMMAND}`. Do not edit by hand. -->",
            f"# {service_name.replace('_', ' ').title()} Service",
            "",
            f"The generator builds this module from {source}",
            "",
            (
                "The Sphinx page "
                f"[`docs/sphinx/services/{service_name}.md`](../../../../docs/sphinx/services/{service_name}.md) "
                "gives the parameters, responses, and a usage example for each operation, "
                "and documents each data model."
            ),
        ]

        doc_content = "\n".join(lines) + "\n"

        write_text_lf(service_dir / "README.md", doc_content)


def _module_name_from_path(py_path: Path, package_root: Path) -> str:
    rel = py_path.relative_to(package_root).with_suffix("")
    return "kentik_api." + ".".join(rel.parts)


def _resolve_import_from(current_module: str, level: int, module: str | None) -> str:
    if level == 0:
        return module or ""

    parts = current_module.split(".")[:-1]
    if level > 0:
        ups = max(level - 1, 0)
        parts = parts[: len(parts) - ups] if ups <= len(parts) else []
    suffix = module.split(".") if module else []
    return ".".join(parts + suffix)


_GROUP_CONFIG: dict[str, tuple[str, str]] = {
    # label: (layer, source path under kentik_api/)
    "Client API": ("client", "client.py"),
    "Client Mixin": ("client", "client_mixin.py"),
    "Auth Credentials": ("foundation", "auth/"),
    "API Config": ("foundation", "core/api_config.py"),
    "REST Runtime": ("foundation", "core/rest_runtime.py"),
    "gRPC Runtime": ("foundation", "core/grpc_runtime.py"),
    "Rate Limit": ("foundation", "core/rate_limit.py"),
    "Error Types": ("foundation", "errors/"),
    "Transport Base": ("transport", "transports/base.py"),
    "REST Transport": ("transport", "transports/rest_client.py"),
    "gRPC Transport": ("transport", "transports/grpc_client.py"),
    "Generated Service Wrappers": ("generated", "gen/{service}/services/{service}.py"),
    "Generated REST Services": ("generated", "gen/{service}/services/"),
    "Generated Models": ("generated", "gen/{service}/models/"),
    "Generated Error Classes": ("generated", "gen/{service}/error/"),
    "Generated Proto Stubs": ("generated", "gen/{service}/pb/"),
}

_LAYER_NAMES: dict[str, str] = {
    "client": "Client Layer",
    "generated": "Generated Layer",
    "transport": "Transport Layer",
    "foundation": "Shared Foundation",
}

# Explorer parts, each a set of module groups. The layout is fixed by hand, so
# _dependency_explorer() checks every drawn wire against the scanned imports.
_PART_GROUPS: dict[str, tuple[str, ...]] = {
    "base": ("API Config", "Auth Credentials", "Error Types", "Rate Limit"),
    "rj": ("REST Runtime",),
    "cg": ("gRPC Runtime",),
    "tr": ("Transport Base", "REST Transport", "gRPC Transport"),
    "models": ("Generated Models",),
    "rest": ("Generated REST Services", "Generated Error Classes"),
    "pb": ("Generated Proto Stubs",),
    "wrap": ("Generated Service Wrappers",),
    "client": ("Client API", "Client Mixin"),
}

_W, _H = 200, 72
_COLS = (40, 330, 620)
_ROWS = (30, 170, 310, 450, 590)

# part: (column, row, family, kind, box lines, card title, role, if it stops)
_PARTS: dict[str, tuple[int, int, str, str, list[str], str, str, str]] = {
    "base": (
        1,
        0,
        "neutral",
        "hub",
        ["Shared foundation", "APIConfig, auth,", "KentikError, RateLimit"],
        "Shared foundation",
        "APIConfig, the auth headers, the KentikError hierarchy and RateLimit. Every other part imports it.",
        "Expected: nothing in the SDK imports, so every call fails.",
    ),
    "rj": (
        0,
        1,
        "neutral",
        "hub",
        ["request_json()", "core/rest_runtime.py", "all REST traffic"],
        "request_json()",
        "The one function that sends REST traffic: auth headers, quota, and errors.",
        "Expected: every REST call fails. gRPC calls fail too, because they parse responses with it.",
    ),
    "cg": (
        1,
        1,
        "neutral",
        "hub",
        ["call_grpc()", "core/grpc_runtime.py", "all gRPC traffic"],
        "call_grpc()",
        "The one function that sends gRPC traffic: deadline, quota, and errors.",
        "Expected: every gRPC call fails. REST calls keep working.",
    ),
    "tr": (
        2,
        1,
        "violet",
        "proc",
        ["Transports", "transports/", "REST and gRPC"],
        "Transports",
        "RestTransport holds the APIConfig. GrpcTransport holds the TLS channel and the default deadline.",
        "Expected: the client cannot be built, on either transport.",
    ),
    "rest": (
        0,
        2,
        "green",
        "proc",
        ["REST functions", "gen/{service}/services/", "+ error classes"],
        "REST functions and error classes",
        "One function per operation. Each one calls request_json() with its own error class.",
        "Expected: REST calls fail for that service. gRPC calls through the same wrapper keep working.",
    ),
    "models": (
        1,
        2,
        "green",
        "src",
        ["Models", "gen/{service}/models/", "Pydantic v2"],
        "Models",
        "The request and response models of every operation. They import nothing else in the SDK.",
        "Expected: the REST functions and the wrappers of that service do not import, so it does not mount.",
    ),
    "pb": (
        2,
        2,
        "green",
        "src",
        ["Proto stubs", "gen/{service}/pb/", "protoc output"],
        "Proto stubs",
        "The modules that protoc compiles. Wrappers call them on a gRPC transport.",
        "Expected: gRPC calls for that service raise NotImplementedError. REST calls keep working.",
    ),
    "wrap": (
        1,
        3,
        "green",
        "proc",
        ["Service wrappers", "client.{service}", "one per service"],
        "Service wrappers",
        "Send each call to the REST function or to call_grpc(), for the transport in use.",
        "Expected: the client does not mount that service, on either transport.",
    ),
    "client": (
        1,
        4,
        "orange",
        "proc",
        ["KentikAPI", "client.py", "client_mixin.py"],
        "KentikAPI client",
        "Reads the credentials, picks the transport, and mounts every wrapper.",
        "Expected: nothing in the SDK can be called.",
    ),
}

# wire id: (path, provider>consumer keys, label, label position, anchor, arrow)
_WIRES: list[tuple[str, str, list[str], str | None, tuple[int, int], str, bool]] = [
    (
        "base_rj",
        "M330,66 H140 V170",
        ["base>rj"],
        "APIConfig, auth",
        (235, 58),
        "middle",
        True,
    ),
    ("base_cg", "M430,102 V170", ["base>cg"], "APIConfig", (438, 140), "start", True),
    (
        "base_tr",
        "M530,66 H720 V170",
        ["base>tr"],
        "APIConfig, auth",
        (625, 58),
        "middle",
        True,
    ),
    ("rj_cg", "M240,206 H330", ["rj>cg"], "parsing", (276, 198), "middle", True),
    (
        "rj_rest",
        "M140,242 V310",
        ["rj>rest"],
        "request_json()",
        (132, 280),
        "end",
        True,
    ),
    (
        "cg_wrap",
        "M530,226 H575 V420 H490 V450",
        ["cg>wrap"],
        "call_grpc()",
        (567, 290),
        "end",
        True,
    ),
    (
        "models_rest",
        "M330,346 H240",
        ["models>rest"],
        "models",
        (294, 338),
        "middle",
        True,
    ),
    (
        "models_wrap",
        "M430,382 V450",
        ["models>wrap"],
        "models",
        (438, 420),
        "start",
        True,
    ),
    (
        "rest_wrap",
        "M140,382 V486 H330",
        ["rest>wrap"],
        "operations",
        (148, 440),
        "start",
        True,
    ),
    (
        "pb_wrap",
        "M720,382 V470 H530",
        ["pb>wrap"],
        "proto stubs",
        (728, 430),
        "start",
        True,
    ),
    (
        "tr_stem",
        "M820,206 H860 V500",
        ["tr>wrap", "tr>client"],
        "transport",
        (868, 350),
        "start",
        False,
    ),
    ("tr_wrap", "M860,500 H530", ["tr>wrap"], None, (0, 0), "middle", True),
    ("tr_client", "M860,500 V626 H530", ["tr>client"], None, (0, 0), "middle", True),
    (
        "wrap_client",
        "M430,522 V590",
        ["wrap>client"],
        "wrappers",
        (438, 560),
        "start",
        True,
    ),
]

# Real imports the explorer leaves out, so the figure stays readable.
_UNDRAWN = {"base>rest", "base>wrap", "base>client", "rest>client"}

_PATHS = {
    "rest": {
        "label": "REST call",
        "family": "blue",
        "title": "A call on a REST transport",
        "text": "The wrapper calls the REST function. It builds the request with the models and sends it with request_json().",
        "links": ["base>rj", "rj>rest", "models>rest", "rest>wrap", "wrap>client"],
    },
    "grpc": {
        "label": "gRPC call",
        "family": "violet",
        "title": "A call on a gRPC transport",
        "text": "The wrapper builds the proto request with the stubs and sends it with call_grpc(), which parses the answer into the REST models.",
        "links": [
            "base>cg",
            "rj>cg",
            "cg>wrap",
            "pb>wrap",
            "models>wrap",
            "wrap>client",
        ],
    },
    "setup": {
        "label": "Client setup",
        "family": "orange",
        "title": "Building the client",
        "text": "KentikAPI builds one transport from the APIConfig and gives it to every wrapper that it mounts.",
        "links": ["base>tr", "tr>client", "tr>wrap", "wrap>client"],
    },
}

_GROUP_ROLES: dict[str, str] = {
    "Client API": "`KentikAPI`: reads the credentials and selects the transport.",
    "Client Mixin": "Mounts each service wrapper as `client.<service>`.",
    "Generated Service Wrappers": "Send each call to the REST function or to the gRPC stub, for the transport in use.",
    "Generated REST Services": "One function per operation in the OpenAPI schema. Each function calls `request_json()`.",
    "Generated Models": "Pydantic request and response models.",
    "Generated Error Classes": "One error class per operation, picked by the response status.",
    "Generated Proto Stubs": "The modules that protoc compiles. Wrappers call them on a gRPC transport.",
    "API Config": "`APIConfig`: base URL, credentials, TLS, timeouts, and the shared HTTP client.",
    "REST Runtime": "`request_json()`: the one function that sends REST traffic.",
    "gRPC Runtime": "`call_grpc()`: the one function that sends gRPC traffic.",
    "Error Types": "The shared exception hierarchy under `KentikError`.",
    "Auth Credentials": "Builds the Kentik auth headers for REST and for gRPC.",
    "Rate Limit": "`RateLimit`: the quota that each response reports.",
    "Transport Base": "The base class of both transports.",
    "REST Transport": "`RestTransport`: holds the `APIConfig` for REST calls.",
    "gRPC Transport": "`GrpcTransport`: the TLS channel, with auth and the default deadline.",
}


def _call_path_diagram() -> list[str]:
    """The overview: one REST row and one gRPC row from the caller to the Kentik API."""
    services = 0
    operations = 0
    for service_dir in iter_service_dirs():
        ops = sum(
            len(parse_generated_rest_module(module))
            for module in (service_dir / "services").glob("*.py")
        )
        services += ops > 0
        operations += ops

    return [
        "```mermaid",
        mermaid_init(),
        "sequenceDiagram",
        "    participant C as Your code",
        f"    participant W as Service wrapper<br/>({services} services, {operations} operations)",
        "    box rgb(231,245,255) REST transport",
        "    participant R as REST function<br/>gen/{service}/services/",
        "    participant RJ as request_json()",
        "    participant RA as Kentik REST API",
        "    end",
        "    box rgb(243,240,255) gRPC transport",
        "    participant CG as call_grpc()",
        "    participant GA as Kentik gRPC API",
        "    end",
        "",
        "    C->>W: client.{service}.{method}(arguments)",
        "    alt REST transport",
        "        W->>R: arguments",
        "        R->>RJ: method, path, body, APIConfig",
        "        RJ->>RA: HTTPS request with auth headers",
        "        RA-->>RJ: JSON response",
        "        RJ-->>R: JSON dict + quota",
        "        R-->>W: Pydantic model",
        "    else gRPC transport",
        "        W->>CG: stub method + proto request",
        "        CG->>GA: gRPC call over TLS",
        "        GA-->>CG: proto response",
        "        CG-->>W: proto response + quota",
        "        W->>W: parse_grpc_response()",
        "    end",
        "    W-->>C: Pydantic model",
        "    Note over C,GA: On a failure, request_json() or call_grpc() raises a KentikError subclass.",
        "```",
    ]


def _dependency_explorer(edge_counts: dict[tuple[str, str], int]) -> list[str]:
    """The Module Dependencies explorer: provider-to-consumer wires between the parts."""
    part_of = {group: part for part, groups in _PART_GROUPS.items() for group in groups}
    imports: dict[str, int] = {}
    for (importer, imported), count in edge_counts.items():
        provider, consumer = part_of.get(imported), part_of.get(importer)
        if provider and consumer and provider != consumer:
            key = f"{provider}>{consumer}"
            imports[key] = imports.get(key, 0) + count

    drawn = {key for _, _, keys, *_ in _WIRES for key in keys}
    if missing := sorted(drawn - imports.keys()):
        raise ValueError(
            f"the dependency explorer draws imports that do not exist: {missing}"
        )
    if left_out := sorted(imports.keys() - drawn - _UNDRAWN):
        print(f"    ⚠️  The dependency explorer does not draw: {', '.join(left_out)}")

    def counted(keys: list[str], index: int) -> list[str]:
        return [
            f"{_PARTS[key.split('>')[index]][5]} ({imports[key]})"
            for key in sorted(keys)
        ]

    parts = {}
    for pid, (*_, title, role, stops) in _PARTS.items():
        sources = ", ".join(_GROUP_CONFIG[g][1] for g in _PART_GROUPS[pid])
        facts = [f"Source: {sources}"]
        if uses := counted([k for k in imports if k.endswith(f">{pid}")], 0):
            facts.append("Imports " + ", ".join(uses))
        if users := counted([k for k in imports if k.startswith(f"{pid}>")], 1):
            facts.append("Imported by " + ", ".join(users))
        parts[pid] = {"title": title, "role": role, "facts": facts, "stops": stops}

    prefix = "deps"
    wires = [
        dk.seg(sid, d, keys, prefix, label, at, anchor=anchor, arrow=arrow)
        for sid, d, keys, label, at, anchor, arrow in _WIRES
    ]
    boxes = [
        dk.node(pid, (_COLS[col], _ROWS[row], _W, _H), fam, kind, lines, label=title)
        for pid, (col, row, fam, kind, lines, title, _, _) in _PARTS.items()
    ]
    markup = dk.svg(
        "deps-svg",
        (960, 690),
        "Module dependencies: the shared foundation feeds the runtimes and the transports. "
        "They, the models and the proto stubs feed the service wrappers, which KentikAPI mounts.",
        "".join(wires + boxes),
        prefix,
    )
    data = {
        "select": "wrap",
        "parts": parts,
        "links": {key: f"{imports[key]} import statements" for key in sorted(drawn)},
        "paths": _PATHS,
    }
    return fragment(
        markup,
        data,
        "Select a part. Bold lines show what it needs. Moving lines show where it is used. Each arrow "
        "points from a module to a module that imports it. Every part also imports the shared "
        "foundation, but the diagram draws that only for the runtimes and the transports.",
    )


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
    if module_name.startswith("kentik_api.core.grpc_runtime"):
        return "gRPC Runtime"
    if module_name.startswith("kentik_api.core.rate_limit"):
        return "Rate Limit"
    if module_name.startswith("kentik_api.errors"):
        return "Error Types"
    if module_name.startswith("kentik_api.transports.base"):
        return "Transport Base"
    if module_name.startswith("kentik_api.transports.rest_client"):
        return "REST Transport"
    if module_name.startswith("kentik_api.transports.grpc_client"):
        return "gRPC Transport"

    if module_name.startswith("kentik_api.gen."):
        if ".pb." in module_name:
            return "Generated Proto Stubs"
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


def _generate_runtime_architecture_docs(
    rest_only: frozenset[str] = frozenset(),
) -> None:
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
        if not py_file.exists() or (
            py_file.name == "__init__.py" and py_file.parent.name != "error"
        ):
            continue
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"), filename=str(py_file))
        except OSError:
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
                base = _resolve_import_from(current_module, node.level, node.module)
                target_modules.append(base)
                target_modules.extend(f"{base}.{alias.name}" for alias in node.names)

            dst_groups = {
                _module_group(target_module)
                for target_module in target_modules
                if target_module.startswith("kentik_api")
            }
            for dst_group in dst_groups:
                if dst_group is None or dst_group == src_group:
                    continue
                nodes.add(dst_group)
                key = (src_group, dst_group)
                edge_counts[key] = edge_counts.get(key, 0) + 1

    imports_of: dict[str, list[str]] = {}
    for (src, dst), count in sorted(edge_counts.items()):
        imports_of.setdefault(src, []).append(f"{dst} ({count})")

    group_rows = [
        f"| {label} | {_LAYER_NAMES[layer]} | `{path}` | "
        f"{', '.join(imports_of.get(label, [])) or 'nothing in the SDK'} | "
        f"{_GROUP_ROLES.get(label, '')} |"
        for label, (layer, path) in _GROUP_CONFIG.items()
        if label in nodes
    ]

    architecture_md = [
        "---",
        "html_theme.sidebar_secondary.remove: true",
        "---",
        "",
        "<!-- AUTO-GENERATED: scripts/generation/docs_rendering.py, _generate_runtime_architecture_docs() -->",
        f"<!-- Rebuilt on every `{REGENERATE_COMMAND}`. Do not edit by hand. -->",
        "",
        "# SDK Runtime Architecture",
        "",
        "This page shows how a call moves through the SDK, and how the hand-written",
        "runtime modules and the generated services depend on each other.",
        "",
        "## Call Path",
        "",
        "Each method call on `client.<service>` takes one of two paths. The transport",
        "that the client uses selects the path. Both paths return the same Pydantic",
        "models and raise the same exception types.",
        "",
        *_call_path_diagram(),
        "",
        "1. `kentik_api.client.KentikAPI` reads the credentials and selects the transport.",
        "2. `kentik_api.client_mixin.KentikClientMixin` mounts one generated service",
        "   wrapper per service.",
        "3. On a REST transport, a wrapper calls the generated REST function in",
        "   `kentik_api.gen.<service>.services`. That function calls `request_json()`",
        "   in `kentik_api.core.rest_runtime`, with the shared `APIConfig`.",
        "4. On a gRPC transport, a wrapper calls `call_grpc()` in",
        "   `kentik_api.core.grpc_runtime`, with the compiled proto stubs in",
        "   `kentik_api.gen.<service>.pb`.",
        "5. Both runtimes turn each failure into a `kentik_api.errors` type, or into",
        "   the error class that the service generates for that operation.",
        "",
        "## Module Dependencies",
        "",
        "The SDK splits into the parts below. Select one to see what it imports and what",
        "imports it. The generator reads the imports from the source on every run.",
        "",
        *_dependency_explorer(edge_counts),
        "",
        "The table lists each module group, and the groups that it imports, with the",
        "number of import statements.",
        "",
        "| Group | Layer | Source | Imports from | Role |",
        "| --- | --- | --- | --- | --- |",
        *group_rows,
        "",
        *_services_without_wrappers_section(),
        *_rest_only_services_section(rest_only),
    ]
    write_text_lf(docs_root / "sdk_runtime_architecture.md", "\n".join(architecture_md))

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
            write_text_lf(index_path, index_text)


def _grpc_stub_method_name(wrapper_file: Path, method_name: str) -> str | None:
    """Reads the real gRPC stub method a wrapper method calls, e.g. "ListASGroups".

    Parsed off the generated `call_grpc(self._grpc_stub_N.<Name>, _req)` call
    rather than re-derived from the snake_case method name: re-deriving loses
    acronym casing (`list_as_groups` -> `ListAsGroups`, not `ListASGroups`).
    """
    try:
        tree = ast.parse(
            wrapper_file.read_text(encoding="utf-8"), filename=str(wrapper_file)
        )
    except OSError:
        return None

    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef) or node.name != method_name:
            continue
        for sub in ast.walk(node):
            if (
                isinstance(sub, ast.Call)
                and isinstance(sub.func, ast.Name)
                and sub.func.id == "call_grpc"
                and sub.args
                and isinstance(sub.args[0], ast.Attribute)
            ):
                return sub.args[0].attr
    return None


def _strip_optional(type_str: str) -> str:
    optional_match = re.match(r"^Optional\[(.+)\]$", type_str)
    return optional_match.group(1) if optional_match else type_str


def _model_has_only_optional_fields(model_file: Path) -> bool:
    """True if every field on the model class has a Field(..., default=...).

    Lets _discover_example_ops() pick a request model that RequestClass()
    alone can construct, so the generated example snippet actually runs.
    """
    try:
        tree = ast.parse(
            model_file.read_text(encoding="utf-8"), filename=str(model_file)
        )
    except OSError:
        return False

    model_class = next(
        (node for node in tree.body if isinstance(node, ast.ClassDef)), None
    )
    if model_class is None:
        return False

    for node in model_class.body:
        if not isinstance(node, ast.AnnAssign):
            continue
        if not isinstance(node.value, ast.Call):
            return False  # a field with no Field(...) call has no default
        if not any(kw.arg == "default" for kw in node.value.keywords):
            return False

    return True


def _discover_example_ops(
    max_list_ops: int = 3,
) -> tuple[list[dict[str, str]], dict[str, str] | None]:
    """Scans generated *ServiceWrapper files to find representative operations.

    Returns (list_ops, body_op).
    list_ops: up to max_list_ops `list` or list_* operations, each {service, method, response_class}.
    body_op: first operation with a data: parameter, {service, method, request_class}.

    Both are chosen to be directly callable with no arguments, so the
    generated example snippets actually run: list_ops only includes `list` and list_*
    methods with zero required parameters, and body_op only includes a
    data-param operation whose request model has zero required fields
    (RequestClass() alone constructs successfully).
    """
    list_ops: list[dict[str, str]] = []
    body_op: dict[str, str] | None = None

    if not SDK_OUTPUT_DIR.exists():
        return list_ops, body_op

    for service_dir in iter_service_dirs():
        service_name = service_dir.name
        services_folder = service_dir / "services"
        if not services_folder.exists():
            continue

        for wrapper_file in sorted(services_folder.glob("*.py")):
            if wrapper_file.name == "__init__.py":
                continue

            for method in parse_wrapper_methods(wrapper_file):
                if (
                    len(list_ops) < max_list_ops
                    and re.match(r"list(_|$)", method.name.lower())
                    and method.return_type
                    and all(not is_required for _, _, is_required in method.params)
                ):
                    raw = _strip_optional(method.return_type)
                    response_class = raw.rsplit(".", 1)[-1]
                    if response_class:
                        list_ops.append(
                            {
                                "service": service_name,
                                "method": method.name,
                                "response_class": response_class,
                                "wrapper_file": str(wrapper_file),
                            }
                        )

                if body_op is None and method.has_data_param:
                    for param_name, annotation, _ in method.params:
                        if param_name == "data" and annotation:
                            raw = _strip_optional(annotation)
                            request_class = raw.rsplit(".", 1)[-1]
                            model_file = service_dir / "models" / f"{request_class}.py"
                            if model_file.exists() and _model_has_only_optional_fields(
                                model_file
                            ):
                                body_op = {
                                    "service": service_name,
                                    "method": method.name,
                                    "request_class": request_class,
                                }
                            break

        if len(list_ops) >= max_list_ops and body_op is not None:
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
    """Injects current generated operation names and counts into docs/sphinx/guides/ marker blocks."""
    if not SDK_OUTPUT_DIR.exists():
        return

    service_count = len(iter_service_dirs())

    list_ops, body_op = _discover_example_ops(max_list_ops=3)
    if not list_ops:
        print("    ⚠️  No list operations found; skipping guide snippet updates.")
        return

    primary = list_ops[0]
    stub_method = (
        _grpc_stub_method_name(Path(primary["wrapper_file"]), primary["method"])
        or primary["method"]
    )
    request_proto = primary["response_class"].replace("Response", "Request")

    gen_md = _GUIDES_DIR / "generation.md"
    if gen_md.exists():
        text = gen_md.read_text(encoding="utf-8")
        text = _replace_marker(text, "service-count", str(service_count))
        write_text_lf(gen_md, text)

    sphinx_readme = PROJECT_ROOT / "docs" / "sphinx" / "README.md"
    if sphinx_readme.exists():
        text = sphinx_readme.read_text(encoding="utf-8")
        text = _replace_marker(text, "service-count", str(service_count))
        write_text_lf(sphinx_readme, text)

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
        write_text_lf(qs_md, text)

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
        write_text_lf(rest_md, text)

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
{mermaid_init()}
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
    else 401
        API-->>RJ: error JSON
        RJ-->>C: raise AuthenticationError
    else other error status
        API-->>RJ: error JSON
        RJ-->>C: raise the operation's HTTPException subclass
    else no response (unreachable or timed out)
        RJ-->>C: raise TransportError
    end
```
""",
        )
        text = _replace_marker(
            text,
            "grpc-callflow-diagram",
            f"""
```mermaid
{mermaid_init()}
sequenceDiagram
    participant C as Caller
    participant W as ServiceWrapper
    participant CG as call_grpc()
    participant S as gRPC stub
    participant API as Kentik gRPC API

    C->>W: {primary["method"]}()
    W->>W: build {request_proto} proto<br/>(ParseDict for operations with a body)
    W->>CG: stub method + proto request
    CG->>S: {stub_method} (gRPC/TLS, deadline set by the channel)
    S->>API: serialized proto request
    alt success
        API-->>S: serialized proto response
        S-->>CG: {primary["response_class"]} proto
        CG-->>W: proto response and quota
        W-->>C: {primary["response_class"]} (Pydantic)<br/>via parse_grpc_response(), the same check as REST
    else gRPC error, deadline, or unreachable
        S-->>CG: raise RpcError
        CG-->>C: map_grpc_error(): AuthenticationError,<br/>the operation's HTTPException subclass, or TransportError
    end
```
""",
        )
        write_text_lf(grpc_md, text)

    body_label = f"{body_op['service']}.{body_op['method']}" if body_op else "none"
    print(
        f"    ✅ Guide snippets updated "
        f"({service_count} services, list: {primary['service']}.{primary['method']}, "
        f"body: {body_label})."
    )


def generate(rest_only: frozenset[str] = frozenset()) -> None:
    """Generates the runtime architecture docs, the gen/ root README, and per-service READMEs."""
    _generate_runtime_architecture_docs(rest_only)
    _generate_gen_root_readme()
    _generate_service_readmes(rest_only)
    _update_guide_snippets()
    write_static_assets(PROJECT_ROOT / "docs" / "sphinx" / "_static")
