from abc import ABC, abstractmethod 

class Empleado(ABC):
    def __init__(self, nombre,id):
        self.nombre = nombre
        self.id = id
    
    @abstractmethod
    def calcular_salario(self):
        pass