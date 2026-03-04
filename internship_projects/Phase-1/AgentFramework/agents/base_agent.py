from abc import ABC, abstractmethod
class Agent(ABC):
    def handle(self, query: str) -> str: pass
