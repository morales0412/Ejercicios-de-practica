from producto import Producto

class ProductoFisico(Producto):
    def __init__(self,id,nombre,precio,peso):
        super().__init__(id,nombre,precio)
        self.__peso = peso
    
    def calcular_impuesto(self):
        return self.__precio *0.15

    def __str__(self):
        return f"{super().__str__()} - Peso: {self.__peso}" 