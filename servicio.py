#proyecto
 
from abc import ABC, abstractmethod
import logging 

class EntidadSistema(ABC): 
    """Clase abstracta base para entidades generales del sistema. """
    def __init__(self, id_entidad: str):
        self.id_entidad= id_entidad



class Servicio(EntidadSistema):
    def __init__(self, id_entidad: str, nombre_servicio: str, costo_base: float):
        super().__init__(id_entidad)
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base
        
    @abstractmethod
    def calcular_costo(self, *args, **kargs) -> float:   
        pass
    
    @abstractmethod
    def describir(self)  -> str:
        pass
    
    