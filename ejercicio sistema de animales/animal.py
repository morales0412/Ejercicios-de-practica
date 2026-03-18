from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property 
    def edad(self):
        return self.__edad

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass
    