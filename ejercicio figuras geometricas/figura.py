from abc import ABC, abstractmethod

class Figura_geometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def __str__(self):
        pass