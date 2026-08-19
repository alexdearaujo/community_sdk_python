# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Shared helpers for SDK examples."""

import json
from typing import Any


def pretty_print(obj: Any) -> None:
    """Print a Pydantic model or plain value as indented JSON."""
    if hasattr(obj, "model_dump"):
        print(json.dumps(obj.model_dump(), indent=2, default=str))
    elif isinstance(obj, list):
        print(
            json.dumps(
                [o.model_dump() if hasattr(o, "model_dump") else o for o in obj],
                indent=2,
                default=str,
            )
        )
    else:
        print(obj)
