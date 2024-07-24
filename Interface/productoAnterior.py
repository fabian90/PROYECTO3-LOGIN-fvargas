from abc import ABC, abstractmethod
from typing import List
from Implementation.ingredientesAnterior import IIngrediente

class IProducto(ABC):
    @abstractmethod
    def calcular_calorias(self) -> float:
        pass

    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    @abstractmethod
    def calcular_rentabilidad(self) -> float:
        pass

    @abstractmethod
    def verificar_ingredientes(self) -> bool:
        pass

    @abstractmethod
    def usar_ingredientes(self):
        pass