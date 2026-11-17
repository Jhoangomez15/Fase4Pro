
from cliente import Cliente
from servicio import Servicio
from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError
)
import logging


class Reserva:
    """
    Clase que gestiona las reservas del sistema Software FJ.
    """

    def __init__(
        self,
        id_reserva: str,
        cliente: Cliente,
        servicio: Servicio,
        duracion: int
    ):
        if not isinstance(id_reserva, str) or not id_reserva.strip():
            raise ReservaInvalidaError(
                "El identificador de la reserva no puede estar vacío."
            )

        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "Debe proporcionar un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "Debe proporcionar un servicio válido."
            )

        if (isinstance(duracion, bool)
                or not isinstance(duracion, int)
                or duracion <= 0):
            raise ReservaInvalidaError(
                "La duración debe ser un número entero mayor que cero."
            )

        self._id_reserva = id_reserva.strip()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "PENDIENTE"

    @property
    def id_reserva(self):
        return self._id_reserva

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    def confirmar(self):
        if self._estado != "PENDIENTE":
            raise ReservaInvalidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "CONFIRMADA"
        logging.info("Reserva %s confirmada.", self._id_reserva)
        return self._estado

    def cancelar(self):
        if self._estado not in ("PENDIENTE", "CONFIRMADA"):
            raise ReservaInvalidaError(
                "No se puede cancelar una reserva ya procesada."
            )

        self._estado = "CANCELADA"
        logging.info("Reserva %s cancelada.", self._id_reserva)
        return self._estado

    def procesar(self):
        if self._estado != "CONFIRMADA":
            raise ReservaInvalidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            costo = self._servicio.calcular_costo(self._duracion)

        except Exception as error:
            logging.exception(
                "Error al procesar la reserva %s.",
                self._id_reserva
            )
            raise ServicioNoDisponibleError(
                "No fue posible procesar el servicio."
            ) from error

        self._estado = "PROCESADA"
        logging.info("Reserva %s procesada correctamente.", self._id_reserva)

        return {
            "id_reserva": self._id_reserva,
            "cliente": self._cliente.obtener_detalles(),
            "servicio": self._servicio.describir(),
            "duracion": self._duracion,
            "costo": costo,
            "estado": self._estado
        }



        
        
        
    