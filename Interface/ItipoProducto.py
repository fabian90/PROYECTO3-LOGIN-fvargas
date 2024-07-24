from abc import ABC, abstractmethod

class ITipoProducto(ABC):
    @abstractmethod
    def create_tipo_producto(self, nombre_tipo_producto, descripcion_tipo_producto):
        pass

    @abstractmethod
    def get_tipo_producto(self, id):
        pass

    @abstractmethod
    def update_tipo_producto(self, id, **kwargs):
        pass

    @abstractmethod
    def delete_tipo_producto(self, id):
        pass

    @abstractmethod
    def get_all_tipo_productos(self):
        pass