#Asesoria_Especializada

class Asesoria_Especializada("Servicio"):
    def __init__(self, id_entidad: str, nombre_servicio: str, costo_base: float, especialidad: str):
        super().__init__(id_entidad, nombre_servicio, costo_base)
        self.especialidad = especialidad
        
    def calcular_costo(self, sesiones: int, nivel_complejidad: float = 1.0) -> float: 
        return self.costo_base * sesiones * nivel_complejidad
    
    def describir(self) -> str: 
        return f"Asesoria especializada: {self.nombre_servicio} en area {self.especialidad}"
    
    