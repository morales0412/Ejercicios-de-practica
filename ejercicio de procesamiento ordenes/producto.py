from abc import ABC, abstractmethod

class Producto(ABC):
    
    def __init__(self,id,nombre,precio):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio

    @abstractmethod
    def calcular_impuesto(self):
        pass

    def __str__(self):
        return f"ID: {self.__id}, Nombre: {self.__nombre}, Precio: {self.__precio}"

