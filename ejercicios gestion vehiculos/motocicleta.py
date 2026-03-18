from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    
    def __init__(self,marca,modelo,año,precio,cilindrada):
        super().__init__(marca,modelo,año,precio)
        self.__cilindrada = cilindrada

    def arrancar(self):
        return "La moto arranca con pedal."
    
    def __str__(self):
        return f"{super().__str__()}, cilindrada: {self.__cilindrada} cc"