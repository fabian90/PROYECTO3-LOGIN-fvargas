from Interface.productoAnterior import IProducto
from Implementation.ingredientesAnterior import Ingrediente
from funciones import contar_calorias, calcular_costo, calcular_rentabilidad
from typing import List

class Producto(IProducto):
    def __init__(self, nombre: str, precio_venta: float, ingredientes: List[Ingrediente]):
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.ingredientes = ingredientes

    def calcular_calorias(self) -> float:
        calorias = [ingrediente.calorias for ingrediente in self.ingredientes]
        return contar_calorias(calorias)

    def calcular_costo(self) -> float:
        ingredientes_dicts = [{'nombre': ingrediente.nombre, 'precio': ingrediente.precio} for ingrediente in self.ingredientes]
        return calcular_costo(*ingredientes_dicts)

    def calcular_rentabilidad(self) -> float:
        ingredientes_dicts = [{'nombre': ingrediente.nombre, 'precio': ingrediente.precio} for ingrediente in self.ingredientes]
        return calcular_rentabilidad(self.precio_venta, *ingredientes_dicts)

    def verificar_ingredientes(self) -> bool:
        return all(ingrediente.inventario > 0 for ingrediente in self.ingredientes)

    def usar_ingredientes(self):
        for ingrediente in self.ingredientes:
            ingrediente.usar(1)

class Copa(Producto):
    def __init__(self, nombre: str, precio_venta: float, ingredientes: List[Ingrediente], tipo_vaso: str):
        super().__init__(nombre, precio_venta, ingredientes)
        self.tipo_vaso = tipo_vaso

class Malteada(Producto):
    def __init__(self, nombre: str, precio_venta: float, ingredientes: List[Ingrediente], volumen_onzas: float):
        super().__init__(nombre, precio_venta, ingredientes)
        self.volumen_onzas = volumen_onzas