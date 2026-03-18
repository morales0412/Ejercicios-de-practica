from producto import Producto

class ProductoDigital(Producto):

    def __init__(self,id,nombre,precio):
        super().__init__(id,nombre,precio)
    
    def calcular_impuesto(self):
        return self.__precio * 0.05

    def __str__(self):
        return f"{super().__str__()} - Impuesto: {self.calcular_impuesto()}"