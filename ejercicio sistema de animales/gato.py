from animal import Animal

class Gato(Animal):

    def __ini__(self,nombre,edad,color_pelo):
        super().__init__(nombre,edad)
        self.__color_pelo = color_pelo

    def hacer_sonido(self):
        return "Miau Miau"
    
    def moverse(self):
        return "Caminando silenciosamente"