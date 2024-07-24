from flask import Blueprint, render_template, request, jsonify
from flask import Blueprint, request, jsonify
from Controllers.heladeriaController import HeladeriaController
from flask_login import login_required, current_user

heladeria_bp = Blueprint('heladeria', __name__)
heladeria_controller = HeladeriaController()

@heladeria_bp.route('/')
# @login_required
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
def calcular_calorias_producto(producto_id):
    try:
        calorias = heladeria_controller.calcular_calorias_producto(producto_id)
        return jsonify({'calorias': calorias})
    except Exception as e:
        return jsonify({'mensaje': f'Error al calcular las calorías del producto: {e}'}), 500

@heladeria_bp.route('/producto/costo/<int:producto_id>')
def calcular_costo_produccion(producto_id):
    try:
        costo = heladeria_controller.calcular_costo_produccion(producto_id)
        return jsonify({'costo': costo})
    except Exception as e:
        return jsonify({'mensaje': f'Error al calcular el costo de producción: {e}'}), 500

@heladeria_bp.route('/producto/rentabilidad/<int:producto_id>')
def calcular_rentabilidad_producto(producto_id):
    try:
        rentabilidad = heladeria_controller.calcular_rentabilidad_producto(producto_id)
        return jsonify({'rentabilidad': rentabilidad})
    except Exception as e:
        return jsonify({'mensaje': f'Error al calcular la rentabilidad del producto: {e}'}), 500

@heladeria_bp.route('/producto/mas_rentable')
def producto_mas_rentable():
    try:
        nombre_producto = heladeria_controller.producto_mas_rentable()
        return jsonify({'producto_mas_rentable': nombre_producto})
    except Exception as e:
        return jsonify({'mensaje': f'Error al encontrar el producto más rentable: {e}'}), 500

@heladeria_bp.route('/ingrediente/sano/<int:ingrediente_id>')
def es_ingrediente_sano(ingrediente_id):
    try:
        es_sano = heladeria_controller.es_ingrediente_sano(ingrediente_id)
        return jsonify({'es_sano': es_sano})
    except Exception as e:
        return jsonify({'mensaje': f'Error al verificar si el ingrediente es sano: {e}'}), 500

@heladeria_bp.route('/ingrediente/abastecer', methods=['POST'])
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
def renovar_inventario_complementos():
    try:
        if heladeria_controller.renovar_inventario_complementos():
            return jsonify({'mensaje': 'Inventario de complementos renovado'})
        else:
            return jsonify({'mensaje': 'Error al renovar el inventario de complementos'}), 400
    except Exception as e:
        return jsonify({'mensaje': f'Error al renovar el inventario de complementos: {e}'}), 500