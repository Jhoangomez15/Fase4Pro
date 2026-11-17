#Reserva
from cliente import Cliente
from servicio import Servicio

class Reserva: 
    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio, duracion: int):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"
        
    def confirmar(self): 
        self.estado = "CONFIRMADA"
        
    def cancelar(self):
        self.estado = "CANCELADA"
        
        
        
    