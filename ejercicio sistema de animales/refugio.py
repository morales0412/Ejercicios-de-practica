class Refugio:
    def __init__(self):
        self.__residentes = []

    def admitir_animal(self,animal):
        if animal.nombre not in [a.nombre for a in self.__residentes]:
            self.__residentes.append(animal)
            print(f"Animal {animal.nombre} admitido en el refugio.")
        else:
            print(f"El animal {animal.nombre} ya esta en el refugio.")
    
    def hora_siesta(self):
        if not self.__residentes:
            print("No hay animales en el refugio.")
            return
        for animal in self.__residentes:
            print("-" * 20)
            print(f"{animal.nombre}")
            print(animal.hacer_sonido())
            print(animal.moverse())
            print("-" * 20)
    
    def listar_residentes(self):
        if not self.__residentes:
            print("No hay animales en el refugio.")
            return
        print("Animales en el refugio: ")
        for i,animal in enumerate(self.__residentes,1):
            print("-" * 20)
            print(f"{i}. {animal.nombre} - Edad: {animal.edad} años")
            print("-" * 20)