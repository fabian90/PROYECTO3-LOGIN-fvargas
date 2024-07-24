from abc import ABC, abstractmethod

class IIngrediente(ABC):
    @abstractmethod
    def es_sano(self) -> bool:
        pass

    @abstractmethod
    def reabastecer(self, cantidad: int):
        pass

    @abstractmethod
    def usar(self, cantidad: int):
        pass