from db import db
class Ingrediente(db.Model):
  __tablename__ = "Ingrediente"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255), nullable=False, unique=True)
  precio = db.Column(db.DECIMAL(10, 2), nullable=False)
  calorias = db.Column(db.Integer, nullable=False)
  inventario = db.Column(db.Integer, nullable=False)
  es_vegetariano = db.Column(db.Boolean, nullable=False)
  tipo = db.Column(db.String(255), nullable=False)
  sabor = db.Column(db.String(255))
  volumen = db.Column(db.DECIMAL(10, 2))
  id_tipo_vaso = db.Column(db.Integer, db.ForeignKey('tipovaso.id'), nullable=False)
  tipo_vaso = db.relationship('TipoVaso', backref=db.backref("ingredientes", lazy=True)) 


def es_sano(self):
    return self.calorias < 100 or self.es_vegetariano
def __repr__(self):
        return f'<Ingrediente {self.nombre}>'

   # Métodos getter
@property
def get_id(self):
    return self.id
@property
def get_nombre(self):
    return self.nombre
@property
def get_precio(self):
    return self.precio
@property
def get_calorias(self):
    return self.calorias
@property
def get_inventario(self):
    return self.inventario
@property
def get_es_vegetariano(self):
    return self.es_vegetariano
@property
def get_tipo(self):
    return self.tipo
@property
def get_sabor(self):
    return self.sabor
@property
def get_volumen(self):
    return self.volumen
@property
def get_id_tipo_vaso(self):
    return self.id_tipo_vaso
@property
def get_tipo_vaso(self):
    return self.tipo_vaso
