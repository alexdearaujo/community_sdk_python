# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Unit tests for scripts/generation/fixup.py.

All tests use tmp_path — no schema download or full generation run required.
"""

import textwrap
from pathlib import Path

import pytest

from scripts.generation.fixup import (
    _dedupe_top_level_function_names,
    _fix_wildcard_exports,
    _normalize_triple_quoted_docstrings,
    _patch_service_files,
    _rebuild_models_init,
    fix_generated_service,
)


# ---------------------------------------------------------------------------
# _rebuild_models_init
# ---------------------------------------------------------------------------


def test_rebuild_models_init_exports_all_classes(tmp_path):
    models = tmp_path / "models"
    models.mkdir()
    (models / "__init__.py").write_text("")
    (models / "Device.py").write_text("class Device:\n    pass\n")
    (models / "Interface.py").write_text("class Interface:\n    pass\n")

    _rebuild_models_init(tmp_path)

    init = (models / "__init__.py").read_text()
    assert "from .Device import Device as Device" in init
    assert "from .Interface import Interface as Interface" in init


def test_rebuild_models_init_skips_nonclass_files(tmp_path):
    models = tmp_path / "models"
    models.mkdir()
    (models / "__init__.py").write_text("")
    (models / "helpers.py").write_text("def helper(): pass\n")  # no class

    _rebuild_models_init(tmp_path)

    assert (models / "__init__.py").read_text() == ""


def test_rebuild_models_init_noop_without_models_dir(tmp_path):
    # Must not raise when models/ is absent
    _rebuild_models_init(tmp_path)


# ---------------------------------------------------------------------------
# _fix_wildcard_exports
# ---------------------------------------------------------------------------


def test_fix_wildcard_exports_replaces_star_import(tmp_path):
    (tmp_path / "foo.py").write_text("class Bar:\n    pass\n")
    init = tmp_path / "__init__.py"
    init.write_text("from .foo import *\n")

    _fix_wildcard_exports(tmp_path)

    assert "from .foo import Bar as Bar" in init.read_text()
    assert "import *" not in init.read_text()


def test_fix_wildcard_exports_skips_error_dirs(tmp_path):
    error_dir = tmp_path / "error"
    error_dir.mkdir()
    init = error_dir / "__init__.py"
    original = "from .foo import *\n"
    init.write_text(original)
    (error_dir / "foo.py").write_text("class Err:\n    pass\n")

    _fix_wildcard_exports(tmp_path)

    # error/__init__.py must not be touched
    assert init.read_text() == original


# ---------------------------------------------------------------------------
# _patch_service_files — auth header patch
# ---------------------------------------------------------------------------


def _make_service_dir(tmp_path: Path) -> Path:
    services = tmp_path / "services"
    services.mkdir(parents=True)
    return services


def test_patch_auth_header(tmp_path):
    svc = _make_service_dir(tmp_path)
    f = svc / "DeviceService.py"
    f.write_text(
        textwrap.dedent("""\
        headers = {
            "Authorization": f"Bearer {api_config.access_token}",
        }
        """)
    )

    _patch_service_files(tmp_path, set())

    content = f.read_text()
    assert "X-CH-Auth-Email" in content
    assert "X-CH-Auth-API-Token" in content
    assert "Authorization" not in content


# ---------------------------------------------------------------------------
# _patch_service_files — import alias patch
# ---------------------------------------------------------------------------


def test_patch_import_alias(tmp_path):
    svc = _make_service_dir(tmp_path)
    f = svc / "DeviceService.py"
    f.write_text(
        "from ..api_config import APIConfig, HTTPException\n"
        "def foo(): pass\n"
    )

    _patch_service_files(tmp_path, set())

    content = f.read_text()
    assert "from kentik_api.core.api_config import APIConfig" in content
    assert "from kentik_api.errors import HTTPException" in content


# ---------------------------------------------------------------------------
# _dedupe_top_level_function_names
# ---------------------------------------------------------------------------


def test_dedupe_function_names_renames_second_duplicate():
    content = textwrap.dedent("""\
        def List(a):
            pass

        def List(b):
            pass
        """)

    result = _dedupe_top_level_function_names(content)

    assert "def List(a):" in result
    assert "def List_2(b):" in result
    assert result.count("def List(") == 1


def test_dedupe_function_names_leaves_unique_names_unchanged():
    content = "def Foo():\n    pass\n\ndef Bar():\n    pass\n"
    assert _dedupe_top_level_function_names(content) == content


# ---------------------------------------------------------------------------
# _normalize_triple_quoted_docstrings
# ---------------------------------------------------------------------------


def test_normalize_docstrings_flattens_indentation():
    content = textwrap.dedent('''\
        class Foo:
            """
                Deeply indented.
                    More deeply.
            """
            pass
        ''')

    result = _normalize_triple_quoted_docstrings(content)

    # Both lines should end up at the same indent — the extra-deep line is flattened
    lines = [l for l in result.splitlines() if l.strip() in ("Deeply indented.", "More deeply.")]
    assert len(lines) == 2
    assert lines[0].startswith(" " * 8)  # class body (4) + inner (4)
    assert lines[0].rstrip() == lines[1].rstrip().replace("More deeply.", "Deeply indented.")


def test_normalize_docstrings_leaves_single_line_untouched():
    content = '    """Short docstring."""\n'
    assert _normalize_triple_quoted_docstrings(content) == content


# ---------------------------------------------------------------------------
# _patch_service_files — wildcard typing import
# ---------------------------------------------------------------------------


def test_patch_typing_wildcard_import(tmp_path):
    svc = _make_service_dir(tmp_path)
    f = svc / "DeviceService.py"
    f.write_text("from typing import *\ndef foo(): pass\n")

    _patch_service_files(tmp_path, set())

    content = f.read_text()
    assert "from typing import *" not in content
    assert "from typing import" in content


# ---------------------------------------------------------------------------
# fix_generated_service — smoke test (all three helpers run without error)
# ---------------------------------------------------------------------------


def test_fix_generated_service_smoke(tmp_path):
    models = tmp_path / "models"
    models.mkdir()
    (models / "__init__.py").write_text("")
    (models / "Device.py").write_text("class Device:\n    pass\n")
    services = tmp_path / "services"
    services.mkdir()
    (services / "DeviceService.py").write_text(
        "from ..api_config import APIConfig, HTTPException\ndef foo(): pass\n"
    )

    fix_generated_service(tmp_path)

    assert "Device as Device" in (models / "__init__.py").read_text()
    assert "from kentik_api.core.api_config import APIConfig" in (
        services / "DeviceService.py"
    ).read_text()
