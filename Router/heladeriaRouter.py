from flask import Blueprint, render_template, request, jsonify
from flask import Blueprint, request, jsonify
from Controllers.heladeriaController import HeladeriaController
from flask_login import login_required, current_user

heladeria_bp = Blueprint('heladeria', __name__)
heladeria_controller = HeladeriaController()

@heladeria_bp.route('/')

def index():
    try:
        productos = heladeria_controller.obtener_productos()
        producto_mas_rentable = heladeria_controller.producto_mas_rentable()
        if "error" in productos:
            return render_template('index.html', error=productos["error"])
        return render_template('index.html', productos=productos, producto_mas_rentable=producto_mas_rentable, usuario=current_user)
    except Exception as e:
        print(f"Error inesperado: {e}")
        return render_template('index.html', error="Error inesperado al cargar la página.")

@heladeria_bp.route('/producto/vender/<int:producto_id>', methods=['POST'])
@login_required
def vender_producto(producto_id):
    try:
        # Llama al método vender_producto del controlador
        resultado = heladeria_controller.vender_producto(producto_id)
        
        # Verifica el resultado y obtiene las ventas del día
        if resultado == "¡Vendido!":
            # Obtén las ventas del día como un atributo y conviértelo a string
            ventas_del_dia = heladeria_controller.get_ventas_del_dia()  # Asegúrate de que es un método, no un atributo
            return jsonify({
                "message": resultado,
                "ventas_del_dia": str(ventas_del_dia)  # Convierte Decimal a string
            }), 200
        else:
            return jsonify({"message": "Error desconocido al vender el producto"}), 400
    except ValueError as e:
        return jsonify({"message": f"¡Oh no! Nos hemos quedado sin {str(e)}"}), 400
    except Exception as e:
        return jsonify({"message": f"Error inesperado: {str(e)}"}), 500

@heladeria_bp.route('/producto/calorias/<int:producto_id>')
@login_required
def calcular_calorias_producto(producto_id):
    try:
        calorias = heladeria_controller.calcular_calorias_producto(producto_id)
        return jsonify({'calorias': calorias})
    except Exception as e:
        return jsonify({'mensaje': f'Error al calcular las calorías del producto: {e}'}), 500

@heladeria_bp.route('/producto/costo/<int:producto_id>')
@login_required
def calcular_costo_produccion(producto_id):
    try:
        costo = heladeria_controller.calcular_costo_produccion(producto_id)
        return jsonify({'costo': costo})
    except Exception as e:
        return jsonify({'mensaje': f'Error al calcular el costo de producción: {e}'}), 500

@heladeria_bp.route('/producto/rentabilidad/<int:producto_id>')
@login_required
def calcular_rentabilidad_producto(producto_id):
    try:
        rentabilidad = heladeria_controller.calcular_rentabilidad_producto(producto_id)
        return jsonify({'rentabilidad': rentabilidad})
    except Exception as e:
        return jsonify({'mensaje': f'Error al calcular la rentabilidad del producto: {e}'}), 500

@heladeria_bp.route('/producto/mas_rentable')
@login_required
def producto_mas_rentable():
    try:
        nombre_producto = heladeria_controller.producto_mas_rentable()
        return jsonify({'producto_mas_rentable': nombre_producto})
    except Exception as e:
        return jsonify({'mensaje': f'Error al encontrar el producto más rentable: {e}'}), 500

@heladeria_bp.route('/ingrediente/sano/<int:ingrediente_id>')
@login_required
def es_ingrediente_sano(ingrediente_id):
    try:
        es_sano = heladeria_controller.es_ingrediente_sano(ingrediente_id)
        return jsonify({'es_sano': es_sano})
    except Exception as e:
        return jsonify({'mensaje': f'Error al verificar si el ingrediente es sano: {e}'}), 500

@heladeria_bp.route('/ingrediente/abastecer', methods=['POST'])
@login_required
def abastecer_ingrediente():
    try:
        ingrediente_id = request.form['ingrediente_id']
        cantidad = int(request.form['cantidad'])
        if heladeria_controller.abastecer_ingrediente(ingrediente_id, cantidad):
            return jsonify({'mensaje': 'Ingrediente abastecido'})
        else:
            return jsonify({'mensaje': 'Error al abastecer el ingrediente'}), 400
    except Exception as e:
        return jsonify({'mensaje': f'Error al abastecer el ingrediente: {e}'}), 500

@heladeria_bp.route('/ingrediente/renovar', methods=['POST'])
@login_required
def renovar_inventario_complementos():
    try:
        if heladeria_controller.renovar_inventario_complementos():
            return jsonify({'mensaje': 'Inventario de complementos renovado'})
        else:
            return jsonify({'mensaje': 'Error al renovar el inventario de complementos'}), 400
    except Exception as e:
        return jsonify({'mensaje': f'Error al renovar el inventario de complementos: {e}'}), 500
    
@heladeria_bp.route('/productos', methods=['GET'])
def consultar_todos_los_productos():
    """Consulta todos los productos."""
    try:
        productos = heladeria_controller.producto_service.get_all_productos()
        productos_info = [
            {
                'id': producto.id,
                'nombre': producto.nombre,
                'tipo_producto': producto.tipo_producto.nombre_tipo_producto,
                'precio_publico': producto.precio_publico
            } for producto in productos
        ]
        return jsonify({'productos': productos_info})
    except Exception as e:
        return jsonify({'mensaje': f'Error al consultar todos los productos: {e}'}), 500

@heladeria_bp.route('/producto/<int:producto_id>', methods=['GET'])
def consultar_producto_por_id(producto_id):
    """Consulta un producto según su ID."""
    try:
        producto = heladeria_controller.producto_service.get_producto(producto_id)
        if producto:
            return jsonify({
                'id': producto.id,
                'nombre': producto.nombre,
                'tipo_producto': producto.tipo_producto.nombre_tipo_producto,
                'precio_publico': producto.precio_publico
            })
        else:
            return jsonify({'mensaje': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'mensaje': f'Error al consultar el producto por ID: {e}'}), 500

@heladeria_bp.route('/producto/nombre/<string:nombre>', methods=['GET'])
def consultar_producto_por_nombre(nombre):
    """Consulta un producto según su nombre."""
    try:
        productos = heladeria_controller.producto_service.get_by_name(nombre)
        if productos:
            productos_info = [
                {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'tipo_producto': producto.tipo_producto.nombre_tipo_producto,
                    'precio_publico': producto.precio_publico
                } for producto in productos
            ]
            return jsonify({'productos': productos_info})
        else:
            return jsonify({'mensaje': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'mensaje': f'Error al consultar el producto por nombre: {e}'}), 500

@heladeria_bp.route('/ingredientes', methods=['GET'])
def consultar_todos_los_ingredientes():
    """Consulta todos los ingredientes."""
    try:
        ingredientes = heladeria_controller.ingrediente_service.get_all_ingredientes()
        ingredientes_info = [
            {
                'id': ingrediente.id,
                'nombre': ingrediente.nombre,
                'calorias': ingrediente.calorias,
                'es_vegetariano': ingrediente.es_vegetariano,
                'inventario': ingrediente.inventario
            } for ingrediente in ingredientes
        ]
        return jsonify({'ingredientes': ingredientes_info})
    except Exception as e:
        return jsonify({'mensaje': f'Error al consultar todos los ingredientes: {e}'}), 500

@heladeria_bp.route('/ingrediente/<int:ingrediente_id>', methods=['GET'])
def consultar_ingrediente_por_id(ingrediente_id):
    """Consulta un ingrediente según su ID."""
    try:
        ingrediente = heladeria_controller.ingrediente_service.get_ingrediente(ingrediente_id)
        if ingrediente:
            return jsonify({
                'id': ingrediente.id,
                'nombre': ingrediente.nombre,
                'calorias': ingrediente.calorias,
                'es_vegetariano': ingrediente.es_vegetariano,
                'inventario': ingrediente.inventario
            })
        else:
            return jsonify({'mensaje': 'Ingrediente no encontrado'}), 404
    except Exception as e:
        return jsonify({'mensaje': f'Error al consultar el ingrediente por ID: {e}'}), 500

@heladeria_bp.route('/ingrediente/nombre/<string:nombre>', methods=['GET'])
def consultar_ingrediente_por_nombre(nombre):
    """Consulta un ingrediente según su nombre."""
    try:
        ingredientes = heladeria_controller.ingrediente_service.get_ingrediente_by_nombre(nombre)
        if ingredientes:
            ingredientes_info = [
                {
                    'id': ingrediente.id,
                    'nombre': ingrediente.nombre,
                    'calorias': ingrediente.calorias,
                    'es_vegetariano': ingrediente.es_vegetariano,
                    'inventario': ingrediente.inventario
                } for ingrediente in ingredientes
            ]
            return jsonify({'ingredientes': ingredientes_info})
        else:
            return jsonify({'mensaje': 'Ingrediente no encontrado'}), 404
    except Exception as e:
        return jsonify({'mensaje': f'Error al consultar el ingrediente por nombre: {e}'}), 500

@heladeria_bp.route('/producto/reabastecer', methods=['POST'])
def reabastecer_producto():
    """Reabastece un producto específico según su ID y cantidad."""
    try:
        producto_id = request.form['producto_id']
        cantidad = int(request.form['cantidad'])
        if heladeria_controller.abastecer_ingrediente(producto_id, cantidad):  # Usa el método correcto
            return jsonify({'mensaje': 'Producto reabastecido'})
        else:
            return jsonify({'mensaje': 'Error al reabastecer el producto'}), 400
    except Exception as e:
        return jsonify({'mensaje': f'Error al reabastecer el producto: {e}'}), 500

@heladeria_bp.route('/producto/renovar', methods=['POST'])
def renovar_inventario_producto():
    """Renueva el inventario de un producto específico según su ID."""
    try:
        producto_id = request.form['producto_id']
        cantidad = int(request.form['cantidad'])
        if heladeria_controller.renovar_inventario_producto(producto_id,cantidad):  # Verifica si este es el método correcto
            return jsonify({'mensaje': 'Inventario de producto renovado'})
        else:
            return jsonify({'mensaje': 'Error al renovar el inventario del producto'}), 400
    except Exception as e:
        return jsonify({'mensaje': f'Error al renovar el inventario del producto: {e}'}),