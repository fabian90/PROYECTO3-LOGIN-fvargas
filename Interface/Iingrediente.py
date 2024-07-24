from abc import ABC, abstractmethod

class IIngrediente(ABC):
    @abstractmethod
    def create_ingrediente(self, nombre, precio, calorias, inventario, es_vegetariano, tipo, sabor, volumen, id_tipo_vaso):
        pass

    @abstractmethod
    def get_ingrediente(self, id):
        pass

    @abstractmethod
    def update_ingrediente(self, id, **kwargs):
        pass

    @abstractmethod
    def delete_ingrediente(self, id):
        pass
    @abstractmethod
    def get_by_complemento(self,name):
        pass