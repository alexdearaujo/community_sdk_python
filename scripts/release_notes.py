# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Renders release notes by diffing `api_surface.json` against an earlier git revision.

`make generate` refreshes `api_surface.json` on every run, and it is committed, so
comparing two points in history costs one `git show`. That keeps this command
idempotent: rerunning it never consumes or advances a baseline, unlike a snapshot
file that gets overwritten as a side effect of generation.

    uv run python scripts/release_notes.py                 # since the latest tag
    uv run python scripts/release_notes.py --since v1.0.6
    uv run python scripts/release_notes.py --since HEAD    # just this working tree
    uv run python scripts/release_notes.py -o notes.md
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from generation import api_surface  # noqa: E402
from generation._shared import PROJECT_ROOT  # noqa: E402

SURFACE_RELPATH = "api_surface.json"


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=PROJECT_ROOT, capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def latest_tag() -> str:
    try:
        return _git("describe", "--tags", "--abbrev=0")
    except RuntimeError as exc:
        raise SystemExit(
            "No git tag found to compare against. Pass --since <ref> explicitly."
        ) from exc


def surface_at(ref: str) -> dict:
    try:
        return json.loads(_git("show", f"{ref}:{SURFACE_RELPATH}"))
    except RuntimeError as exc:
        raise SystemExit(
            f"`{SURFACE_RELPATH}` does not exist at `{ref}`. This is expected for "
            "revisions predating surface tracking; pick a later ref, or run "
            "`make generate` on that revision to create one."
        ) from exc


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        metavar="REF",
        help="git ref to compare against (default: most recent tag)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="write markdown here instead of stdout",
    )
    args = parser.parse_args()

    since = args.since or latest_tag()
    before = surface_at(since)

    surface_path = PROJECT_ROOT / SURFACE_RELPATH
    if not surface_path.exists():
        raise SystemExit(f"{SURFACE_RELPATH} is missing. Run `make generate` first.")
    after = api_surface.read(surface_path)

    markdown = api_surface.render_markdown(api_surface.diff(before, after), since=since)

    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
        print(f"Wrote release notes for changes since {since} to {args.output}")
    else:
        print(markdown, end="")


if __name__ == "__main__":
    main()
