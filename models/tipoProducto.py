from db import db
class TipoProducto(db.Model):
  __tablename__ = "tipoproducto"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre_tipo_producto = db.Column(db.String(50), nullable=False, unique=True)
  descripcion_tipo_producto = db.Column(db.String(db.Text), nullable=False)
#   productos = db.relationship('TipoProducto', backref="producto", lazy=True)
#   productos = db.relationship('Producto', backref=db.backref(backref='tipo_producto'), lazy=True)
def __repr__(self):
    return f'<TipoProducto {self.nombre_tipo_producto}>'
    # Métodos getter
def get_id(self):
    return self.id
def get_nombre_tipo_producto(self):
    return self.nombre_tipo_producto
def get_descripcion_tipo_producto(self):
    return self.descripcion_tipo_producto