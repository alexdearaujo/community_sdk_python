# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from abc import ABC, abstractmethod


class BaseTransport(ABC):
    @abstractmethod
    def close(self):
        pass
