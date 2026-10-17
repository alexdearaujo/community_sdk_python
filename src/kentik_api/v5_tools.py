# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Helpers for the V5-backed `client.v5` calls.

They call the generated operations and never send HTTP themselves, so every
request still goes through the shared runtime.
"""

from __future__ import annotations

import base64
import binascii
import re
from dataclasses import dataclass

from kentik_api.errors import HTTPException
from kentik_api.gen.v5.models import ChartResponse

_DATA_URI = re.compile(r"data:(?P<mime>[^;,]+)(?:;[^;,]+)*;base64,(?P<data>.*)", re.S)


@dataclass(frozen=True)
class ChartImage:
    image_type: str
    """The MIME type, for example `image/png` or `image/svg+xml`."""
    data: bytes


def decode_chart(response: ChartResponse) -> ChartImage:
    """Decodes the data URI of a `client.v5.top_x_chart` response."""
    if not response.dataUri:
        raise _unusable("no data URI")
    match = _DATA_URI.fullmatch(response.dataUri)
    if match is None:
        raise _unusable("not a base64 data URI")
    try:
        data = base64.b64decode(match["data"], validate=True)
    except binascii.Error:
        raise _unusable("not valid base64") from None
    return ChartImage(match["mime"], data)


def _unusable(problem: str) -> HTTPException:
    # Same status as any other unusable success body (see rest_runtime).
    return HTTPException(
        502,
        f"TopXChart returned an unusable chart: {problem}.",
        details={"problem": problem},
    )
