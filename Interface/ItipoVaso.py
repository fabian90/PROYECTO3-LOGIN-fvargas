from abc import ABC, abstractmethod

class ITipoVaso(ABC):
    @abstractmethod
    def create_tipo_vaso(self, nombre, descripcion):
        pass

    @abstractmethod
    def get_tipo_vaso(self, id):
        pass

    @abstractmethod
    def update_tipo_vaso(self, id, **kwargs):
        pass

    @abstractmethod
    def delete_tipo_vaso(self, id):
        pass