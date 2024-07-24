from db import db
class Producto(db.Model):
    __tablename__ = 'producto'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio_publico = db.Column(db.Numeric(10, 2), nullable=False)
    id_tipo_producto = db.Column(db.Integer, db.ForeignKey('tipoproducto.id'), nullable=False)  
    tipo_producto = db.relationship('TipoProducto', backref=db.backref('productos', lazy=True))
    # tipo_producto = db.relationship('TipoProducto', back_populates='productos')
    # producto = db.Column(db.Integer, db.ForeignKey('tipoproducto.id'))
#   tipo_producto = db.relationship("TipoProducto")

def __repr__(self):
        return f'<Producto {self.nombre}>'
# Métodos getter
@property
def get_id(self):
    return self.id
@property
def get_nombre(self):
    return self.nombre
@property
def get_precio_publico(self):
    return self.precio_publico
@property
def get_id_tipo_producto(self):
    return self.id_tipo_producto
@property
def get_tipo_producto(self):
    return self.tipo_producto

# @staticmethod
# def get_all_productos(cls):
#     return cls.query.all()

# @staticmethod
# def get_producto(cls,producto_id):
#     return cls.query.get(producto_id)

# def as_dict(self):
#     return {
#         'id': self.id,
#         'nombre': self.nombre,
#         'precio_publico': str(self.precio_publico),
#         'id_tipo_producto': self.id_tipo_producto
#     }