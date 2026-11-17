
import logging

# Configuración del registro de eventos y errores
logging.basicConfig(
    filename="registro_software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logging.info("Sistema Software FJ iniciado.")
from cliente import Cliente
from reservasala import ReservaSala
from alquiler import AlquilerEquipos
from Asesoria import AsesoriaEspecializada
from Reserva import Reserva

from excepciones import (
    ClienteInvalidoError,
    ReservaInvalidaError,
    ServicioNoDisponibleError
)
def registrar_resultado(mensaje):
    print(mensaje)
    logging.info(mensaje)
    # OPERACIÓN 1: Registro de un cliente válido
try:
    cliente1 = Cliente(
        "C01",
        "Ana Perez",
        "ana@example.com",
        "3001234567"
    )

    registrar_resultado(
        f"Cliente registrado correctamente: {cliente1.obtener_detalles()}"
    )

except ClienteInvalidoError as error:
    logging.error(f"Error al registrar el cliente: {error}")
    print(f"Error: {error}")
    # OPERACIÓN 2: Registro de un cliente con correo inválido
try:
    cliente2 = Cliente(
        "C02",
        "Carlos Ruiz",
        "correo_invalido.com",
        "3001234567"
    )

    registrar_resultado("Cliente 2 registrado correctamente.")

except ClienteInvalidoError as error:
    logging.error(f"Operación 2 - Error de cliente: {error}")
    print(f"Cliente rechazado correctamente: {error}")
    # OPERACIÓN 3: Crear y procesar una reserva de sala
try:
    sala1 = ReservaSala(
        "S01",
        "Sala de reuniones",
        100000,
        10
    )

    reserva1 = Reserva("R01", cliente1, sala1, 2)
    reserva1.confirmar()

    resultado = reserva1.procesar()

    registrar_resultado(
        f"Reserva de sala procesada: {resultado}"
    )

except (ReservaInvalidaError, ServicioNoDisponibleError) as error:
    logging.error(f"Operación 3 - Error en reserva: {error}")
    print(f"Error en la reserva: {error}")
    # OPERACIÓN 4: Crear y procesar un alquiler de equipos
try:
    equipo1 = AlquilerEquipos(
        "E01",
        "Computador",
        50000,
        "ABC123"
    )

    reserva2 = Reserva("R02", cliente1, equipo1, 2)
    reserva2.confirmar()

    resultado = reserva2.procesar()

    registrar_resultado(
        f"Alquiler de equipos procesado: {resultado}"
    )

except (ReservaInvalidaError, ServicioNoDisponibleError) as error:
    logging.error(f"Operación 4 - Error en reserva: {error}")
    print(f"Error en el alquiler: {error}")
    # OPERACIÓN 5: Crear y procesar una asesoría especializada
try:
    asesoria1 = AsesoriaEspecializada(
        "A01",
        "Consultoria informatica",
        80000,
        "Ciberseguridad"
    )

    reserva3 = Reserva("R03", cliente1, asesoria1, 2)
    reserva3.confirmar()

    resultado = reserva3.procesar()

    registrar_resultado(
        f"Asesoría especializada procesada: {resultado}"
    )

except (ReservaInvalidaError, ServicioNoDisponibleError) as error:
    logging.error(f"Operación 5 - Error en reserva: {error}")
    print(f"Error en la asesoría: {error}")
    # OPERACIÓN 6: Registro de un cliente con teléfono inválido
try:
    cliente3 = Cliente(
        "C03",
        "Laura Gomez",
        "laura@example.com",
        "telefono123"
    )

    registrar_resultado("Cliente 3 registrado correctamente.")

except ClienteInvalidoError as error:
    logging.error(f"Operación 6 - Error de cliente: {error}")
    print(f"Cliente rechazado correctamente: {error}")
    # OPERACIÓN 7: Intentar crear una reserva con duración inválida
try:
    reserva_invalida = Reserva(
        "R04",
        cliente1,
        sala1,
        0
    )

    registrar_resultado("Reserva creada correctamente.")

except ReservaInvalidaError as error:
    logging.error(f"Operación 7 - Error de reserva: {error}")
    print(f"Reserva rechazada correctamente: {error}")
    # OPERACIÓN 8: Cancelar una reserva pendiente
try:
    reserva4 = Reserva("R05", cliente1, sala1, 3)

    reserva4.cancelar()

    registrar_resultado(
        f"Reserva {reserva4.id_reserva} cancelada correctamente. "
        f"Estado: {reserva4.estado}"
    )

except ReservaInvalidaError as error:
    logging.error(f"Operación 8 - Error al cancelar: {error}")
    print(f"No fue posible cancelar la reserva: {error}")
    # OPERACIÓN 9: Intentar procesar una reserva pendiente
try:
    reserva5 = Reserva("R06", cliente1, equipo1, 2)

    resultado = reserva5.procesar()

    registrar_resultado(
        f"Reserva procesada: {resultado}"
    )

except ReservaInvalidaError as error:
    logging.error(f"Operación 9 - Error al procesar: {error}")
    print(f"Proceso rechazado correctamente: {error}")
    # OPERACIÓN 10: Validar el nivel de complejidad de una asesoría
try:
    costo = asesoria1.calcular_costo(2, -1)

except ValueError as error:
    logging.error(f"Operación 10 - Error en asesoría: {error}")
    print(f"Asesoría rechazada correctamente: {error}")

else:
    registrar_resultado(f"Costo de asesoría calculado: {costo}")

finally:
    logging.info("Operación 10 finalizada.")
    print("Finalizó la operación 10.")