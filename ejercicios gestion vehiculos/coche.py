from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self,marca,modelo,año,precio,numero_puertas):
        super().__init__(marca,modelo,año,precio)
        self.__numero_puertas = numero_puertas
    
    def arrancar(self):
        return "El coche arranca con una llave."
    
    def __str__(self):
        return f"{super().__str__()} , Numero de puertas: {self.__numero_puertas}"