# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Unit tests for docs_rendering._GROUP_CONFIG and _module_group consistency."""

from scripts.generation.docs_rendering import (
    _GROUP_CONFIG,
    _LAYER_NAMES,
    _module_group,
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
