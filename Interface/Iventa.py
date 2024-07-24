from abc import ABC, abstractmethod

class IVenta(ABC):
    @abstractmethod
    def create_venta(self, id_producto, cantidad, fecha):
        pass

    @abstractmethod
    def get_venta(self, id):
        pass

    @abstractmethod
    def update_venta(self, id, **kwargs):
        pass

    @abstractmethod
    def delete_venta(self, id):
        pass