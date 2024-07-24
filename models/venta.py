from db import db
class Venta(db.Model):
  __tablename__ = "Venta"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id'), nullable=False)
  fecha_venta = db.Column(db.Date, nullable=False)
  total = db.Column(db.DECIMAL(10, 2), nullable=False)

  producto = db.relationship("Producto")