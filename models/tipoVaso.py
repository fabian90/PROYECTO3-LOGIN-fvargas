from db import db
class TipoVaso(db.Model):
  __tablename__ = "tipovaso"

  id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
  nombre = db.Column(db.String(255), nullable=False, unique=True)
  descripcion = db.Column(db.String(255))
#   ingredientes = db.relationship('Ingrediente', backref='tipo_vaso', lazy=True)

  # Métodos getter
  def get_id(self):
      return self.id

  def get_nombre(self):
      return self.nombre

  def get_descripcion(self):
      return self.descripcion