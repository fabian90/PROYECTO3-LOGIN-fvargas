from Interface.ItipoVaso import ITipoVaso
from models.tipoVaso import TipoVaso
from db import db

class TipoVasoService(ITipoVaso):
    def create_tipo_vaso(self, nombre, descripcion):
        nuevo_tipo_vaso = TipoVaso(
            nombre=nombre,
            descripcion=descripcion
        )
        db.session.add(nuevo_tipo_vaso)
        db.session.commit()
        return nuevo_tipo_vaso

    def get_tipo_vaso(self, id):
        return TipoVaso.query.get(id)

    def update_tipo_vaso(self, id, **kwargs):
        tipo_vaso = TipoVaso.query.get(id)
        if tipo_vaso:
            for key, value in kwargs.items():
                setattr(tipo_vaso, key, value)
            db.session.commit()
        return tipo_vaso

    def delete_tipo_vaso(self, id):
        tipo_vaso = TipoVaso.query.get(id)
        if tipo_vaso:
            db.session.delete(tipo_vaso)
            db.session.commit()
        return tipo_vaso