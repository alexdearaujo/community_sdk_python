# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Swagger file selection and generated/schema service-directory parity validation."""

from pathlib import Path
from typing import TypedDict


class SwaggerFileMetadata(TypedDict):
    path: Path
    service: str
    namespace: tuple[str, ...]
    version: str
    filename: str


def _swagger_file_metadata(
    swagger_path: Path, openapi_base: Path
) -> SwaggerFileMetadata:
    """Extracts normalized metadata for a swagger file path."""
    rel = swagger_path.relative_to(openapi_base)
    if len(rel.parts) < 3:
        raise ValueError(f"Unexpected swagger path shape: {rel}")

    return {
        "path": swagger_path,
        "service": rel.parts[0],
        "namespace": tuple(rel.parts[1:-2]),
        "version": rel.parts[-2],
        "filename": rel.parts[-1],
    }


def select_latest_swagger_files_by_service(
    openapi_base: Path,
) -> tuple[dict[str, list[SwaggerFileMetadata]], int, int]:
    """Selects latest swagger per (service, namespace, filename) and groups by service."""
    all_swaggers = sorted(openapi_base.rglob("*.swagger.json"))
    latest_by_family: dict[tuple[str, tuple[str, ...], str], SwaggerFileMetadata] = {}

    for swagger_path in all_swaggers:
        metadata = _swagger_file_metadata(swagger_path, openapi_base)
        family_key = (
            metadata["service"],
            metadata["namespace"],
            metadata["filename"],
        )
        existing = latest_by_family.get(family_key)
        if existing is None or metadata["version"] > existing["version"]:
            latest_by_family[family_key] = metadata

    by_service: dict[str, list[SwaggerFileMetadata]] = {}
    for metadata in latest_by_family.values():
        service = metadata["service"]
        by_service.setdefault(service, []).append(metadata)

    for service in by_service:
        by_service[service].sort(
            key=lambda item: (
                item["namespace"],
                item["filename"],
                item["version"],
            )
        )

    selected_count = len(latest_by_family)
    ignored_count = len(all_swaggers) - selected_count
    return by_service, selected_count, ignored_count


def validate_generated_service_parity(
    source_services: set[str], generated_root: Path
) -> None:
    """Fails generation if top-level generated service dirs drift from schema dirs."""
    generated_services = {
        p.name
        for p in generated_root.iterdir()
        if p.is_dir() and p.name not in ("__pycache__", "pb_companions")
    }

    missing = sorted(source_services - generated_services)
    extra = sorted(generated_services - source_services)
    if not missing and not extra:
        return

    print("\n❌ Service directory parity check failed.")
    if missing:
        print("  Missing in generated output:", ", ".join(missing))
    if extra:
        print("  Extra generated directories:", ", ".join(extra))
    raise RuntimeError(
        "Generated service directories do not match source schema top-level directories."
    )
