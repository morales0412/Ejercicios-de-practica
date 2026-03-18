from animal import Animal

class Perro(Animal):

    def __init__(self,nombre,edad,raza):
        super().__init__(nombre,edad)
        self.__raza = raza
    
    def hacer_sonido(self):
        return "Guau Guau"
    
    def moverse(self):
        return "Corriendo rapidamente"