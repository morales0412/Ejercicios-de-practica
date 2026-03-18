from abc import ABC, abstractmethod

class   Vehiculo (ABC):
    def __init__(self,marca,modelo,año,precio):
        self.__marca = marca
        self.__modelo = modelo
        self.año = año
        self.precio = precio
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo  
    
    @marca.setter
    def marca(self,marca):  
        self.__marca = marca
    
    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: ${self.precio}"
    
    @abstractmethod
    def arrancar(self):
        pass

