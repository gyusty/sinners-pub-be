from abc import ABC, abstractmethod
from app.domain.order import Order

class IOrder(ABC):
    @abstractmethod
    def find(self, name) -> Order:
        pass
    @abstractmethod
    def all(self) -> list[Order]:
        pass
    @abstractmethod
    def create(self, order) -> Order:
        pass