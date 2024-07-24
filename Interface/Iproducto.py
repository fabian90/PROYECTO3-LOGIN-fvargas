from abc import ABC, abstractmethod

class IProducto(ABC):
    @abstractmethod
    def get_all_productos(self):
        pass
    
    @abstractmethod
    def create_producto(self, nombre, precio_publico, id_tipo_producto):
        pass
    @abstractmethod
    def get_producto(self, id):
        pass
    @abstractmethod
    def update_producto(self, id, **kwargs):
        pass
    @abstractmethod
    def delete_producto(self, id):
        pass
    @abstractmethod
    def get_by_name(self,name):
        pass
    
   