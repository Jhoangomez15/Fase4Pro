
from servicio import Servicio


class ReservaSala(Servicio):
    """
    Clase para gestionar reservas de salas.
    """

    def __init__(self, id_entidad: str, nombre_servicio: str,
                 costo_base: float, capacidad: int):
        super().__init__(id_entidad, nombre_servicio, costo_base)

        if (isinstance(capacidad, bool)
                or not isinstance(capacidad, int)
                or capacidad <= 0):
            raise ValueError(
                "La capacidad debe ser un entero mayor que cero."
            )

        self.capacidad = capacidad

    def calcular_costo(self, horas: int,
                       aplicar_impuesto: bool = True) -> float:

        if (isinstance(horas, bool)
                or not isinstance(horas, int)
                or horas <= 0):
            raise ValueError(
                "Las horas deben ser un entero mayor que cero."
            )

        if not isinstance(aplicar_impuesto, bool):
            raise ValueError(
                "La aplicación del impuesto debe ser verdadera o falsa."
            )

        costo = self.costo_base * horas

        if aplicar_impuesto:
            costo *= 1.19

        return costo

    def describir(self) -> str:
        return (
            f"Reserva de sala: {self.nombre_servicio} "
            f"(capacidad: {self.capacidad} personas)"
        )

    
        
