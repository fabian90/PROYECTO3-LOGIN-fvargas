from Interface.IproductoIngrediente import IProductoIngrediente
from models.productoIngrediente import ProductoIngrediente
from db import db

class ProductoIngredienteService(IProductoIngrediente):
    def create_producto_ingrediente(self, id_producto, id_ingrediente):
        nuevo_producto_ingrediente = ProductoIngrediente(
            id_producto=id_producto,
            id_ingrediente=id_ingrediente
        )
        db.session.add(nuevo_producto_ingrediente)
        db.session.commit()
        return nuevo_producto_ingrediente

    def get_producto_ingrediente(self, id):
        return ProductoIngrediente.query.get(id)
    
    def get_producto_ingrediente_by_producto_id(self, id):
        return ProductoIngrediente.query.filter_by(id_producto=id)
    
    def get_producto_ingrediente_by_ingrediente_id(self, id):
        return ProductoIngrediente.query.filter_by(id_ingrediente=id)

    def update_producto_ingrediente(self, id, **kwargs):
        producto_ingrediente = ProductoIngrediente.query.get(id)
        if producto_ingrediente:
            for key, value in kwargs.items():
                setattr(producto_ingrediente, key, value)
            db.session.commit()
        return producto_ingrediente

    def delete_producto_ingrediente(self, id):
        producto_ingrediente = ProductoIngrediente.query.get(id)
        if producto_ingrediente:
            db.session.delete(producto_ingrediente)
            db.session.commit()
        return producto_ingrediente