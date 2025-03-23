from abc import ABC, abstractmethod
from app.domain.item import Item

class IItem(ABC):
    @abstractmethod
    def find(self, name) -> Item:
        pass
    @abstractmethod
    def all(self) -> list[Item]:
        pass
    @abstractmethod
    def create(self, item) -> Item:
        pass