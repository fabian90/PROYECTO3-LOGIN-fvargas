from Implementation.productosAnterior import Producto
from Implementation.ingredientesAnterior import Ingrediente
from funciones import producto_mas_rentable

class Heladeria:
    def __init__(self):
        self.productos = []
        self.ingredientes = []
        self.contador_ventas = 0

    def agregar_producto(self, producto: Producto):
        if len(self.productos) < 4:
            self.productos.append(producto)
        else:
            print("La heladería ya tiene 4 productos.")

    def agregar_ingrediente(self, ingrediente: Ingrediente):
        self.ingredientes.append(ingrediente)

    def producto_mas_rentable(self) -> Producto:
        if len(self.productos) < 4:
            print("Debe haber al menos 4 productos para determinar el más rentable.")
            return None

        productos_dicts = [{'nombre': producto.nombre, 'rentabilidad': producto.calcular_rentabilidad()} for producto in self.productos]
        nombre_producto_mas_rentable = producto_mas_rentable(productos_dicts[0], productos_dicts[1], productos_dicts[2], productos_dicts[3])
        return next(producto for producto in self.productos if producto.nombre == nombre_producto_mas_rentable)

    def vender_producto(self, nombre_producto: str)-> bool:
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if not producto:
            print(f"No se encontró el producto {nombre_producto}.")
            return None

        if producto.verificar_ingredientes():
            producto.usar_ingredientes()
            self.contador_ventas += 1
        else:
            print(f"No hay suficiente inventario para el producto {nombre_producto}.")