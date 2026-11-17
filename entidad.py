
from abc import ABC, abstractmethod


class EntidadSistema(ABC):
    """
    Clase abstracta general para las entidades
    del sistema Software FJ.
    """

    def __init__(self, id_entidad):
        if not isinstance(id_entidad, str) or not id_entidad.strip():
            raise ValueError(
                "El identificador de la entidad no puede estar vacío."
            )

        self._id_entidad = id_entidad.strip()

    @property
    def id_entidad(self):
        return self._id_entidad

    @abstractmethod
    def obtener_detalles(self):
        pass

