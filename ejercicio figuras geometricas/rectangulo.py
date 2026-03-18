from figura import Figura_geometrica


class Rectangulo(Figura_geometrica):

    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura

    @property 
    def base(self):
        return self.__base
    
    @property 
    def altura(self):
        return self.__altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f"Rectangulo de base: {self.base} y altura: {self.altura} - Area: {self.area():.2f} Perimetro: {self.perimetro():.2f}"