from figura import Figura_geometrica

class Triangulo(Figura_geometrica):
    
    def __init__(self,base,altura,lado1,lado2,lado3):
        self.__base = base
        self.__altura = altura
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    @property
    def base(self):
        return self.__base
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def lado1(self):    
        return self.__lado1    
    
    @property
    def lado2(self):    
        return self.__lado2
    
    @property
    def lado3(self):    
        return self.__lado3
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def __str__(self):
        return f"Triangulo de base: {self.base}, altura: {self.altura}, lados: {self.lado1}, {self.lado2}, {self.lado3} - Area: {self.area():.2f} Perimetro: {self.perimetro():.2f}"