from Implementation.productoService import ProductoService
from Implementation.ingredienteService import IngredienteService
from Implementation.productoIngredienteService import ProductoIngredienteService
from Implementation.tipoProductoService import TipoProductoService
from funciones import es_sano, contar_calorias, calcular_costo, calcular_rentabilidad
from db import db

class HeladeriaController:
    def __init__(self):
        self.ventas_del_dia = 0
        self.producto_service = ProductoService()
        self.ingrediente_service=IngredienteService()
        self.producto_ingrediente_service=ProductoIngredienteService()
        self.producto_tipo_service=TipoProductoService()
    def obtener_productos(self):
        """Obtiene la lista de productos con información adicional."""
        try:
            productos = self.producto_service.get_all_productos()
            productos_info = []

            for producto in productos:
                calorias_totales, es_sano = self.calcular_calorias_producto(producto.id)
                costo_produccion = self.calcular_costo_produccion(producto.id)
                rentabilidad = self.calcular_rentabilidad_producto(producto.id)

                productos_info.append({
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'tipo_producto': producto.tipo_producto.nombre_tipo_producto,
                    'precio_publico': producto.precio_publico,
                    'calorias_totales': calorias_totales,
                    'costo_produccion': costo_produccion,
                    'rentabilidad': rentabilidad,
                    'es_sano': es_sano
                })
            return productos_info
        except Exception as e:
            # Manejo de excepciones y logging del error
            print(f"Error al obtener los productos: {e}")
            return {"error": "No se pudieron obtener los productos."}
    def es_ingrediente_sano(self, ingrediente_id):
        """Verifica si un ingrediente es sano."""
        try:
            ingrediente = self.ingrediente_service.get_ingrediente(ingrediente_id)
            if ingrediente:
                if not es_sano(ingrediente.calorias, ingrediente.es_vegetariano):
                 return False
            return True
        except Exception as e:
            print(f"Error al verificar si el ingrediente es sano: {e}")
            return False
    def abastecer_ingrediente(self, ingrediente_id, cantidad):
        """Abastece un ingrediente específico."""
        try:
            ingrediente = self.ingrediente_service.get_ingrediente(ingrediente_id)
            if ingrediente:
                nuevo_inventario = ingrediente.inventario + cantidad
                self.ingrediente_service.update_ingrediente(ingrediente_id, inventario=nuevo_inventario)
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(f"Error al abastecer el ingrediente: {e}")
            return False

    def renovar_inventario_complementos(self):
        """Renueva el inventario de todos los complementos."""
        try:
            complementos = self.ingrediente_service.get_by_complemento('COMPLEMENTO')
            if complementos:
                for complemento in complementos:
                    self.ingrediente_service.update_ingrediente(complemento.id, inventario=complemento.inventario + 10)  # Asumiendo que la renovación es de 10 unidades
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(f"Error al renovar el inventario de complementos: {e}")
            return False

    def calcular_calorias_producto(self, producto_id):
        """Calcula las calorías de un producto dado su ID."""
        try:
            producto = self.producto_service.get_producto(producto_id)
            if not producto:
                return 0
            calorias_ingredientes = []
            producto_ingredientes = self.producto_ingrediente_service.get_producto_ingrediente_by_producto_id(producto_id)
            for pi in producto_ingredientes:
                ingrediente = self.ingrediente_service.get_ingrediente(pi.id_ingrediente)
                if ingrediente:
                    calorias_ingredientes.append(ingrediente.calorias)
                    if producto.tipo_producto.nombre_tipo_producto == 'malteada':
                        calorias_ingredientes.append(200)  # Añade 200 calorías por la crema chantilly
            total_calorias=contar_calorias(calorias_ingredientes)
            sano = es_sano(total_calorias)
            return (total_calorias,sano)
        except Exception as e:
            print(f"Error al calcular las calorías del producto: {e}")
            return 0

    def calcular_costo_produccion(self, producto_id):
        """Calcula el costo de producción de un producto dado su ID."""
        try:
            producto_ingredientes = self.producto_ingrediente_service.get_producto_ingrediente_by_producto_id(producto_id)
            costo_ingredientes = []
            for pi in producto_ingredientes:
                ingrediente = self.ingrediente_service.get_ingrediente(pi.id_ingrediente)
                if ingrediente:
                    costo_ingredientes.append(ingrediente.precio)
            producto = self.producto_service.get_producto(producto_id)
            if producto.tipo_producto.nombre_tipo_producto == 'malteada':
                costo_ingredientes.append(500)  # Costo del vaso plástico
            return calcular_costo(costo_ingredientes)
        except Exception as e:
            print(f"Error al calcular el costo de producción: {e}")
            return 0

    def calcular_rentabilidad_producto(self, producto_id):
        """Calcula la rentabilidad de un producto dado su ID."""
        try:
            producto = self.producto_service.get_producto(producto_id)
            if producto:
                costo_produccion = self.calcular_costo_produccion(producto_id)
                return calcular_rentabilidad(producto.precio_publico, costo_produccion)
            return None
        except Exception as e:
            print(f"Error al calcular la rentabilidad del producto: {e}")
            return None

    def producto_mas_rentable(self):
        """Encuentra el producto más rentable."""
        try:
            productos = self.producto_service.get_all_productos()
            max_rentabilidad = -float('inf')
            producto_mas_rentable = None
            for producto in productos:
                rentabilidad = self.calcular_rentabilidad_producto(producto.id)
                if rentabilidad > max_rentabilidad:
                    max_rentabilidad = rentabilidad
                    producto_mas_rentable = producto
            return producto_mas_rentable.nombre if producto_mas_rentable else None
        except Exception as e:
            print(f"Error al encontrar el producto más rentable: {e}")
            return None

    def vender_producto(self, producto_id):
        """Vende un producto dado su ID si hay suficientes ingredientes."""
        try:
            producto = self.producto_service.get_producto(producto_id)
            if not producto:
                raise ValueError("Producto no encontrado")

            producto_ingredientes = self.producto_ingrediente_service.get_producto_ingrediente_by_producto_id(producto_id)

            # Verifica si hay suficientes ingredientes
            for pi in producto_ingredientes:
                ingrediente = self.ingrediente_service.get_ingrediente(pi.id_ingrediente)
                if ingrediente:
                    # Determina la cantidad necesaria según el tipo de ingrediente
                    cantidad_necesaria = 1 if ingrediente.tipo == 'COMPLEMNETO' else 0.2
                    if ingrediente.inventario < cantidad_necesaria:
                        raise ValueError(ingrediente.nombre)  # Lanza ValueError con el nombre del ingrediente faltante

            # Actualiza inventario de los ingredientes
            for pi in producto_ingredientes:
                ingrediente = self.ingrediente_service.get_ingrediente(pi.id_ingrediente)
                if ingrediente:
                    cantidad_necesaria = 1 if ingrediente.tipo == 'COMPLEMENTO' else 0.2
                    nuevo_inventario = ingrediente.inventario - cantidad_necesaria
                    self.ingrediente_service.update_ingrediente(ingrediente.id, inventario=nuevo_inventario)

            # Suma a las ventas del día
            self.ventas_del_dia += producto.precio_publico
            db.session.commit()
            return "¡Vendido!"  # Retorna "¡Vendido!" si la venta es exitosa
        except ValueError as e:
            raise e
        except Exception as e:
            print(f"Error al vender el producto: {e}")
            return False        
        
    def get_ventas_del_dia(self):
        """Devuelve el total de ventas del día."""
        return self.ventas_del_dia