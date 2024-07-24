from Interface.Iproducto import IProducto
from models.producto import Producto
from sqlalchemy.orm import joinedload
from db import db

class ProductoService(IProducto):
    def create_producto(self, nombre, precio_publico, id_tipo_producto):
        nuevo_producto = Producto(
            nombre=nombre,
            precio_publico=precio_publico,
            id_tipo_producto=id_tipo_producto
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return nuevo_producto

    def get_all_productos(self):
          return Producto.query.options(joinedload(Producto.tipo_producto)).all()

    def get_producto(self, id):
        return Producto.query.get(id)

    def update_producto(self, id, **kwargs):
        producto = Producto.query.get(id)
        if producto:
            for key, value in kwargs.items():
                setattr(producto, key, value)
            db.session.commit()
        return producto

    def delete_producto(self, id):
        producto = Producto.query.get(id)
        if producto:
            db.session.delete(producto)
            db.session.commit()
        return producto
    def get_by_name(self,name):
          return Producto.query.filter_by(name=name).all()