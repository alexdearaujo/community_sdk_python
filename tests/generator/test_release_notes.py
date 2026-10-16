# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Tests for the CHANGELOG check in scripts/release_notes.py."""

from __future__ import annotations

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
