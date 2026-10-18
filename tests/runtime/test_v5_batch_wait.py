# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
"""wait_for_batch() polls the status until the batch completes (spec 005, FR-012)."""

from __future__ import annotations

from types import SimpleNamespace
from typing import cast

import pytest

from kentik_api import v5_tools
from kentik_api.client import KentikAPI
from kentik_api.errors import HTTPException
from kentik_api.gen.v5.models import BatchStatus
from kentik_api.v5_tools import BatchWaitTimeout, wait_for_batch


class _Clock:
    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def monotonic(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


@pytest.fixture
def clock(monkeypatch: pytest.MonkeyPatch) -> _Clock:
    fake = _Clock()
    monkeypatch.setattr(v5_tools, "time", fake)
    return fake


def _client(statuses):
    answers = iter(statuses)

    def batch_status(*, guid):
        answer = next(answers)
        if isinstance(answer, Exception):
            raise answer
        return answer

    return cast(
        KentikAPI, SimpleNamespace(v5=SimpleNamespace(batch_status=batch_status))
    )


def test_returns_the_status_once_the_batch_is_complete(clock):
    done = BatchStatus(guid="g", is_complete=True)
    client = _client([BatchStatus(guid="g", is_complete=False), done])

    assert wait_for_batch(client, "g", timeout=60, interval=5) is done
    assert clock.sleeps == [5]


def test_raises_with_the_last_status_when_the_time_limit_expires(clock):
    pending = BatchStatus(guid="g", is_complete=False, number_of_parts=2)
    client = _client([pending] * 10)

    with pytest.raises(BatchWaitTimeout) as exc:
        wait_for_batch(client, "g", timeout=12, interval=5)

    assert exc.value.guid == "g"
    assert exc.value.last_status is pending
    assert clock.sleeps == [5, 5, 2]


def test_a_failed_status_call_raises_at_once(clock):
    client = _client([HTTPException(404, "Could not find this batch")])

    with pytest.raises(HTTPException):
        wait_for_batch(client, "g", timeout=60, interval=5)
    assert clock.sleeps == []
