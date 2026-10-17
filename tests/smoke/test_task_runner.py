# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
"""Facts about the poe task table and the files that agents read (spec 007)."""

from __future__ import annotations

import shlex
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any

import pytest

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


def _dry_run(*argv: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, "-m", "poethepoet", "--no-ansi", "-d", *argv],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    line = next(
        x
        for x in (result.stdout + result.stderr).splitlines()
        if x.startswith("Poe => ")
    )
    return shlex.split(line.removeprefix("Poe => "))[2:]


@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        (["generate"], []),
        (["generate", "--local"], ["--local-repo", "../api-schema-public/"]),
        (["generate", "--local-repo", "a b/c"], ["--local-repo", "a b/c"]),
        (["generate", "--schema-ref", "REF"], ["--schema-ref", "REF"]),
        (
            ["check-changelog", "--since", "REF"],
            ["--check-changelog", "--since", "REF"],
        ),
        (
            ["release-notes", "--since", "REF", "--out", "o.md"],
            ["--since", "REF", "-o", "o.md"],
        ),
        (
            ["impact-report", "--since", "REF", "--no-checks", "--out", "o.html"],
            ["--since", "REF", "--no-checks", "-o", "o.html"],
        ),
    ],
)
def test_task_options_reach_the_program(argv: list[str], expected: list[str]):
    # Each Make variable became an option; a value with a space stays one argument.
    assert _dry_run(*argv) == expected
