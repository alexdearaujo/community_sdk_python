# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

from dataclasses import dataclass

__all__ = ["RateLimit"]


@dataclass(frozen=True)
class RateLimit:
    """Quota the API reported on one response, as of that response.

    Each field is `None` when the server omitted it rather than a guessed
    default, because the API advertises only the per-minute window: the
    concurrency cap, soft-limit delay, and hourly limit never reach a header.
    """

    limit: int | None
    remaining: int | None
    reset_seconds: int | None
    window_seconds: int | None
    raw: str | None
