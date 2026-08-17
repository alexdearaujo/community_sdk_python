from abc import ABC, abstractmethod


class BaseTransport(ABC):
    @abstractmethod
    def close(self):
        pass
