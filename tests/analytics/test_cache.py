# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
"""DFCache stores Parquet by time range and fetches only what it lacks (FR-019)."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from pathlib import Path

import pandas as pd
import pytest

from kentik_api.analytics import DFCache, dedup_data_frame

START = datetime(2025, 10, 16, tzinfo=UTC)


def _frame(start: datetime, end: datetime) -> pd.DataFrame:
    index = pd.date_range(start, end, freq="1min", inclusive="left", name="ts")
    return pd.DataFrame({"link": "router1:eth0", "bps": range(len(index))}, index=index)


class _Query:
    def __init__(self):
        self.calls: list[tuple[datetime, datetime]] = []

    def __call__(self, *, start, end):
        self.calls.append((start, end))
        return _frame(start, end)


def test_fetch_stores_parquet_files_and_returns_the_range(tmp_path: Path):
    cache = DFCache(tmp_path)
    query = _Query()

    df = cache.fetch(query, START, START + timedelta(hours=2), step=timedelta(hours=1))

    assert len(query.calls) == 2
    assert df is not None and len(df) == 120
    assert all(path.suffix == ".parquet" for path in cache.files)
    assert cache.file_count == 2


def test_a_second_fetch_fetches_only_the_missing_steps(tmp_path: Path):
    cache = DFCache(tmp_path)
    cache.fetch(_Query(), START, START + timedelta(hours=1), step=timedelta(hours=1))
    query = _Query()

    df = cache.fetch(query, START, START + timedelta(hours=3), step=timedelta(hours=1))

    assert query.calls == [
        (START + timedelta(hours=1), START + timedelta(hours=2)),
        (START + timedelta(hours=2), START + timedelta(hours=3)),
    ]
    assert df is not None
    assert len(df) == 180


def test_a_fetch_without_step_skips_a_cached_range(tmp_path: Path):
    cache = DFCache(tmp_path)
    cache.fetch(_Query(), START, START + timedelta(hours=2))
    query = _Query()

    df = cache.fetch(query, START, START + timedelta(hours=1))

    assert query.calls == []
    assert df is not None
    assert len(df) == 61


def test_fetch_removes_duplicate_rows(tmp_path: Path):
    cache = DFCache(tmp_path)
    cache.store(_frame(START, START + timedelta(minutes=30)))
    query = _Query()

    df = cache.fetch(
        query,
        START + timedelta(minutes=20),
        START + timedelta(minutes=50),
        dedup_columns=["ts", "link"],
    )

    assert query.calls == [
        (START + timedelta(minutes=20), START + timedelta(minutes=50))
    ]
    assert df is not None
    assert df.index.is_unique
    assert len(df) == 30


def test_get_removes_duplicate_rows(tmp_path: Path):
    cache = DFCache(tmp_path)
    cache.store(_frame(START, START + timedelta(minutes=30)))
    cache.store(_frame(START + timedelta(minutes=20), START + timedelta(minutes=50)))

    df = cache.get(dedup_columns=["ts", "link"])

    assert df is not None
    assert df.index.is_unique
    assert len(df) == 50


def test_files_the_cache_did_not_write_are_ignored(tmp_path: Path):
    (tmp_path / "notes.parquet").write_bytes(b"not parquet")
    (tmp_path / "evil.pickle").write_bytes(b"\x80\x04K.")
    (tmp_path / "a_b.parquet").write_bytes(b"not parquet either")
    cache = DFCache(tmp_path)

    assert cache.is_empty
    assert cache.get() is None


def test_file_names_have_no_colon(tmp_path: Path):
    # Windows does not allow `:` in a file name.
    cache = DFCache(tmp_path)
    cache.store(_frame(START, START + timedelta(minutes=2)))

    assert [p.name for p in cache.files] == [
        "2025-10-16T00_00_00+00_00_2025-10-16T00_01_00+00_00.parquet"
    ]


@pytest.mark.parametrize(
    ("name", "start", "end"),
    [
        # Written before file names avoided `:`, on macOS or Linux.
        (
            "2025-10-16T00:00:00+00:00_2025-10-16T01:00:00+00:00.parquet",
            START,
            START + timedelta(hours=1),
        ),
        (
            "2025-10-16T00_00_00_2025-10-16T01_00_00.parquet",
            START.replace(tzinfo=None),
            START.replace(tzinfo=None) + timedelta(hours=1),
        ),
    ],
)
def test_file_names_parse_with_or_without_colons(name: str, start, end):
    assert DFCache.parse_df_filename(Path(name)) == (start, end)


def test_dedup_needs_the_named_columns():
    with pytest.raises(ValueError, match="not in the DataFrame"):
        dedup_data_frame(_frame(START, START + timedelta(minutes=2)), ["nope"])
