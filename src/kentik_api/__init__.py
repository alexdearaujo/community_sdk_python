# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .client import KentikAPI as KentikAPI

__all__ = ["KentikAPI"]


def __getattr__(name: str) -> Any:
    if name == "KentikAPI":
        from .client import KentikAPI

        return KentikAPI
    raise AttributeError(name)
