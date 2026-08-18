"""Runtime architecture docs (inline Mermaid), the gen/ root README, and per-service READMEs."""

import ast
import re
from pathlib import Path

from ._shared import PROJECT_ROOT, SDK_OUTPUT_DIR

# Top-level README for src/kentik_api/gen/. This lives inside the fully-wiped
# gen/ tree, so it is generated here rather than hand-written: `make clean`
# (rm -rf gen/) would otherwise delete it with no way to regenerate it.
_GEN_ROOT_README = """\
# Generated Services (`kentik_api.gen`)

Fully generated. Every `make generate` run wipes and rebuilds every
subdirectory here, and rewrites this file too. **Never hand-edit
anything under this folder**, including this README. If output here is
wrong, fix the generator (`scripts/generate_sdk.py`, a phase module in
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
service, see `docs/source/services/<service>.md`, or the built
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
            f"# {service_name.replace('_', ' ').title()} Service",
            "",
            "This module was automatically generated from the Kentik OpenAPIv3 schema.",
            "",
            "For the full endpoint reference (parameters, responses, usage "
            "examples) and data model documentation, see the Sphinx docs: "
            f"`docs/source/services/{service_name}.md`.",
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
    docs_root = PROJECT_ROOT / "docs" / "source"

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

    mermaid_lines = ["flowchart LR"]

    for node_name in sorted(nodes):
        node_id = re.sub(r"[^A-Za-z0-9_]", "_", node_name)
        mermaid_lines.append(f'    {node_id}["{node_name}"]')

    mermaid_lines.append("")
    for (src, dst), count in sorted(edge_counts.items()):
        src_id = re.sub(r"[^A-Za-z0-9_]", "_", src)
        dst_id = re.sub(r"[^A-Za-z0-9_]", "_", dst)
        label = f'|"x{count}"|' if count > 1 else ""
        mermaid_lines.append(f"    {src_id} -->{label} {dst_id}")

    architecture_md = [
        "# SDK Runtime Architecture",
        "",
        "This page explains how core runtime modules and generated services connect at runtime.",
        "",
        "## Runtime Flow",
        "",
        "1. `kentik_api.client.KentikAPI` reads credentials and selects transport.",
        "2. `kentik_api.client_mixin.KentikClientMixin` mounts generated service wrappers.",
        "3. Wrapper classes in `kentik_api.gen.<service>.services.<service>` delegate to generated REST functions.",
        "4. Generated REST services use `kentik_api.core.api_config` and `kentik_api.core.rest_runtime`.",
        "5. Runtime failures are normalized into `kentik_api.errors` and generated service-local error classes.",
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


def generate() -> None:
    """Generates the runtime architecture docs, the gen/ root README, and per-service READMEs."""
    _generate_runtime_architecture_docs()
    _generate_gen_root_readme()
    _generate_service_readmes()
