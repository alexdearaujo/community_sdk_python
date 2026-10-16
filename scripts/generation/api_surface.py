# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Records the SDK's public API surface and diffs two recordings into release notes.

`make generate` writes `api_surface.json` at the repo root on every run. Because that
file is committed alongside the generated code, any two points in history can be
compared with a single `git show <ref>:api_surface.json`, instead of reconstructing
whole generated trees. `scripts/release_notes.py` does exactly that.

Nothing here records timestamps or versions of the generator itself. Those would
change on every run and bury the real signal under noise.
"""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path
from typing import Any

from ._shared import (
    PROJECT_ROOT,
    SDK_OUTPUT_DIR,
    discover_service_model_classes,
    iter_service_dirs,
    parse_generated_rest_module,
)

SURFACE_FILE = PROJECT_ROOT / "api_surface.json"
SCHEMA_VERSION = 1

_TRACKED_REQUIREMENTS = ("grpcio", "protobuf", "httpx", "pydantic")
_PROTOBUF_GENCODE_RE = re.compile(
    r"ValidateProtobufRuntimeVersion\(\s*_runtime_version\.Domain\.\w+,\s*(\d+),\s*(\d+),\s*(\d+),"
)
_GRPC_GENCODE_RE = re.compile(r'^GRPC_GENERATED_VERSION\s*=\s*"([^"]+)"', re.MULTILINE)


def _operation_key(method: str, path: str) -> str:
    """Identifies an operation by method and path.

    Never by operationId alone: multi-file services legitimately reuse generic ids
    such as `List` across different underlying REST modules.
    """
    return f"{method.upper()} {path}"


def _declared_requirements() -> dict[str, str]:
    pyproject = tomllib.loads(
        (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    )
    found = {}
    for spec in pyproject["project"]["dependencies"]:
        for package in _TRACKED_REQUIREMENTS:
            if re.match(rf"^{re.escape(package)}\s*[<>=!~]", spec):
                found[package] = spec
    return dict(sorted(found.items()))


def _gencode_versions() -> dict[str, str]:
    versions: dict[str, str] = {}
    for stub in SDK_OUTPUT_DIR.rglob("*_pb2.py"):
        match = _PROTOBUF_GENCODE_RE.search(stub.read_text(encoding="utf-8"))
        if match:
            versions["protobuf"] = ".".join(match.groups())
            break
    for stub in SDK_OUTPUT_DIR.rglob("*_pb2_grpc.py"):
        match = _GRPC_GENCODE_RE.search(stub.read_text(encoding="utf-8"))
        if match:
            versions["grpcio"] = match.group(1)
            break
    return versions


def _mounted_services() -> set[str]:
    mixin = PROJECT_ROOT / "src" / "kentik_api" / "client_mixin.py"
    if not mixin.exists():
        return set()
    return set(
        re.findall(r"from kentik_api\.gen\.(\w+)\.services\.", mixin.read_text("utf-8"))
    )


def capture(output_dir: Path | None = None) -> dict[str, Any]:
    """Builds a snapshot of the generated SDK's public surface."""
    root = SDK_OUTPUT_DIR if output_dir is None else output_dir
    mounted = _mounted_services()
    services: dict[str, Any] = {}

    for service_dir in iter_service_dirs(root):
        operations: dict[str, Any] = {}
        for module in sorted((service_dir / "services").glob("*.py")):
            for op in parse_generated_rest_module(module):
                operations[_operation_key(op.http_method, op.path)] = {
                    "operation": op.operation_name,
                    "status": op.expected_status,
                    "required_params": sorted(
                        name for name, _, required in op.params if required
                    ),
                }

        services[service_dir.name] = {
            "mounted": service_dir.name in mounted,
            "operations": dict(sorted(operations.items())),
            "models": sorted(discover_service_model_classes(service_dir)),
        }

    return {
        "schema_version": SCHEMA_VERSION,
        "requirements": _declared_requirements(),
        "gencode": _gencode_versions(),
        "services": dict(sorted(services.items())),
    }


def write(surface: dict[str, Any], path: Path | None = None) -> Path:
    target = SURFACE_FILE if path is None else path
    target.write_text(json.dumps(surface, indent=2) + "\n", encoding="utf-8")
    return target


def read(path: Path | None = None) -> dict[str, Any]:
    target = SURFACE_FILE if path is None else path
    return json.loads(target.read_text(encoding="utf-8"))


def diff(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    """Compares two surface snapshots into an ordered, render-ready delta."""
    old_services, new_services = before.get("services", {}), after.get("services", {})

    added = sorted(set(new_services) - set(old_services))
    removed = sorted(set(old_services) - set(new_services))

    changed: dict[str, Any] = {}
    for name in sorted(set(old_services) & set(new_services)):
        old, new = old_services[name], new_services[name]
        entry = {
            "added_operations": sorted(set(new["operations"]) - set(old["operations"])),
            "removed_operations": sorted(
                set(old["operations"]) - set(new["operations"])
            ),
            "added_models": sorted(set(new["models"]) - set(old["models"])),
            "removed_models": sorted(set(old["models"]) - set(new["models"])),
            "mount_changed": old["mounted"] != new["mounted"],
            "now_mounted": new["mounted"],
        }
        if any(v for k, v in entry.items() if k != "now_mounted"):
            changed[name] = entry

    return {
        "added_services": [
            {
                "name": name,
                "mounted": new_services[name]["mounted"],
                "operations": sorted(new_services[name]["operations"]),
                "models": new_services[name]["models"],
            }
            for name in added
        ],
        "removed_services": removed,
        "changed_services": changed,
        "requirements": _diff_mapping(
            before.get("requirements", {}), after.get("requirements", {})
        ),
        "gencode": _diff_mapping(before.get("gencode", {}), after.get("gencode", {})),
    }


def _diff_mapping(before: dict[str, str], after: dict[str, str]) -> dict[str, Any]:
    changes = {}
    for key in sorted(set(before) | set(after)):
        old, new = before.get(key), after.get(key)
        if old != new:
            changes[key] = {"before": old, "after": new}
    return changes


def is_empty(delta: dict[str, Any]) -> bool:
    return not any(delta.values())


def render_markdown(delta: dict[str, Any], *, since: str) -> str:
    """Renders a delta as GitHub-release-ready markdown."""
    if is_empty(delta):
        return f"No public API surface changes since `{since}`.\n"

    lines: list[str] = []
    breaking: list[str] = []

    if delta["added_services"]:
        lines.append("### New services\n")
        for service in delta["added_services"]:
            mount = (
                f"`client.{service['name']}`"
                if service["mounted"]
                else "types only, not mounted on the client"
            )
            lines.append(
                f"- **{service['name']}** ({mount}): "
                f"{len(service['operations'])} operations, {len(service['models'])} models"
            )
            for operation in service["operations"]:
                lines.append(f"  - `{operation}`")
        lines.append("")

    if delta["removed_services"]:
        breaking.append(
            "- Services removed: "
            + ", ".join(f"`client.{name}`" for name in delta["removed_services"])
        )

    endpoint_lines: list[str] = []
    for name, entry in delta["changed_services"].items():
        bullets = []
        for operation in entry["added_operations"]:
            bullets.append(f"  - added `{operation}`")
        for operation in entry["removed_operations"]:
            bullets.append(f"  - **removed** `{operation}`")
            breaking.append(f"- `{name}`: operation removed, `{operation}`")
        if entry["mount_changed"]:
            state = "now mounted on" if entry["now_mounted"] else "**no longer on**"
            bullets.append(f"  - {state} the client")
            if not entry["now_mounted"]:
                breaking.append(f"- `client.{name}` is no longer available")
        if entry["added_models"]:
            count = len(entry["added_models"])
            bullets.append(
                f"  - {count} new model{'s' if count != 1 else ''}: "
                + ", ".join(f"`{m}`" for m in entry["added_models"][:5])
                + (" ..." if count > 5 else "")
            )
        for model in entry["removed_models"]:
            breaking.append(f"- `{name}`: model removed, `{model}`")
        if bullets:
            endpoint_lines.append(f"- **{name}**")
            endpoint_lines.extend(bullets)

    if endpoint_lines:
        lines.append("### Changed services\n")
        lines.extend(endpoint_lines)
        lines.append("")

    if delta["requirements"]:
        lines.append("### Dependency requirements\n")
        for package, change in delta["requirements"].items():
            if change["before"] is None:
                lines.append(f"- `{package}` is now required: `{change['after']}`")
                breaking.append(f"- New required dependency, `{change['after']}`")
            elif change["after"] is None:
                lines.append(f"- `{package}` is no longer required")
            else:
                lines.append(
                    f"- `{package}`: `{change['before']}` to `{change['after']}`"
                )
                breaking.append(
                    f"- Dependency floor raised, `{change['before']}` to `{change['after']}`"
                )
        lines.append("")

    if delta["gencode"]:
        lines.append("### Generated protobuf toolchain\n")
        for package, change in delta["gencode"].items():
            lines.append(
                f"- `{package}` gencode: `{change['before']}` to `{change['after']}`"
            )
        lines.append("")

    if breaking:
        lines = [
            "### Breaking changes\n",
            *dict.fromkeys(breaking),
            "",
            *lines,
        ]

    return "\n".join(lines).rstrip() + "\n"


def render_summary(surface: dict[str, Any]) -> str:
    """Renders the whole surface, for the first release where no baseline exists yet."""
    services = surface.get("services", {})
    mounted = {name: s for name, s in services.items() if s["mounted"]}
    operations = sum(len(s["operations"]) for s in services.values())
    models = sum(len(s["models"]) for s in services.values())

    lines = [
        "### API surface",
        "",
        f"- {len(services)} services ({len(mounted)} mounted on the client)",
        f"- {operations} REST operations",
        f"- {models} models",
        "",
        "<details>",
        "<summary>Services</summary>",
        "",
    ]
    for name, service in services.items():
        count = len(service["operations"])
        detail = (
            f"`client.{name}`, {count} operation{'s' if count != 1 else ''}"
            if service["mounted"]
            else "types only, not mounted on the client"
        )
        lines.append(f"- **{name}**: {detail}")
    lines += ["", "</details>", ""]

    if surface.get("requirements"):
        lines += ["### Requires", ""]
        lines += [f"- `{spec}`" for spec in surface["requirements"].values()]
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def generate() -> Path:
    """Phase entrypoint: records the current surface. Called once per generation run."""
    return write(capture())
