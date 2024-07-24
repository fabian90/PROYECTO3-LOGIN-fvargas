from Interface.ingredienteAnterior import IIngrediente
from funciones import es_sano

class Ingrediente(IIngrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, es_vegetariano: bool):
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias
        self.inventario = inventario
        self.es_vegetariano = es_vegetariano

    def es_sano(self) -> bool:
        return es_sano(self.calorias, self.es_vegetariano)

    def reabastecer(self, cantidad: int):
        self.inventario += cantidad

    def usar(self, cantidad: int):
        pass  # Será implementado en las clases derivadas

class Base(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, es_vegetariano: bool, sabor: str):
        super().__init__(nombre, precio, calorias, inventario, es_vegetariano)
        self.sabor = sabor

    def usar(self, cantidad: int):
        self.inventario -= cantidad

class Complemento(Ingrediente):
    def bajar_inventario_a_cero(self):
        self.inventario = 0

    def usar(self, cantidad: int):
        self.inventario -= cantidad