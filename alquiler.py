#Alquiler_Equipos

class AlquilerEquipos("servicio"):
    def __init__(self, id_entidad: str, nombre_servicio: str, costo_base: float, serial: str):
        super().__init__(id_entidad, nombre_servicio, costo_base) 
        self.serial = serial 
    
    def calcular_costo(self, dias: int, descuento: float = 0.0) -> float:
        costo = self.costo_base * dias
        if descuento > 0: 
            costo *= (1 - descuento)
        return costo 
    
    def describir(self) -> str:
        return f"Alquiler de equipo: {self.nombre_servicio} [Serial: {self.serial}]"
    
        