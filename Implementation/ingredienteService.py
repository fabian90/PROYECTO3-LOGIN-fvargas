from Interface.Iingrediente import IIngrediente
from models.ingrediente import Ingrediente
from db import db

class IngredienteService(IIngrediente):
    def create_ingrediente(self, nombre, precio, calorias, inventario, es_vegetariano, tipo, sabor, volumen, id_tipo_vaso):
        nuevo_ingrediente = Ingrediente(
            nombre=nombre,
            precio=precio,
            calorias=calorias,
            inventario=inventario,
            es_vegetariano=es_vegetariano,
            tipo=tipo,
            sabor=sabor,
            volumen=volumen,
            id_tipo_vaso=id_tipo_vaso
        )
        db.session.add(nuevo_ingrediente)
        db.session.commit()
        return nuevo_ingrediente

    def get_ingrediente(self, id)->Ingrediente:
        return Ingrediente.query.get(id)

    def update_ingrediente(self, id, **kwargs):
        ingrediente = Ingrediente.query.get(id)
        if ingrediente:
            for key, value in kwargs.items():
                setattr(ingrediente, key, value)
            db.session.commit()
        return ingrediente

    def delete_ingrediente(self, id):
        ingrediente = Ingrediente.query.get(id)
        if ingrediente:
            db.session.delete(ingrediente)
            db.session.commit()
        return ingrediente
    
    def get_by_complemento(self,name):
          return Ingrediente.query.filter_by(tipo=name).all()
        
             
    
