# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Unit tests for docs_rendering._GROUP_CONFIG and _module_group consistency."""

from pathlib import Path

from scripts.generation.docs_rendering import (
    _GROUP_CONFIG,
    _LAYER_NAMES,
    _module_group,
)

_PACKAGE_ROOT = Path(__file__).resolve().parents[2] / "src" / "kentik_api"

# Hand-written modules the architecture diagram must never silently drop.
# _generate_runtime_architecture_docs() skips any module _module_group() maps to
# None, so an unmapped module vanishes from the diagram with no error at all --
# that is how core.grpc_runtime went missing from it entirely.
_HAND_WRITTEN_DIRS = ("auth", "core", "errors", "transports")


def _hand_written_modules() -> list[str]:
    modules = ["kentik_api.client", "kentik_api.client_mixin"]
    for rel in _HAND_WRITTEN_DIRS:
        for py_file in sorted((_PACKAGE_ROOT / rel).rglob("*.py")):
            if py_file.name == "__init__.py" and py_file.parent.name != "errors":
                continue
            parts = py_file.relative_to(_PACKAGE_ROOT).with_suffix("").parts
            modules.append("kentik_api." + ".".join(parts).removesuffix(".__init__"))
    return modules


def test_every_hand_written_module_maps_to_a_group():
    """No hand-written module may map to None, or it silently vanishes from the diagram."""
    unmapped = [m for m in _hand_written_modules() if _module_group(m) is None]
    assert not unmapped, (
        f"_module_group() returned None for {unmapped}; these modules would be "
        f"silently omitted from the generated architecture diagram. Add a branch "
        f"in _module_group() and a label in _GROUP_CONFIG."
    )


def test_every_layer_in_group_config_has_a_layer_name():
    """Every layer key referenced in _GROUP_CONFIG must have an entry in _LAYER_NAMES."""
    missing = {layer for layer in _GROUP_CONFIG.values() if layer not in _LAYER_NAMES}
    assert not missing, (
        f"Layer keys in _GROUP_CONFIG with no _LAYER_NAMES entry: {missing}"
    )


def test_group_config_covers_all_module_group_return_values():
    """_module_group() should only return labels that appear in _GROUP_CONFIG."""
    # Exercise a representative sample of module paths through _module_group
    # to verify their return values are in _GROUP_CONFIG.
    sample_modules = [
        ("kentik_api.client", None),
        ("kentik_api.client_mixin", None),
        ("kentik_api.auth.credentials", None),
        ("kentik_api.core.api_config", None),
        ("kentik_api.core.rest_runtime", None),
        ("kentik_api.core.grpc_runtime", None),
        ("kentik_api.errors", None),
        ("kentik_api.transports.base", None),
        ("kentik_api.transports.rest_client", None),
        ("kentik_api.transports.grpc_client", None),
        ("kentik_api.gen.device.error", None),
        ("kentik_api.gen.device.models.Device", None),
    ]
    for module_name, source_file in sample_modules:
        label = _module_group(module_name, source_file)
        if label is not None:
            assert label in _GROUP_CONFIG, (
                f"_module_group({module_name!r}) returned {label!r} "
                f"which is not in _GROUP_CONFIG"
            )


def test_group_config_has_no_duplicate_layer_assignments():
    """Sanity check: each group label appears exactly once in _GROUP_CONFIG."""
    assert len(_GROUP_CONFIG) == len(set(_GROUP_CONFIG)), (
        "Duplicate keys in _GROUP_CONFIG"
    )
