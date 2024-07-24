from Interface.ItipoProducto import ITipoProducto
from models.tipoProducto import TipoProducto
from db import db

class TipoProductoService(ITipoProducto):

    def create_tipo_producto(self, nombre, descripcion):
        nuevo_tipo_producto = TipoProducto(
            nombre_tipo_producto=nombre,
            descripcion_tipo_producto=descripcion
        )
        db.session.add(nuevo_tipo_producto)
        db.session.commit()
        return nuevo_tipo_producto

    def get_tipo_producto(self, id):
        return TipoProducto.query.get(id)

    def update_tipo_producto(self, id, **kwargs):
        tipo_producto = TipoProducto.query.get(id)
        if tipo_producto:
            for key, value in kwargs.items():
                setattr(tipo_producto, key, value)
            db.session.commit()
        return tipo_producto

    def delete_tipo_producto(self, id):
        tipo_producto = TipoProducto.query.get(id)
        if tipo_producto:
            db.session.delete(tipo_producto)
            db.session.commit()
        return tipo_producto

    def get_all_tipo_productos(self):
        return TipoProducto.query.all()