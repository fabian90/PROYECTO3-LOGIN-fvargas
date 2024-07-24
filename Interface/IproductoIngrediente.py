from abc import ABC, abstractmethod

class IProductoIngrediente(ABC):
    @abstractmethod
    def create_producto_ingrediente(self, id_producto, id_ingrediente):
        pass

    @abstractmethod
    def get_producto_ingrediente(self, id):
        pass

    @abstractmethod
    def update_producto_ingrediente(self, id, **kwargs):
        pass

    @abstractmethod
    def delete_producto_ingrediente(self, id):
        pass
    @abstractmethod
    def get_producto_ingrediente_by_producto_id(self, id):
        pass
    @abstractmethod
    def get_producto_ingrediente_by_ingrediente_id(self, id):
        pass