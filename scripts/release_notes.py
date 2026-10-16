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
    uv run python scripts/release_notes.py --check-changelog --since origin/main

`--check-changelog` prints nothing on success. It exits 1 when a breaking change
since the baseline has no mention in CHANGELOG.md's Unreleased section.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from generation import api_surface  # noqa: E402
from generation._shared import PROJECT_ROOT  # noqa: E402

SURFACE_RELPATH = "api_surface.json"
CHANGELOG = PROJECT_ROOT / "CHANGELOG.md"


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=PROJECT_ROOT, capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


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
    A tag on HEAD is skipped too: the release workflow runs on the tag it is
    describing, and comparing a release with itself lists nothing.
    """
    head = _git("rev-parse", "HEAD")
    for tag in _tags_newest_first():
        if _git("rev-list", "-n", "1", tag) == head:
            continue
        surface = api_surface.recorded_at(tag)
        if surface is not None:
            return tag, surface
    return None


def _unreleased_notes() -> str:
    text = CHANGELOG.read_text(encoding="utf-8")
    match = re.search(r"^## Unreleased\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1) if match else ""


def _mentioned(name: str, notes: str) -> bool:
    """True when a code span in the notes holds `name` as a whole token.

    A bare substring would let prose such as "user credentials" satisfy a
    removed `user` service.
    """
    token = re.compile(rf"(?<![\w]){re.escape(name)}(?![\w])")
    return any(token.search(span) for span in re.findall(r"`([^`]+)`", notes))


def _check_changelog(delta: dict, since: str) -> None:
    notes = _unreleased_notes()
    missing = [
        (message, name)
        for message, name in api_surface.breaking_changes(delta)
        if not _mentioned(name, notes)
    ]
    if not missing:
        return
    print(
        f"CHANGELOG.md's Unreleased section does not mention these breaking "
        f"changes since `{since}`. Add an entry that names each one:",
        file=sys.stderr,
    )
    for message, name in missing:
        print(f"{message}  (mention `{name}`)", file=sys.stderr)
    raise SystemExit(1)


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
    parser.add_argument(
        "--check-changelog",
        action="store_true",
        help="fail if CHANGELOG.md does not mention every breaking change",
    )
    args = parser.parse_args()

    surface_path = PROJECT_ROOT / SURFACE_RELPATH
    if not surface_path.exists():
        raise SystemExit(f"{SURFACE_RELPATH} is missing. Run `make generate` first.")
    after = api_surface.read(surface_path)

    if args.since:
        before = api_surface.recorded_at(args.since)
        baseline = None if before is None else (args.since, before)
    else:
        baseline = _default_baseline()

    if args.check_changelog:
        if baseline is None:
            # Nothing to compare yet, which is not a missing CHANGELOG entry.
            print(
                f"No surface record at `{args.since or 'any tag'}`, so there is "
                "nothing to check.",
                file=sys.stderr,
            )
            return
        since, before = baseline
        _check_changelog(api_surface.diff(before, after), since)
        return

    if baseline is not None:
        since, before = baseline
        print(f"Comparing against {since}", file=sys.stderr)
        markdown = api_surface.render_markdown(
            api_surface.diff(before, after), since=since
        )
    elif args.since:
        raise SystemExit(
            f"`{SURFACE_RELPATH}` does not exist at `{args.since}`, so there is "
            "nothing to compare against. That revision predates surface "
            "tracking. Pick a later ref, or omit --since to use the newest "
            "tag that has a record."
        )
    else:
        # First release since tracking landed: summarise rather than fail.
        print(
            "No tagged release carries a surface record yet, so there is no "
            "baseline to diff against. Showing the current surface instead.\n"
            "Future releases will produce a change list automatically.",
            file=sys.stderr,
        )
        markdown = api_surface.render_summary(after)

    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
        print(f"Wrote release notes to {args.output}", file=sys.stderr)
    else:
        print(markdown, end="")


if __name__ == "__main__":
    main()
