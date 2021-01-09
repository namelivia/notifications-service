from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def send(message: str):
        pass
