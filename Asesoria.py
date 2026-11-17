
from servicio import Servicio


class AsesoriaEspecializada(Servicio):
    """
    Clase para gestionar asesorías especializadas.
    """

    def __init__(self, id_entidad: str, nombre_servicio: str,
                 costo_base: float, especialidad: str):
        super().__init__(id_entidad, nombre_servicio, costo_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError(
                "La especialidad no puede estar vacía."
            )

        self.especialidad = especialidad.strip()

    def calcular_costo(self, sesiones: int,
                       nivel_complejidad: float = 1.0) -> float:

        if (isinstance(sesiones, bool)
                or not isinstance(sesiones, int)
                or sesiones <= 0):
            raise ValueError(
                "Las sesiones deben ser un entero mayor que cero."
            )

        if (isinstance(nivel_complejidad, bool)
                or not isinstance(nivel_complejidad, (int, float))
                or nivel_complejidad <= 0):
            raise ValueError(
                "El nivel de complejidad debe ser un número mayor que cero."
            )

        return self.costo_base * sesiones * nivel_complejidad

    def describir(self) -> str:
        return (
            f"Asesoría especializada: {self.nombre_servicio} "
            f"en área {self.especialidad}"
        )




    