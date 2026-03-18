from figura import Figura_geometrica
import math

class Circulo(Figura_geometrica):
    pi = math.pi
    def __init__(self,radio):
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio
    
    def area(self):
        return self.pi *(self.radio **2)
    
    def perimetro(self):
        return 2 * self.pi * self.radio
    
    def __str__(self):
        return f"Circulo de radio: {self.radio} - Area: {self.area():.2f}  Perimetro: {self.perimetro():.2f}"