#Reserva_sala

class ReservaSala("Servicio"):
    def __init__(self, id_entidad: str, nombre_servicio: str, costo_base: float, capacidad: int): 
        super().__init__(id_entidad, nombre_servicio, costo_base)
        self.capacidad = capacidad
    
    def calcular_costo(self, horas: int, aplicar_impuesto: bool = True) -> float:
        costo = self.costo_base * horas
        if aplicar_impuesto:
            costo *= 1.19 #IVA 19%
        return costo
    
    def describir(self) -> str:
        return f"Reserva de Sala: {self.nombre_servicio} (capacidad: {self.capacidad} personas)"
    
    
        
