
from servicio import Servicio


class AlquilerEquipos(Servicio):
    """
    Clase para gestionar el alquiler de equipos.
    """

    def __init__(self, id_entidad: str, nombre_servicio: str,
                 costo_base: float, serial: str):
        super().__init__(id_entidad, nombre_servicio, costo_base)

        if not isinstance(serial, str) or not serial.strip():
            raise ValueError("El serial del equipo no puede estar vacío.")

        self.serial = serial.strip()

    def calcular_costo(self, dias: int, descuento: float = 0.0) -> float:
        if isinstance(dias, bool) or not isinstance(dias, int) or dias <= 0:
            raise ValueError("Los días deben ser un entero mayor que cero.")

        if (isinstance(descuento, bool)
                or not isinstance(descuento, (int, float))
                or not 0 <= descuento <= 1):
            raise ValueError("El descuento debe estar entre 0 y 1.")

        costo = self.costo_base * dias
        costo *= (1 - descuento)

        return costo

    def describir(self) -> str:
        return (
            f"Alquiler de equipo: {self.nombre_servicio} "
            f"[Serial: {self.serial}]"
        )


