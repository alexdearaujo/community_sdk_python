# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Tests for the CHANGELOG check in scripts/release_notes.py."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import pytest

from scripts import release_notes

_DELTA = release_notes.api_surface.diff(
    {
        "services": {
            "kmeta": {
                "mounted": True,
                "operations": {},
                "models": [],
                "fields": {"Config": {"vaultId": {"type": "str", "required": False}}},
                "enums": {},
            }
        }
    },
    {
        "services": {
            "kmeta": {
                "mounted": True,
                "operations": {},
                "models": [],
                "fields": {"Config": {}},
                "enums": {},
            }
        }
    },
)


def _changelog(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, text: str) -> None:
    path = tmp_path / "CHANGELOG.md"
    path.write_text(text, encoding="utf-8")
    monkeypatch.setattr(release_notes, "CHANGELOG", path)


def _copy_device_service_tree(tmp_path: Path, side: str) -> Path:
    repo_root = Path(__file__).resolve().parents[2]
    source = repo_root / "src" / "kentik_api" / "gen" / "device"
    target = tmp_path / side / "device"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__"))
    return target


def test_check_passes_when_unreleased_names_the_change(tmp_path, monkeypatch):
    _changelog(tmp_path, monkeypatch, "## Unreleased\n\n- `Config.vaultId` is gone\n")

    release_notes._check_changelog(_DELTA, "v1.0.7")


def test_check_fails_naming_what_to_mention(tmp_path, monkeypatch, capsys):
    _changelog(
        tmp_path,
        monkeypatch,
        "## Unreleased\n\n- nothing here\n\n## 1.0.7\n\n- `Config.vaultId` once\n",
    )

    with pytest.raises(SystemExit) as exc:
        release_notes._check_changelog(_DELTA, "v1.0.7")

    assert exc.value.code == 1
    assert "(mention `Config.vaultId`)" in capsys.readouterr().err


def test_surface_breaking_changes_include_operation_signature_breaks(tmp_path):
    _copy_device_service_tree(tmp_path, "before")
    after = _copy_device_service_tree(tmp_path, "after")

    rest = after / "services" / "DeviceService.py"
    source = rest.read_text(encoding="utf-8")

    source = source.replace(
        "    querynoCustomColumns: Optional[bool] = None,\n"
        "    view: Optional[str] = None,\n"
        ") -> ListDevicesResponse:",
        "    querynoCustomColumns: Optional[bool] = None,\n) -> ListDevicesResponse:",
        1,
    )
    source = re.sub(
        r"(def GetDeviceByName\(.*?querynoCustomColumns: )Optional\[bool\]",
        r"\1Optional[str]",
        source,
        count=1,
        flags=re.S,
    )
    source = re.sub(
        r"(def GetDevice\(.*?\) -> )GetDeviceResponse:",
        r"\1DeviceConcise:",
        source,
        count=1,
        flags=re.S,
    )
    rest.write_text(source, encoding="utf-8")

    delta = release_notes.api_surface.diff(
        release_notes.api_surface.capture(tmp_path / "before"),
        release_notes.api_surface.capture(tmp_path / "after"),
    )
    breaking = release_notes.api_surface.breaking_changes(delta)

    assert breaking, (
        "operation signature changes must be treated as breaking so the release "
        "gate cannot miss optional-parameter, type, or return-model drift"
    )


def test_check_changelog_rejects_substring_only_mentions(tmp_path, monkeypatch, capsys):
    delta = release_notes.api_surface.diff(
        {
            "services": {
                "user": {
                    "mounted": True,
                    "operations": {},
                    "models": [],
                    "fields": {},
                    "enums": {},
                }
            }
        },
        {"services": {}},
    )
    _changelog(
        tmp_path,
        monkeypatch,
        "## Unreleased\n\n- Documented how to pass user credentials.\n",
    )

    with pytest.raises(SystemExit) as exc:
        release_notes._check_changelog(delta, "v2.0.0")

    assert exc.value.code == 1
    assert "breaking changes" in capsys.readouterr().err
