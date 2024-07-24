def es_sano(calorias: int) -> bool:
    """Determina si un producto es sano basado en las calorías."""
    return calorias < 100

def contar_calorias(ingredientes: list[int]) -> float:
    """Calcula el conteo de calorías de un producto."""
    total_calorias = sum(ingredientes) * 0.95
    return round(total_calorias, 2)

def calcular_costo(ingredientes: list[int]) -> int:
    """Calcula el costo de producir un producto."""
    total_precio = sum(ingredientes)
    return total_precio

def calcular_rentabilidad(precio_venta: int, total_costo: int  ) -> int:
    """Calcula la rentabilidad de un producto."""
    return precio_venta - total_costo

def producto_mas_rentable(producto1: dict, producto2: dict, producto3: dict, producto4: dict) -> str:
    """Encuentra el producto más rentable."""
    productos = [producto1, producto2, producto3, producto4]
    productos.sort(key=lambda x: x['rentabilidad'], reverse=True)
    return productos[0]['nombre']