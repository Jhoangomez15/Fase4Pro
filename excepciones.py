class SoftwareFJError(Exception):
    """Excepción base del sistema Software FJ."""
    pass


class ClienteInvalidoError(SoftwareFJError):
    """Error cuando los datos de un cliente no son válidos."""
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """Error cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(SoftwareFJError):
    """Error cuando una reserva no cumple las condiciones."""
    pass