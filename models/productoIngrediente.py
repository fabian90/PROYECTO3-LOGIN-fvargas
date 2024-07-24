from db import db
class ProductoIngrediente(db.Model):
  __tablename__ = "ProductoIngrediente"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
  id_ingrediente = db.Column(db.Integer, db.ForeignKey('ingrediente.id'), nullable=False)

# Métodos getter
def get_id(self):
    return self.id

def get_id_producto(self):
    return self.id_producto

def get_id_ingrediente(self):
    return self.id_ingrediente

def get_producto(self):
    return self.producto

def get_ingrediente(self):
    return self.ingrediente