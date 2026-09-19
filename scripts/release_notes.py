# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Renders release notes by diffing `api_surface.json` against an earlier git revision.

`make generate` refreshes `api_surface.json` on every run, and it is committed, so
comparing two points in history costs one `git show`. That keeps this command
idempotent: rerunning it never consumes or advances a baseline, unlike a snapshot
file that gets overwritten as a side effect of generation.

    uv run python scripts/release_notes.py                 # since newest tag with a record
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


def _surface_at(ref: str) -> dict | None:
    """Returns the recorded surface at ref, or None if that revision has no record."""
    try:
        return json.loads(_git("show", f"{ref}:{SURFACE_RELPATH}"))
    except RuntimeError:
        return None


def _tags_newest_first() -> list[str]:
    try:
        tags = _git("tag", "--sort=-creatordate")
    except RuntimeError:
        return []
    return [tag for tag in tags.splitlines() if tag.strip()]


def _default_baseline() -> tuple[str, dict] | None:
    """Finds the most recent tag that actually carries a surface record.

    Tags predating surface tracking have no record, so the newest tag is often not
    a usable baseline. Skipping to the newest one that is beats failing outright.
    """
    for tag in _tags_newest_first():
        surface = _surface_at(tag)
        if surface is not None:
            return tag, surface
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since",
        metavar="REF",
        help="git ref to compare against (default: newest tag carrying a surface record)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="write markdown here instead of stdout",
    )
    args = parser.parse_args()

    surface_path = PROJECT_ROOT / SURFACE_RELPATH
    if not surface_path.exists():
        raise SystemExit(f"{SURFACE_RELPATH} is missing. Run `make generate` first.")
    after = api_surface.read(surface_path)

    if args.since:
        before = _surface_at(args.since)
        if before is None:
            raise SystemExit(
                f"`{SURFACE_RELPATH}` does not exist at `{args.since}`, so there is "
                "nothing to compare against. That revision predates surface "
                "tracking. Pick a later ref, or omit --since to use the newest "
                "tag that has a record."
            )
        markdown = api_surface.render_markdown(
            api_surface.diff(before, after), since=args.since
        )
    else:
        baseline = _default_baseline()
        if baseline is None:
            # First release since tracking landed: summarise rather than fail.
            print(
                "No tagged release carries a surface record yet, so there is no "
                "baseline to diff against. Showing the current surface instead.\n"
                "Future releases will produce a change list automatically.",
                file=sys.stderr,
            )
            markdown = api_surface.render_summary(after)
        else:
            since, before = baseline
            print(f"Comparing against {since}", file=sys.stderr)
            markdown = api_surface.render_markdown(
                api_surface.diff(before, after), since=since
            )

    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
        print(f"Wrote release notes to {args.output}", file=sys.stderr)
    else:
        print(markdown, end="")


if __name__ == "__main__":
    main()
