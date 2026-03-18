from abc import ABC, abstractmethod
from datetime import date

class Empleado(ABC):

    def __init__(self,id,nombre,correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.__historial_salario = []
    
    @abstractmethod
    def calcular_salario(self):
        pass

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}"
    
    def registrar_pago (self,monto):
        fecha = date.today()
        self.__historial_salario.append((fecha,monto))
    
    def obtener_historial_pagos(self):
        return list(self.__historial_salario)