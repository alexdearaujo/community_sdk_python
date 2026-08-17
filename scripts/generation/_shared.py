"""Constants and helpers used by more than one generation phase module."""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
SDK_OUTPUT_DIR = PROJECT_ROOT / "src" / "kentik_api" / "gen"


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

    for f in files_to_scan:
        model_classes.update(
            re.findall(r"^class ([A-Za-z0-9_]+)[\(:]", f.read_text(), re.MULTILINE)
        )

    return model_classes
