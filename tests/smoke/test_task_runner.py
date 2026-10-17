# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
"""Facts about the poe task table and the files that agents read (spec 007)."""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _poe() -> dict[str, Any]:
    with (ROOT / "pyproject.toml").open("rb") as f:
        return tomllib.load(f)["tool"]["poe"]


def _keys(node: object) -> set[str]:
    if isinstance(node, dict):
        return set(node) | {k for v in node.values() for k in _keys(v)}
    if isinstance(node, list):
        return {k for v in node for k in _keys(v)}
    return set()


def test_every_task_has_help():
    tasks = _poe()["tasks"]
    assert tasks
    for name, task in tasks.items():
        assert isinstance(task, dict), f"{name} has no table, so it has no help"
        help_text = task.get("help", "")
        assert help_text.strip(), f"{name} has no help"
        assert "\n" not in help_text, f"{name} help is longer than one line"


def test_no_task_loads_an_env_file():
    # .env holds real credentials; KentikAPI reads it into a dict on purpose.
    assert "envfile" not in _keys(_poe())


def test_no_task_uses_a_shell():
    for name, task in _poe()["tasks"].items():
        assert "shell" not in task, f"{name} needs a shell, which Windows lacks"
