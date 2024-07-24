# tests/test_heladeria_controller.py

import pytest
from unittest.mock import MagicMock, patch
from Controllers.heladeriaController import HeladeriaController
from db import db

@pytest.fixture
def mock_services():
    # Crea mocks para los servicios
    producto_service = MagicMock()
    ingrediente_service = MagicMock()
    producto_ingrediente_service = MagicMock()
    tipo_producto_service = MagicMock()
    
    # Crea un mock para db.session
    db_session_mock = MagicMock()
    db.session = db_session_mock

    controller = HeladeriaController()
    controller.producto_service = producto_service
    controller.ingrediente_service = ingrediente_service
    controller.producto_ingrediente_service = producto_ingrediente_service
    controller.producto_tipo_service = tipo_producto_service
    
    return controller, producto_service, ingrediente_service, producto_ingrediente_service, tipo_producto_service, db_session_mock

# Pruebas unitarias
def test_es_ingrediente_sano(mock_services):
    controller, _, ingrediente_service, _, _, _ = mock_services
    ingrediente = MagicMock()
    ingrediente.calorias = 50
    ingrediente.es_vegetariano = False
    ingrediente_service.get_ingrediente.return_value = ingrediente
    
    sano = controller.es_ingrediente_sano(1)
    
    assert sano == True

def test_abastecer_ingrediente(mock_services):
    controller, _, ingrediente_service, _, _, db_session_mock = mock_services
    ingrediente = MagicMock()
    ingrediente.inventario = 5
    ingrediente_service.get_ingrediente.return_value = ingrediente
    
    resultado = controller.abastecer_ingrediente(1, 10)
    
    assert resultado == True
    ingrediente_service.update_ingrediente.assert_called_once_with(1, inventario=15)
    db_session_mock.commit.assert_called_once()

def test_renovar_inventario_complementos(mock_services):
    controller, _, ingrediente_service, _, _, db_session_mock = mock_services
    complemento = MagicMock()
    complemento.inventario = 5
    ingrediente_service.get_by_complemento.return_value = [complemento]
    
    resultado = controller.renovar_inventario_complementos()
    
    assert resultado == True
    ingrediente_service.update_ingrediente.assert_called_once_with(complemento.id, inventario=15)
    db_session_mock.commit.assert_called_once()

def test_calcular_calorias_producto(mock_services):
    controller, producto_service, ingrediente_service, producto_ingrediente_service, _, _ = mock_services
    producto = MagicMock()
    producto.tipo_producto.nombre_tipo_producto = 'malteada'
    producto_service.get_producto.return_value = producto
    
    ingrediente = MagicMock()
    ingrediente.calorias = 50
    producto_ingrediente_service.get_producto_ingrediente_by_producto_id.return_value = [MagicMock(id_ingrediente=1)]
    ingrediente_service.get_ingrediente.return_value = ingrediente
    
    calorias_totales, sano = controller.calcular_calorias_producto(1)
    
    assert calorias_totales == 237.5
    assert sano == True

def test_calcular_costo_produccion(mock_services):
    controller, producto_service, ingrediente_service, producto_ingrediente_service, _, _ = mock_services
    producto = MagicMock()
    producto.tipo_producto.nombre_tipo_producto = 'malteada'
    producto_service.get_producto.return_value = producto
    
    ingrediente = MagicMock()
    ingrediente.precio = 100
    producto_ingrediente_service.get_producto_ingrediente_by_producto_id.return_value = [MagicMock(id_ingrediente=1)]
    ingrediente_service.get_ingrediente.return_value = ingrediente
    
    costo = controller.calcular_costo_produccion(1)
    
    assert costo == 600

def test_calcular_rentabilidad_producto(mock_services):
    controller, producto_service, _, _, _, _ = mock_services
    producto = MagicMock()
    producto.precio_publico = 200
    producto_service.get_producto.return_value = producto
    
    controller.calcular_costo_produccion = MagicMock(return_value=100)
    
    rentabilidad = controller.calcular_rentabilidad_producto(1)
    
    assert rentabilidad == 100

def test_producto_mas_rentable(mock_services):
    controller, producto_service, _, _, _, _ = mock_services
    producto = MagicMock()
    producto.id = 1
    producto.precio_publico = 200
    producto_service.get_all_productos.return_value = [producto]
    
    controller.calcular_rentabilidad_producto = MagicMock(return_value=100)
    
    nombre_producto = controller.producto_mas_rentable()
    
    assert nombre_producto == producto.nombre

def test_vender_producto(mock_services):
    controller, producto_service, ingrediente_service, producto_ingrediente_service, _, db_session_mock = mock_services
    producto = MagicMock()
    producto.precio_publico = 100
    producto_service.get_producto.return_value = producto

    ingrediente = MagicMock()
    ingrediente.inventario = 1
    ingrediente_service.get_ingrediente.return_value = ingrediente

    resultado = controller.vender_producto(1)

    assert resultado == "¡Vendido!"
    # ingrediente_service.update_ingrediente.assert_called_once_with(ingrediente.id, inventario=0.8)
