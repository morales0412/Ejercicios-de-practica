from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def presentarse(self):
        pass


class Estudiante(Persona):
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años. Soy estudiante.")


estudiante = Estudiante("Juan", 20)
estudiante.presentarse()
