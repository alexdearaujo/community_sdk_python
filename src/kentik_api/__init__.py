# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from typing import TYPE_CHECKING, Any

from .core.rate_limit import RateLimit, rate_limit_of

if TYPE_CHECKING:
    from .client import KentikAPI as KentikAPI

__all__ = ["KentikAPI", "RateLimit", "rate_limit_of"]


def __getattr__(name: str) -> Any:
    # Lazy, so importing the package does not load every generated service.
    if name == "KentikAPI":
        from .client import KentikAPI

        return KentikAPI
    raise AttributeError(name)
