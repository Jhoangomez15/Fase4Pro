
from abc import ABC, abstractmethod


class EntidadSistema(ABC):
    """
    Clase abstracta general para las entidades
    del sistema Software FJ.
    """

    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @property
    def id_entidad(self):
        return self._id_entidad

    @abstractmethod
    def obtener_detalles(self):
        pass
