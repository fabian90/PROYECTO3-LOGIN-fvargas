from Interface.Iventa import IVenta
from models.venta import Venta
from db import db

class VentaService(IVenta):
    def create_venta(self, id_producto, cantidad, fecha):
        nueva_venta = Venta(
            id_producto=id_producto,
            cantidad=cantidad,
            fecha=fecha
        )
        db.session.add(nueva_venta)
        db.session.commit()
        return nueva_venta

    def get_venta(self, id):
        return Venta.query.get(id)

    def update_venta(self, id, **kwargs):
        venta = Venta.query.get(id)
        if venta:
            for key, value in kwargs.items():
                setattr(venta, key, value)
            db.session.commit()
        return venta

    def delete_venta(self, id):
        venta = Venta.query.get(id)
        if venta:
            db.session.delete(venta)
            db.session.commit()
        return venta