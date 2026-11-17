
import math
from abc import abstractmethod
from entidad import EntidadSistema


class Servicio(EntidadSistema):
    """
    Clase abstracta base para los servicios
    del sistema Software FJ.
    """

    def __init__(self, id_entidad: str, nombre_servicio: str,
                 costo_base: float):

        if not isinstance(id_entidad, str) or not id_entidad.strip():
            raise ValueError(
                "El identificador del servicio no puede estar vacío."
            )

        super().__init__(id_entidad.strip())

        if not isinstance(nombre_servicio, str) or not nombre_servicio.strip():
            raise ValueError(
                "El nombre del servicio no puede estar vacío."
            )

        self.nombre_servicio = nombre_servicio.strip()

        if (isinstance(costo_base, bool)
                or not isinstance(costo_base, (int, float))
                or not math.isfinite(costo_base)
                or costo_base <= 0):
            raise ValueError(
                "El costo base debe ser un número mayor que cero."
            )

        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs) -> float:
        pass

    @abstractmethod
    def describir(self) -> str:
        pass

    def obtener_detalles(self):
        return self.describir()

